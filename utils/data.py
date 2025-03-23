import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Project data structure
def get_projects_data():
    """
    Returns structured data for projects portfolio
    """
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
    
    return projects

# Skills data structure
def get_skills_data():
    """
    Returns structured data for skills visualization
    """
    tech_skills = [
        {"category": "Programming Languages", "skill": "Python", "proficiency": 95},
        {"category": "Programming Languages", "skill": "JavaScript", "proficiency": 80},
        {"category": "Programming Languages", "skill": "SQL", "proficiency": 85},
        {"category": "AI/ML", "skill": "TensorFlow", "proficiency": 90},
        {"category": "AI/ML", "skill": "PyTorch", "proficiency": 85},
        {"category": "AI/ML", "skill": "Scikit-learn", "proficiency": 95},
        {"category": "AI/ML", "skill": "NLP", "proficiency": 90},
        {"category": "AI/ML", "skill": "Computer Vision", "proficiency": 85},
        {"category": "Data Handling", "skill": "Pandas", "proficiency": 95},
        {"category": "Data Handling", "skill": "NumPy", "proficiency": 90},
        {"category": "Data Handling", "skill": "MongoDB", "proficiency": 95},
        {"category": "Data Handling", "skill": "PostgreSQL", "proficiency": 85},
        {"category": "Development", "skill": "Flask", "proficiency": 90},
        {"category": "Development", "skill": "FastAPI", "proficiency": 85},
        {"category": "Development", "skill": "Streamlit", "proficiency": 95},
        {"category": "Development", "skill": "Telegram Bot API", "proficiency": 95},
        {"category": "DevOps", "skill": "Docker", "proficiency": 85},
        {"category": "DevOps", "skill": "Git", "proficiency": 90},
        {"category": "DevOps", "skill": "CI/CD", "proficiency": 80},
    ]
    
    return tech_skills

# Domain expertise data
def get_domain_expertise():
    """
    Returns structured data for domain expertise
    """
    domain_expertise = [
        {"domain": "Machine Learning", "years": 5, "projects": 15},
        {"domain": "Deep Learning", "years": 4, "projects": 12},
        {"domain": "Natural Language Processing", "years": 4, "projects": 10},
        {"domain": "Computer Vision", "years": 3, "projects": 8},
        {"domain": "Database Management", "years": 6, "projects": 18},
        {"domain": "Telegram Bot Development", "years": 5, "projects": 20},
    ]
    
    return domain_expertise

# Blog post data
def get_blog_posts():
    """
    Returns structured data for blog posts
    """
    blog_posts = [
        {
            "title": "Building Effective Recommendation Systems with TensorFlow",
            "date": "2023-10-15",
            "category": "AI/ML",
            "tags": ["TensorFlow", "Recommendation Systems", "Deep Learning"],
            "content": "Full blog post content goes here..."
        },
        {
            "title": "Advanced MongoDB Aggregation Pipelines for Data Analysis",
            "date": "2023-09-22",
            "category": "Database",
            "tags": ["MongoDB", "Data Analysis", "Aggregation Framework"],
            "content": "Full blog post content goes here..."
        },
        {
            "title": "Creating Interactive Telegram Bots with Python",
            "date": "2023-08-10",
            "category": "Telegram",
            "tags": ["Python", "Telegram", "Bot Development"],
            "content": "Full blog post content goes here..."
        },
        {
            "title": "Optimizing Python Performance for Data Processing",
            "date": "2023-07-05",
            "category": "Python",
            "tags": ["Python", "Performance", "Optimization"],
            "content": "Full blog post content goes here..."
        }
    ]
    
    return blog_posts

# Generate synthetic experience data for timeline visualization
def generate_experience_timeline():
    """
    Returns structured data for experience timeline
    """
    experience = [
        {
            "role": "Senior AI Developer",
            "company": "TechInnovate",
            "period": "2020-Present",
            "description": [
                "Led AI and ML initiatives for enterprise clients across multiple industries",
                "Designed and implemented advanced recommendation systems and prediction models",
                "Developed custom NLP solutions for automated document processing",
                "Mentored junior developers and coordinated cross-functional teams",
                "Integrated ML models with existing business systems"
            ]
        },
        {
            "role": "ML Engineer",
            "company": "DataSolutions Inc.",
            "period": "2018-2020",
            "description": [
                "Built and deployed machine learning models for business intelligence applications",
                "Created data pipelines for processing and transforming large datasets",
                "Developed MongoDB schemas and query optimization strategies",
                "Implemented automated testing frameworks for ML model validation",
                "Collaborated with data scientists to productionize research prototypes"
            ]
        },
        {
            "role": "Python Developer",
            "company": "WebTech Systems",
            "period": "2015-2018",
            "description": [
                "Developed web applications and APIs using Python frameworks",
                "Created initial versions of Telegram bots for business automation",
                "Implemented database solutions with both SQL and NoSQL technologies",
                "Built data visualization dashboards for business analytics",
                "Contributed to open source Python libraries and tools"
            ]
        }
    ]
    
    return experience
