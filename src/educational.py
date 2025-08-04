"""
Educational platform features for Plot Pyre
Interactive tutorials, guided workflows, and learning paths
"""
import json
from typing import Dict, List, Any, Optional
import streamlit as st
import pandas as pd

class EducationalContent:
    """Handles educational tutorials and guided workflows"""
    
    # Pre-defined learning paths
    LEARNING_PATHS = {
        "beginner": {
            "title": "Data Visualization Fundamentals",
            "description": "Learn the basics of data visualization with Python",
            "duration": "30 minutes",
            "lessons": [
                {
                    "id": "intro",
                    "title": "Introduction to Data Visualization",
                    "content": "Learn why data visualization is important and how Python can help",
                    "exercises": ["Upload your first dataset", "Create a simple chart"]
                },
                {
                    "id": "data_types",
                    "title": "Understanding Data Types",
                    "content": "Learn about different data types and their visualization methods",
                    "exercises": ["Identify data types in your dataset", "Choose appropriate charts"]
                },
                {
                    "id": "basic_charts",
                    "title": "Creating Basic Charts",
                    "content": "Learn to create line, bar, and pie charts",
                    "exercises": ["Create a line chart", "Create a bar chart", "Create a pie chart"]
                }
            ]
        },
        "intermediate": {
            "title": "Advanced Visualization Techniques",
            "description": "Master advanced visualization concepts and techniques",
            "duration": "45 minutes",
            "lessons": [
                {
                    "id": "multi_dim",
                    "title": "Multi-dimensional Data Visualization",
                    "content": "Learn to visualize complex, multi-dimensional datasets",
                    "exercises": ["Create scatter plots", "Use color and size encoding"]
                },
                {
                    "id": "interactive",
                    "title": "Interactive Visualizations",
                    "content": "Create interactive charts with Streamlit",
                    "exercises": ["Add filters", "Create hover effects", "Implement zoom"]
                },
                {
                    "id": "ai_insights",
                    "title": "AI-Powered Analysis",
                    "content": "Use AI to generate insights from your data",
                    "exercises": ["Generate AI insights", "Interpret AI recommendations"]
                }
            ]
        },
        "advanced": {
            "title": "Data Science Mastery",
            "description": "Become a data visualization expert",
            "duration": "60 minutes",
            "lessons": [
                {
                    "id": "custom_charts",
                    "title": "Custom Chart Creation",
                    "content": "Create custom visualizations beyond standard charts",
                    "exercises": ["Create custom plots", "Use advanced libraries"]
                },
                {
                    "id": "storytelling",
                    "title": "Data Storytelling",
                    "content": "Tell compelling stories with your data",
                    "exercises": ["Create a data story", "Design a dashboard"]
                },
                {
                    "id": "collaboration",
                    "title": "Collaborative Analysis",
                    "content": "Share and collaborate on data analysis",
                    "exercises": ["Share visualizations", "Collaborate on datasets"]
                }
            ]
        }
    }
    
    # Interactive tutorials
    TUTORIALS = {
        "upload_data": {
            "title": "Upload Your First Dataset",
            "steps": [
                {
                    "instruction": "Click on 'Upload File' in the sidebar",
                    "description": "Choose CSV or Excel file from your computer",
                    "expected_action": "File upload widget appears"
                },
                {
                    "instruction": "Select your file and click 'Upload'",
                    "description": "The file will be processed and loaded into the app",
                    "expected_action": "Dataset preview appears"
                },
                {
                    "instruction": "Review the dataset preview",
                    "description": "Check if your data looks correct",
                    "expected_action": "You can see your data in a table"
                }
            ]
        },
        "create_chart": {
            "title": "Create Your First Chart",
            "steps": [
                {
                    "instruction": "Select columns for X and Y axes",
                    "description": "Choose which data to visualize",
                    "expected_action": "Column selection widgets appear"
                },
                {
                    "instruction": "Choose chart type",
                    "description": "Select from line, bar, or pie chart",
                    "expected_action": "Chart type selector appears"
                },
                {
                    "instruction": "Click 'Generate Chart'",
                    "description": "Your chart will be created and displayed",
                    "expected_action": "Interactive chart appears"
                }
            ]
        },
        "ai_insights": {
            "title": "Get AI-Powered Insights",
            "steps": [
                {
                    "instruction": "Click 'Generate Insights' button",
                    "description": "AI will analyze your data",
                    "expected_action": "AI processing starts"
                },
                {
                    "instruction": "Wait for AI to complete analysis",
                    "description": "This may take a few seconds",
                    "expected_action": "Insights appear"
                },
                {
                    "instruction": "Read and interpret the insights",
                    "description": "Understand what the AI found in your data",
                    "expected_action": "You can use insights for decisions"
                }
            ]
        }
    }
    
    # Code snippets for common tasks
    CODE_SNIPPETS = {
        "basic_plot": {
            "title": "Basic Plot with Matplotlib",
            "description": "Create a simple line plot",
            "code": """
import matplotlib.pyplot as plt
import pandas as pd

# Assuming df is your DataFrame
plt.figure(figsize=(10, 6))
plt.plot(df['x_column'], df['y_column'])
plt.title('Your Chart Title')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.show()
            """,
            "tags": ["matplotlib", "basic", "line"]
        },
        "interactive_plot": {
            "title": "Interactive Plot with Streamlit",
            "description": "Create an interactive plot in Streamlit",
            "code": """
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# In your Streamlit app
st.title('Interactive Plot')
chart_type = st.selectbox('Chart Type', ['Line', 'Bar', 'Pie'])

if chart_type == 'Line':
    fig, ax = plt.subplots()
    ax.plot(df['x'], df['y'])
    st.pyplot(fig)
            """,
            "tags": ["streamlit", "interactive", "web"]
        },
        "ai_analysis": {
            "title": "AI-Powered Analysis",
            "description": "Use AI to analyze your data",
            "code": """
from src.ai_utils import get_data_insights

# Get AI insights
insights = get_data_insights(df, question="What are the key trends?")
print(insights)
            """,
            "tags": ["ai", "analysis", "insights"]
        }
    }
    
    @staticmethod
    def get_learning_path(path_id: str) -> Dict[str, Any]:
        """Get a specific learning path"""
        return EducationalContent.LEARNING_PATHS.get(path_id, {})
    
    @staticmethod
    def get_all_learning_paths() -> Dict[str, Dict[str, Any]]:
        """Get all available learning paths"""
        return EducationalContent.LEARNING_PATHS
    
    @staticmethod
    def get_tutorial(tutorial_id: str) -> Dict[str, Any]:
        """Get a specific tutorial"""
        return EducationalContent.TUTORIALS.get(tutorial_id, {})
    
    @staticmethod
    def get_all_tutorials() -> Dict[str, Dict[str, Any]]:
        """Get all available tutorials"""
        return EducationalContent.TUTORIALS
    
    @staticmethod
    def get_code_snippet(snippet_id: str) -> Dict[str, Any]:
        """Get a specific code snippet"""
        return EducationalContent.CODE_SNIPPETS.get(snippet_id, {})
    
    @staticmethod
    def search_code_snippets(tags: List[str]) -> List[Dict[str, Any]]:
        """Search code snippets by tags"""
        results = []
        for snippet_id, snippet in EducationalContent.CODE_SNIPPETS.items():
            if any(tag in snippet.get("tags", []) for tag in tags):
                results.append(snippet)
        return results
    
    @staticmethod
    def create_progress_tracker(user_id: str = "default") -> Dict[str, Any]:
        """Create a progress tracker for a user"""
        return {
            "user_id": user_id,
            "current_path": None,
            "completed_lessons": [],
            "total_points": 0,
            "achievements": [],
            "last_activity": pd.Timestamp.now().isoformat()
        }
    
    @staticmethod
    def update_progress(user_id: str, lesson_id: str, points: int = 10):
        """Update user progress"""
        # This would typically be stored in a database
        # For now, we'll use session state
        if "user_progress" not in st.session_state:
            st.session_state.user_progress = EducationalContent.create_progress_tracker(user_id)
        
        progress = st.session_state.user_progress
        
        if lesson_id not in progress["completed_lessons"]:
            progress["completed_lessons"].append(lesson_id)
            progress["total_points"] += points
            progress["last_activity"] = pd.Timestamp.now().isoformat()
            
            # Check for achievements
            if len(progress["completed_lessons"]) >= 5:
                if "First 5 Lessons" not in progress["achievements"]:
                    progress["achievements"].append("First 5 Lessons")
            
            if progress["total_points"] >= 100:
                if "Data Explorer" not in progress["achievements"]:
                    progress["achievements"].append("Data Explorer")
        
        return progress
    
    @staticmethod
    def get_recommendations(user_progress: Dict[str, Any]) -> List[str]:
        """Get personalized recommendations based on user progress"""
        recommendations = []
        
        completed = set(user_progress.get("completed_lessons", []))
        
        # Recommend next lessons based on completed ones
        if "intro" in completed and "data_types" not in completed:
            recommendations.append("Learn about data types and their visualization")
        
        if "basic_charts" in completed and "multi_dim" not in completed:
            recommendations.append("Explore multi-dimensional data visualization")
        
        if "ai_insights" not in completed:
            recommendations.append("Try AI-powered data analysis")
        
        return recommendations
    
    @staticmethod
    def generate_learning_report(user_progress: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a comprehensive learning report"""
        report = {
            "user_id": user_progress.get("user_id", "unknown"),
            "total_lessons_completed": len(user_progress.get("completed_lessons", [])),
            "total_points": user_progress.get("total_points", 0),
            "achievements": user_progress.get("achievements", []),
            "learning_path": user_progress.get("current_path", "Not started"),
            "recommendations": EducationalContent.get_recommendations(user_progress),
            "report_generated_at": pd.Timestamp.now().isoformat()
        }
        
        return report
    
    @staticmethod
    def create_interactive_tutorial(tutorial_id: str, step: int = 0):
        """Create an interactive tutorial experience"""
        tutorial = EducationalContent.get_tutorial(tutorial_id)
        if not tutorial:
            return None
        
        steps = tutorial.get("steps", [])
        if step >= len(steps):
            return {"completed": True, "message": "Tutorial completed!"}
        
        current_step = steps[step]
        
        return {
            "tutorial_id": tutorial_id,
            "title": tutorial.get("title"),
            "current_step": step + 1,
            "total_steps": len(steps),
            "instruction": current_step.get("instruction"),
            "description": current_step.get("description"),
            "expected_action": current_step.get("expected_action"),
            "next_step": step + 1 if step + 1 < len(steps) else None
        }
    
    @staticmethod
    def render_learning_dashboard():
        """Render the educational dashboard"""
        st.title("📚 Learning Dashboard")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Lessons Completed", len(st.session_state.get("user_progress", {}).get("completed_lessons", [])))
        
        with col2:
            st.metric("Total Points", st.session_state.get("user_progress", {}).get("total_points", 0))
        
        with col3:
            st.metric("Achievements", len(st.session_state.get("user_progress", {}).get("achievements", [])))
        
        # Learning paths
        st.subheader("🎯 Learning Paths")
        for path_id, path_data in EducationalContent.get_all_learning_paths().items():
            with st.expander(f"{path_data['title']} - {path_data['duration']}"):
                st.write(path_data['description'])
                st.write("**Lessons:**")
                for lesson in path_data['lessons']:
                    st.write(f"- {lesson['title']}: {lesson['content']}")
        
        # Recommendations
        recommendations = EducationalContent.get_recommendations(
            st.session_state.get("user_progress", {})
        )
        if recommendations:
            st.subheader("🎯 Recommendations")
            for rec in recommendations:
                st.info(f"💡 {rec}")
        
        # Tutorials
        st.subheader("📖 Interactive Tutorials")
        for tutorial_id, tutorial_data in EducationalContent.get_all_tutorials().items():
            if st.button(f"Start: {tutorial_data['title']}", key=f"tutorial_{tutorial_id}"):
                # This would launch the tutorial
                st.session_state.current_tutorial = tutorial_id
                st.session_state.tutorial_step = 0
                st.rerun()
    
    @staticmethod
    def render_code_snippets():
        """Render code snippets section"""
        st.subheader("💻 Code Snippets")
        
        # Filter by tags
        tags = st.multiselect(
            "Filter by tags:",
            ["matplotlib", "streamlit", "interactive", "ai", "basic", "advanced"],
            key="snippet_tags"
        )
        
        if tags:
            snippets = EducationalContent.search_code_snippets(tags)
        else:
            snippets = list(EducationalContent.CODE_SNIPPETS.values())
        
        for snippet in snippets:
            with st.expander(f"{snippet['title']}"):
                st.write(snippet['description'])
                st.code(snippet['code'], language='python')
                st.write("**Tags:**", ", ".join(snippet.get('tags', [])))
