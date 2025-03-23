import streamlit as st
import pandas as pd
from utils.visitor_counter import display_visitor_counter

# Page configuration
st.set_page_config(
    page_title="Projects - Chiranjib Koch",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for navigation (included on all pages)
with st.sidebar:
    st.title("Navigation")
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/skills.py", label="Skills & Expertise", icon="📊")
    st.page_link("pages/projects.py", label="Projects", icon="💻")
    st.page_link("pages/blog.py", label="Tech Blog", icon="📝")
    st.page_link("pages/contact.py", label="Contact", icon="📧")
    
    st.divider()
    st.caption("© 2023 Chiranjib Koch")

# Main content
st.title("Projects Portfolio")
st.markdown("""
This page showcases a selection of my professional projects across various domains.
Use the filters to find specific types of projects.
""")

# Project data
projects = [
    {
        "title": "AI-Powered Recommendation System",
        "description": "Developed a recommendation engine using collaborative filtering and deep learning techniques. The system analyzes user behavior and preferences to provide personalized product recommendations with high accuracy.",
        "tech": ["Python", "TensorFlow", "MongoDB", "Flask"],
        "category": "AI/ML",
        "image": "🤖"
    },
    {
        "title": "Advanced Telegram Bot Framework",
        "description": "Created a robust framework for developing and deploying Telegram bots with advanced functionalities including natural language processing, automated responses, and integration with external services.",
        "tech": ["Python", "Telegram API", "MongoDB", "Docker"],
        "category": "Telegram",
        "image": "📱"
    },
    {
        "title": "Predictive Analytics Dashboard",
        "description": "Built an interactive dashboard for visualizing ML predictions and business insights. Features include data visualization, trend analysis, and customizable reporting capabilities.",
        "tech": ["Python", "Streamlit", "Pandas", "Scikit-learn"],
        "category": "Data Visualization",
        "image": "📊"
    },
    {
        "title": "Automated Document Processing System",
        "description": "Implemented an end-to-end solution for document processing using OCR and NLP techniques. The system automatically extracts, classifies, and routes information from various document types.",
        "tech": ["Python", "PyTorch", "MongoDB", "FastAPI"],
        "category": "AI/ML",
        "image": "📄"
    },
    {
        "title": "E-commerce Telegram Bot",
        "description": "Designed and built a Telegram bot that allows users to browse products, place orders, and track shipments directly from Telegram. Features include secure payment integration and personalized notifications.",
        "tech": ["Python", "Telegram API", "MongoDB", "Payment Gateway API"],
        "category": "Telegram",
        "image": "🛒"
    },
    {
        "title": "Time Series Forecasting Tool",
        "description": "Developed a tool for forecasting time series data using advanced statistical and machine learning methods. Applied to sales prediction, inventory management, and resource planning.",
        "tech": ["Python", "TensorFlow", "Pandas", "Plotly"],
        "category": "AI/ML",
        "image": "📈"
    },
    {
        "title": "NoSQL Database Migration Framework",
        "description": "Created a framework to facilitate data migration from relational databases to MongoDB with schema validation, data transformation, and integrity verification.",
        "tech": ["Python", "MongoDB", "SQL", "ETL"],
        "category": "Database",
        "image": "🗄️"
    },
    {
        "title": "Telegram Customer Support Bot",
        "description": "Built a Telegram bot that handles customer inquiries, routes complex issues to human agents, and provides automated responses for common questions.",
        "tech": ["Python", "Telegram API", "NLP", "Redis"],
        "category": "Telegram",
        "image": "🎭"
    },
    {
        "title": "AI-based Image Recognition Service",
        "description": "Developed a web service that uses deep learning models to recognize and classify objects in images with high accuracy.",
        "tech": ["Python", "PyTorch", "Flask", "Docker"],
        "category": "AI/ML",
        "image": "🖼️"
    },
    {
        "title": "MongoDB Performance Optimization Suite",
        "description": "Created a suite of tools to analyze and optimize MongoDB database performance, including index recommendation, query optimization, and schema design validation.",
        "tech": ["Python", "MongoDB", "Prometheus", "Grafana"],
        "category": "Database",
        "image": "⚡"
    }
]

# Filters
st.markdown("### Filter Projects")
col1, col2 = st.columns(2)

with col1:
    categories = sorted(list(set([p["category"] for p in projects])))
    selected_categories = st.multiselect("Categories", categories, default=categories)

with col2:
    technologies = sorted(list(set([tech for p in projects for tech in p["tech"]])))
    selected_technologies = st.multiselect("Technologies", technologies)

# Filter projects based on selection
filtered_projects = projects
if selected_categories:
    filtered_projects = [p for p in filtered_projects if p["category"] in selected_categories]
if selected_technologies:
    filtered_projects = [p for p in filtered_projects if any(tech in p["tech"] for tech in selected_technologies)]

# Display projects
if filtered_projects:
    st.markdown("## Project List")
    
    for i in range(0, len(filtered_projects), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            if i < len(filtered_projects):
                project = filtered_projects[i]
                with st.container(border=True):
                    st.markdown(f"### {project['image']} {project['title']}")
                    st.markdown(f"**Category:** {project['category']}")
                    st.markdown(project['description'])
                    st.markdown(f"**Technologies:** {', '.join(project['tech'])}")
        
        with col2:
            if i + 1 < len(filtered_projects):
                project = filtered_projects[i + 1]
                with st.container(border=True):
                    st.markdown(f"### {project['image']} {project['title']}")
                    st.markdown(f"**Category:** {project['category']}")
                    st.markdown(project['description'])
                    st.markdown(f"**Technologies:** {', '.join(project['tech'])}")
else:
    st.info("No projects match the selected filters. Please adjust your criteria.")

# Display visitor counter at the bottom
display_visitor_counter()
