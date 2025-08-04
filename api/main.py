from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io
from typing import List, Optional, Dict, Any
import json

from src.ai_utils import get_data_insights, generate_text_embedding
from src.db_utils import (
    get_dataset,
    get_dataset_names,
    store_dataset,
    vector_search,
    get_database
)

app = FastAPI(
    title="Plot Pyre API",
    description="Backend API for Plot Pyre - AI-Powered Data Visualization Tool",
    version="1.0.0"
)

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Plot Pyre API - AI-Powered Data Visualization Backend"}

@app.get("/datasets")
async def list_datasets():
    """Get list of all available datasets"""
    try:
        dataset_names = get_dataset_names()
        return {"datasets": dataset_names}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching datasets: {str(e)}")

@app.get("/datasets/{dataset_name}")
async def get_dataset_by_name(dataset_name: str):
    """Get a specific dataset by name"""
    try:
        df = get_dataset(dataset_name)
        # Convert DataFrame to JSON-compatible format
        dataset_dict = {
            "name": dataset_name,
            "data": df.to_dict(orient="records"),
            "columns": df.columns.tolist(),
            "row_count": len(df),
            "memory_usage": df.memory_usage(deep=True).sum()
        }
        return dataset_dict
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Dataset not found: {str(e)}")

@app.post("/datasets/upload")
async def upload_dataset(
    file: UploadFile = File(...),
    dataset_name: str = None
):
    """Upload and store a dataset"""
    try:
        # Read file content
        content = await file.read()
        
        # Determine file extension
        filename = file.filename
        extension = filename.split('.')[-1] if '.' in filename else ''
        
        # Set dataset name if not provided
        if not dataset_name:
            dataset_name = filename.split('.')[0] if '.' in filename else filename
        
        # Process based on file type
        if extension.lower() == 'csv':
            df = pd.read_csv(io.StringIO(content.decode('utf-8')))
        elif extension.lower() in ['xlsx', 'xls']:
            df = pd.read_excel(io.BytesIO(content))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")
        
        # Store dataset
        num_records = store_dataset(dataset_name, df)
        
        return {
            "message": f"Dataset '{dataset_name}' uploaded successfully",
            "records": num_records,
            "columns": df.columns.tolist()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading dataset: {str(e)}")

@app.post("/ai/insights")
async def generate_insights(dataset_name: str, request: Dict[str, Any] = None):
    """Generate AI insights for a dataset"""
    try:
        # Get dataset
        df = get_dataset(dataset_name)
        
        # Extract parameters from request
        specific_columns = request.get("specific_columns") if request else None
        question = request.get("question") if request else None
        
        # Generate insights
        insights = get_data_insights(
            df,
            specific_columns=specific_columns,
            question=question
        )
        
        return {"insights": insights}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating insights: {str(e)}")

@app.post("/ai/embedding")
async def create_embedding(text: str):
    """Generate text embedding"""
    try:
        embedding = generate_text_embedding(text)
        return {"embedding": embedding, "text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating embedding: {str(e)}")

@app.post("/search/vector")
async def vector_search_endpoint(
    dataset_name: str,
    query: str,
    num_results: int = 5,
    text_field_to_return: Optional[str] = None
):
    """Perform vector search on a dataset"""
    try:
        # Perform vector search
        search_results_df = vector_search(
            dataset_name,
            query,
            index_field="embedding",
            num_results=num_results,
            text_field_to_return=text_field_to_return,
        )
        
        # Convert to JSON
        if not search_results_df.empty:
            results = search_results_df.to_dict(orient="records")
        else:
            results = []
        
        return {"results": results, "query": query}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during vector search: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
