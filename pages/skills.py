import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
from utils.visitor_counter import display_visitor_counter

# Page configuration
st.set_page_config(
    page_title="Skills & Expertise - Chiranjib Koch",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for navigation
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
st.title("Skills & Expertise")
st.markdown("""
This page provides an overview of my technical skills, expertise areas, and professional experience.
Explore the visualizations to understand my proficiency in various technologies and domains.
""")

# Technical Skills Data
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

# Convert to DataFrame
df_skills = pd.DataFrame(tech_skills)

# Domain expertise
domain_expertise = [
    {"domain": "Machine Learning", "years": 5, "projects": 15},
    {"domain": "Deep Learning", "years": 4, "projects": 12},
    {"domain": "Natural Language Processing", "years": 4, "projects": 10},
    {"domain": "Computer Vision", "years": 3, "projects": 8},
    {"domain": "Database Management", "years": 6, "projects": 18},
    {"domain": "Telegram Bot Development", "years": 5, "projects": 20},
]

# Convert to DataFrame
df_domains = pd.DataFrame(domain_expertise)

# Experience timeline
experience = [
    {"role": "Senior AI Developer", "company": "TechInnovate", "period": "2020-Present"},
    {"role": "ML Engineer", "company": "DataSolutions Inc.", "period": "2018-2020"},
    {"role": "Python Developer", "company": "WebTech Systems", "period": "2015-2018"},
]

# Tabs for different skill visualizations
tab1, tab2, tab3 = st.tabs(["Technical Skills", "Domain Expertise", "Experience"])

with tab1:
    st.markdown("### Technical Skills Overview")
    st.markdown("Below is a comprehensive overview of my technical skills across various categories.")
    
    # Filter options
    skill_categories = sorted(df_skills["category"].unique())
    selected_categories = st.multiselect("Filter by category", skill_categories, default=skill_categories)
    
    # Filter data
    filtered_skills = df_skills[df_skills["category"].isin(selected_categories)]
    
    if not filtered_skills.empty:
        # Create horizontal bar chart with Plotly
        fig = px.bar(
            filtered_skills,
            x="proficiency",
            y="skill",
            color="category",
            orientation="h",
            height=600,
            labels={"proficiency": "Proficiency Level", "skill": "Skill"},
            title="Technical Skills Proficiency",
            hover_data=["category"],
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        
        fig.update_layout(
            yaxis={"categoryorder": "total ascending"},
            legend_title="Category",
            margin=dict(l=0, r=0, t=30, b=0),
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Please select at least one category to display skills.")

with tab2:
    st.markdown("### Domain Expertise")
    st.markdown("My years of experience and number of projects completed in various domains.")
    
    # Create two columnar visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        # Years of experience visualization
        years_chart = alt.Chart(df_domains).mark_bar().encode(
            x=alt.X('years:Q', title='Years of Experience'),
            y=alt.Y('domain:N', title=None, sort='-x'),
            color=alt.Color('years:Q', scale=alt.Scale(scheme='blues'), legend=None),
            tooltip=['domain', 'years']
        ).properties(
            title='Experience by Domain (Years)',
            height=300
        )
        
        st.altair_chart(years_chart, use_container_width=True)
    
    with col2:
        # Projects completed visualization
        projects_chart = alt.Chart(df_domains).mark_bar().encode(
            x=alt.X('projects:Q', title='Number of Projects'),
            y=alt.Y('domain:N', title=None, sort='-x'),
            color=alt.Color('projects:Q', scale=alt.Scale(scheme='greens'), legend=None),
            tooltip=['domain', 'projects']
        ).properties(
            title='Projects Completed by Domain',
            height=300
        )
        
        st.altair_chart(projects_chart, use_container_width=True)
    
    # Radar chart for overall expertise
    st.markdown("### Overall Expertise Radar")
    
    # Normalize years and projects to scale 0-10 for radar chart
    df_radar = df_domains.copy()
    df_radar['years_norm'] = df_radar['years'] / df_radar['years'].max() * 10
    df_radar['projects_norm'] = df_radar['projects'] / df_radar['projects'].max() * 10
    
    # Calculate an overall expertise score
    df_radar['expertise_score'] = (df_radar['years_norm'] * 0.6) + (df_radar['projects_norm'] * 0.4)
    
    # Create radar chart with Plotly
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=df_radar['expertise_score'],
        theta=df_radar['domain'],
        fill='toself',
        line=dict(color='rgb(67, 147, 195)'),
        fillcolor='rgba(67, 147, 195, 0.2)',
        name='Expertise Score'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        title="Overall Expertise Radar",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown("### Professional Experience")
    st.markdown("Timeline of my professional career and expertise development.")
    
    # Display experience as a timeline
    for exp in experience:
        st.markdown(f"### {exp['role']} | {exp['company']}")
        st.markdown(f"**Period:** {exp['period']}")
        
        if exp['role'] == "Senior AI Developer":
            st.markdown("""
            • Led AI and ML initiatives for enterprise clients across multiple industries
            • Designed and implemented advanced recommendation systems and prediction models
            • Developed custom NLP solutions for automated document processing
            • Mentored junior developers and coordinated cross-functional teams
            • Integrated ML models with existing business systems
            """)
        
        elif exp['role'] == "ML Engineer":
            st.markdown("""
            • Built and deployed machine learning models for business intelligence applications
            • Created data pipelines for processing and transforming large datasets
            • Developed MongoDB schemas and query optimization strategies
            • Implemented automated testing frameworks for ML model validation
            • Collaborated with data scientists to productionize research prototypes
            """)
        
        elif exp['role'] == "Python Developer":
            st.markdown("""
            • Developed web applications and APIs using Python frameworks
            • Created initial versions of Telegram bots for business automation
            • Implemented database solutions with both SQL and NoSQL technologies
            • Built data visualization dashboards for business analytics
            • Contributed to open source Python libraries and tools
            """)
        
        st.divider()

# Display visitor counter at the bottom
display_visitor_counter()
