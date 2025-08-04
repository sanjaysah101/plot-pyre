"""
Offline-first utilities for Plot Pyre
Handles local storage, caching, and PWA features
"""
import json
import os
import pickle
from pathlib import Path
import pandas as pd
from typing import Dict, Any, Optional, List
import hashlib
import streamlit as st

# Local storage configuration
LOCAL_STORAGE_DIR = Path.home() / ".plot_pyre" / "local_storage"
CACHE_DIR = LOCAL_STORAGE_DIR / "cache"
DATASETS_DIR = LOCAL_STORAGE_DIR / "datasets"
VISUALIZATIONS_DIR = LOCAL_STORAGE_DIR / "visualizations"

# Ensure directories exist
for dir_path in [LOCAL_STORAGE_DIR, CACHE_DIR, DATASETS_DIR, VISUALIZATIONS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

class OfflineStorage:
    """Handles offline storage of datasets, visualizations, and AI insights"""
    
    @staticmethod
    def save_dataset_locally(dataset_name: str, df: pd.DataFrame, metadata: Dict[str, Any] = None):
        """Save dataset to local storage"""
        try:
            dataset_path = DATASETS_DIR / f"{dataset_name}.parquet"
            metadata_path = DATASETS_DIR / f"{dataset_name}_metadata.json"
            
            # Save dataframe as parquet for efficient storage
            df.to_parquet(dataset_path, index=False)
            
            # Save metadata
            if metadata is None:
                metadata = {}
            metadata.update({
                "dataset_name": dataset_name,
                "rows": len(df),
                "columns": list(df.columns),
                "saved_at": pd.Timestamp.now().isoformat()
            })
            
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
                
            return str(dataset_path)
        except Exception as e:
            st.error(f"Error saving dataset locally: {e}")
            return None
    
    @staticmethod
    def load_local_dataset(dataset_name: str) -> Optional[pd.DataFrame]:
        """Load dataset from local storage"""
        try:
            dataset_path = DATASETS_DIR / f"{dataset_name}.parquet"
            if dataset_path.exists():
                return pd.read_parquet(dataset_path)
            return None
        except Exception as e:
            st.error(f"Error loading local dataset: {e}")
            return None
    
    @staticmethod
    def list_local_datasets() -> List[Dict[str, Any]]:
        """List all locally stored datasets"""
        datasets = []
        for metadata_path in DATASETS_DIR.glob("*_metadata.json"):
            try:
                with open(metadata_path, 'r') as f:
                    metadata = json.load(f)
                    datasets.append(metadata)
            except:
                continue
        return sorted(datasets, key=lambda x: x.get("saved_at", ""), reverse=True)
    
    @staticmethod
    def cache_ai_insights(dataset_name: str, insights: str, query: str = None):
        """Cache AI insights for offline access"""
        try:
            cache_key = f"{dataset_name}_{hashlib.md5(query.encode()).hexdigest()[:8]}" if query else dataset_name
            cache_path = CACHE_DIR / f"{cache_key}_insights.json"
            
            cache_data = {
                "dataset_name": dataset_name,
                "query": query,
                "insights": insights,
                "cached_at": pd.Timestamp.now().isoformat()
            }
            
            with open(cache_path, 'w') as f:
                json.dump(cache_data, f, indent=2)
                
            return str(cache_path)
        except Exception as e:
            st.error(f"Error caching insights: {e}")
            return None
    
    @staticmethod
    def get_cached_insights(dataset_name: str, query: str = None) -> Optional[str]:
        """Retrieve cached AI insights"""
        try:
            cache_key = f"{dataset_name}_{hashlib.md5(query.encode()).hexdigest()[:8]}" if query else dataset_name
            cache_path = CACHE_DIR / f"{cache_key}_insights.json"
            
            if cache_path.exists():
                with open(cache_path, 'r') as f:
                    cache_data = json.load(f)
                    return cache_data.get("insights")
            return None
        except Exception as e:
            st.error(f"Error retrieving cached insights: {e}")
            return None
    
    @staticmethod
    def save_visualization_config(config: Dict[str, Any], viz_name: str):
        """Save visualization configuration for offline use"""
        try:
            viz_path = VISUALIZATIONS_DIR / f"{viz_name}_config.json"
            config.update({
                "saved_at": pd.Timestamp.now().isoformat(),
                "viz_name": viz_name
            })
            
            with open(viz_path, 'w') as f:
                json.dump(config, f, indent=2)
                
            return str(viz_path)
        except Exception as e:
            st.error(f"Error saving visualization: {e}")
            return None
    
    @staticmethod
    def load_visualization_config(viz_name: str) -> Optional[Dict[str, Any]]:
        """Load visualization configuration"""
        try:
            viz_path = VISUALIZATIONS_DIR / f"{viz_name}_config.json"
            if viz_path.exists():
                with open(viz_path, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            st.error(f"Error loading visualization: {e}")
            return None
    
    @staticmethod
    def get_storage_stats() -> Dict[str, Any]:
        """Get statistics about local storage usage"""
        try:
            total_size = 0
            file_count = 0
            
            for dir_path in [CACHE_DIR, DATASETS_DIR, VISUALIZATIONS_DIR]:
                if dir_path.exists():
                    for file_path in dir_path.rglob("*"):
                        if file_path.is_file():
                            total_size += file_path.stat().st_size
                            file_count += 1
            
            return {
                "total_size_mb": round(total_size / (1024 * 1024), 2),
                "file_count": file_count,
                "datasets_count": len(list(DATASETS_DIR.glob("*.parquet"))),
                "cache_entries": len(list(CACHE_DIR.glob("*.json"))),
                "visualizations": len(list(VISUALIZATIONS_DIR.glob("*.json")))
            }
        except Exception as e:
            st.error(f"Error getting storage stats: {e}")
            return {"total_size_mb": 0, "file_count": 0, "datasets_count": 0, "cache_entries": 0, "visualizations": 0}
    
    @staticmethod
    def clear_cache():
        """Clear all cached data"""
        try:
            for cache_file in CACHE_DIR.glob("*"):
                cache_file.unlink()
            return True
        except Exception as e:
            st.error(f"Error clearing cache: {e}")
            return False
    
    @staticmethod
    def clear_all_local_storage():
        """Clear all local storage"""
        try:
            for dir_path in [CACHE_DIR, DATASETS_DIR, VISUALIZATIONS_DIR]:
                for file_path in dir_path.rglob("*"):
                    if file_path.is_file():
                        file_path.unlink()
            return True
        except Exception as e:
            st.error(f"Error clearing storage: {e}")
            return False

# PWA Service Worker for offline functionality
PWA_SERVICE_WORKER = """
const CACHE_NAME = 'plot-pyre-v1';
const urlsToCache = [
  '/',
  '/static/css/main.css',
  '/static/js/main.js',
  '/manifest.json',
  '/favicon.ico'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});
"""

def generate_pwa_manifest():
    """Generate PWA manifest.json"""
    manifest = {
        "name": "Plot Pyre - Python-Powered Data Visualization",
        "short_name": "Plot Pyre",
        "description": "AI-powered data visualization tool with Python backend",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#4B8BBE",
        "theme_color": "#FFD43B",
        "icons": [
            {
                "src": "/static/icons/icon-192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "/static/icons/icon-512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ]
    }
    return manifest
