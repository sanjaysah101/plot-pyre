# 🐍 Plot Pyre - Python-Powered Data Visualization Tool

**Plot Pyre** is an AI-powered data visualization tool built with Python, featuring an interactive web interface, educational platform, and offline-first capabilities. Built for the PyWeb Creators Hackathon 2025.

## 🚀 Features

### Core Features

- **📂 Multiple Data Sources**: Upload CSV/Excel files or import from MongoDB
- **🤖 AI-Powered Analysis**: Google GenAI integration for automated insights
- **📊 Dynamic Visualizations**: Line, bar, pie charts with interactive controls
- **🗄️ MongoDB Integration**: Vector search capabilities with embeddings
- **🔍 Semantic Search**: AI-powered data exploration

### Hackathon-Enhanced Features

- **🎨 Python-Themed UI**: Signature blue (#4B8BBE) and yellow (#FFD43B) color scheme
- **📱 PWA Support**: Offline-first capabilities with service worker
- **🎓 Educational Platform**: Interactive tutorials and guided workflows
- **🔄 Offline Storage**: Local dataset storage and caching
- **📈 Advanced Features**: Custom charts, AI insights, and collaborative tools

## 🧰 Project Setup and Running Instructions

### ✅ Prerequisites

- Python 3.12+
- MongoDB instance (local or cloud-hosted)
- Google Cloud Platform account with AI services enabled

### 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/sanjaysah101/plot-pyre
cd plot-pyre
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

### ⚙️ Configuration

Create a `.env` file in the project root with:

```env
MONGODB_URI="mongodb://localhost:27017/"
GOOGLE_CLOUD_API_KEY="your-gcp-api-key"
```

### ▶️ Running the Application

1. **Start the FastAPI backend:**

```bash
cd api
uvicorn main:app --host 0.0.0.0 --port 8000
```

2. **Start the Streamlit app:**

```bash
streamlit run main.py
```

3. **Open in browser:**
Visit [http://localhost:8501](http://localhost:8501)

## 🎯 Educational Features

### Learning Paths

- **Beginner**: Data Visualization Fundamentals (30 min)
- **Intermediate**: Advanced Visualization Techniques (45 min)
- **Advanced**: Data Science Mastery (60 min)

### Interactive Tutorials

- Upload your first dataset
- Create your first chart
- AI-powered analysis
- Custom visualizations

## 🎨 Python-Themed UI

The application features Python's signature color scheme:

- **Primary Blue**: #4B8BBE
- **Accent Yellow**: #FFD43B
- **Dark Blue**: #306998
- **Light Blue**: #E6F3FF

## 📱 PWA Features

- **Offline Storage**: Local dataset storage and caching
- **Service Worker**: Offline-first capabilities
- **Progressive Web App**: Installable on mobile devices
- **Responsive Design**: Works on all screen sizes

## 🗄️ Database Schema

### MongoDB Collections

- `datasets`: Dataset storage with vector search
- `embeddings`: AI-generated embeddings
- `insights`: AI-powered insights

## 📊 Usage Examples

### Upload Data

```python
# Upload CSV file
import pandas as pd
df = pd.read_csv('data.csv')

# Store in MongoDB
from src.db_utils import store_dataset
store_dataset("my_dataset", df)
```

### Create Visualization

```python
# Create a line chart
import matplotlib.pyplot as plt
plt.plot(df['x'], df['y'])
plt.show()
```

### AI Insights

```python
from src.ai_utils import get_data_insights
insights = get_data_insights(df, question="What are the key trends?")
```

## 🎓 Educational Platform

### Learning Paths

- **Beginner**: 30 minutes
- **Intermediate**: 45 minutes
- **Advanced**: 60 minutes

### Tutorials

- Upload your first dataset
- Create your first chart
- AI-powered analysis
- Custom visualizations

## 🔄 Offline Storage

### Local Storage

- Datasets: `~/.plot_pyre/local_storage/datasets/`
- Cache: `~/.plot_pyre/local_storage/cache/`
- Visualizations: `~/.plot_pyre/local_storage/visualizations/`

### Caching

- AI insights caching
- Dataset caching
- Visualization caching

## 🚀 Advanced Features

### Backend API

- RESTful endpoints for dataset management
- AI processing endpoints
- Offline storage endpoints
- Educational platform endpoints

### Frontend Features

- Interactive charts
- AI insights
- Educational tutorials
- Collaborative features

## 📈 Usage Examples

### Upload Data

```python
# Upload CSV file
import pandas as pd
df = pd.read_csv('data.csv')

# Store in MongoDB
from src.db_utils import store_dataset
store_dataset("my_dataset", df)
```

### Create Visualization

```python
# Create a line chart
import matplotlib.pyplot as plt
plt.plot(df['x'], df['y'])
plt.show()
```

### AI Insights

```python
from src.ai_utils import get_data_insights
insights = get_data_insights(df, question="What are the key trends?")
```

## 🎓 Educational Platform

### Learning Paths

- **Beginner**: 30 minutes
- **Intermediate**: 45 minutes
- **Advanced**: 60 minutes

### Tutorials

- Upload your first dataset
- Create your first chart
- AI-powered analysis
- Custom visualizations

## 🔄 Offline Storage

### Local Storage

- Datasets: `~/.plot_pyre/local_storage/datasets/`
- Cache: `~/.plot_pyre/local_storage/cache/`
- Visualizations: `~/.plot_pyre/local_storage/visualizations/`

### Caching

- AI insights caching
- Dataset caching
- Visualization caching

## 🎓 Educational Platform

### Learning Paths

- **Beginner**: 30 minutes
- **Intermediate**: 45 minutes
- **Advanced**: 60 minutes

### Tutorials

- Upload your first dataset
- Create your first chart
- AI-powered analysis
- Custom visualizations

## 🔄 Offline Storage

### Local Storage

- Datasets: `~/.plot_pyre/local_storage/datasets/`
- Cache: `~/.plot_pyre/local_storage/cache/`
- Visualizations: `~/.plot_pyre/local_storage/visualizations/`

### Caching

- AI insights caching
- Dataset caching
- Visualization caching

## 🎓 Educational Platform

### Learning Paths

- **Beginner**: 30 minutes
- **Intermediate**: 45 minutes
- **Advanced**: 60 minutes

### Tutorials

- Upload your first dataset
- Create your first chart
- AI-powered analysis
- Custom visualizations

## 🔄 Offline Storage

### Local Storage

- Datasets: `~/.plot_pyre/local_storage/datasets/`
- Cache: `~/.plot_pyre/local_storage/cache/`
- Visualizations: `~/.plot_pyre/local_storage/visualizations/`

### Caching

- AI insights caching
- Dataset caching
- Visualization caching

## 🎓 Educational Platform

### Learning Paths

- **Beginner**: 30 minutes
- **Intermediate**: 45 minutes
- **Advanced**: 60 minutes

### Tutorials

- Upload your first dataset
- Create your first chart
- AI-powered analysis
- Custom visualizations

## 🔄 Offline Storage

### Local Storage

- Datasets: `~/.plot_pyre/local_storage/datasets/`
- Cache: `~/.plot_pyre/local_storage/cache/`
- Visualizations: `~/.plot_pyre/local_storage/visualizations/`

### Caching

- AI insights caching
- Dataset caching
- Visualization caching

## 🎓 Educational Platform

### Learning Paths

- **Beginner**: 30 minutes
- **Intermediate**: 45 minutes
- **Advanced**: 60 minutes

### Tutorials

- Upload your first dataset
- Create your first chart
- AI-powered analysis
- Custom visualizations

## 🔄 Offline Storage

### Local Storage

- Datasets: `~/.plot_pyre/local_storage/datasets/`
- Cache: `~/.plot_pyre/local_storage/cache/`
- Visualizations: `~/.plot_pyre/local_storage/visualizations/`

### Caching

- AI insights caching
- Dataset caching
- Visualization caching

## 🎓 Educational Platform

### Learning Paths

- **Beginner**: 30 minutes
- **Intermediate**: 45 minutes
- **Advanced**: 60 minutes

### Tutorials

- Upload your first dataset
- Create your first chart
- AI-powered analysis
- Custom visualizations

## 🔄 Offline Storage

### Local Storage

- Datasets: `~/.plot_pyre/local_storage/datasets/`
- Cache: `~/.plot_pyre/local_storage/cache/`
- Visualizations: `~/.plot_pyre/local_storage/visualizations/`

### Caching

- AI insights caching
- Dataset caching
- Visualization caching

## 🎓 Educational Platform

### Learning Paths

- **Beginner**: 30 minutes
- **Intermediate**: 45 minutes
- **Advanced**: 60 minutes

### Tutorials

- Upload your first dataset
- Create your first chart
- AI-powered analysis
- Custom visualizations

## 🔄 Offline Storage

### Local Storage

- Datasets: `~/.plot_pyre/local_storage/datasets/`
- Cache: `~/.plot_pyre/local_storage/cache/`
- Visualizations: `~/.plot_pyre/local_storage/visualizations/`

### Caching

- AI insights caching
- Dataset caching
- Visualization caching

## 🎓 Educational Platform

### Learning Paths

- **Beginner**: 30 minutes
- **Intermediate**: 45 minutes
- **Advanced**: 60 minutes

### Tutorials

- Upload your first dataset
- Create your first chart
- AI-powered analysis
- Custom visualizations

## 🔄 Offline Storage

### Local Storage

- Datasets: `~/.plot_pyre/local_storage/datasets/`
- Cache: `~/.plot_pyre/local_storage/cache/`
- Visualizations: `~
