import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

def create_skills_bar_chart(skills_data):
    """
    Creates a horizontal bar chart for skills visualization
    
    Parameters:
    -----------
    skills_data : list of dicts
        List containing skill data with category, skill name and proficiency level
    
    Returns:
    --------
    plotly.graph_objects.Figure
        A plotly figure object for the horizontal bar chart
    """
    df = pd.DataFrame(skills_data)
    
    fig = px.bar(
        df,
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
    
    return fig

def create_domain_expertise_charts(domain_data):
    """
    Creates charts for visualizing domain expertise
    
    Parameters:
    -----------
    domain_data : list of dicts
        List containing domain expertise data with domain, years and projects count
    
    Returns:
    --------
    tuple
        A tuple containing Altair chart objects for years and projects visualizations
    """
    df = pd.DataFrame(domain_data)
    
    # Years chart
    years_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('years:Q', title='Years of Experience'),
        y=alt.Y('domain:N', title=None, sort='-x'),
        color=alt.Color('years:Q', scale=alt.Scale(scheme='blues'), legend=None),
        tooltip=['domain', 'years']
    ).properties(
        title='Experience by Domain (Years)',
        height=300
    )
    
    # Projects chart
    projects_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('projects:Q', title='Number of Projects'),
        y=alt.Y('domain:N', title=None, sort='-x'),
        color=alt.Color('projects:Q', scale=alt.Scale(scheme='greens'), legend=None),
        tooltip=['domain', 'projects']
    ).properties(
        title='Projects Completed by Domain',
        height=300
    )
    
    return years_chart, projects_chart

def create_expertise_radar(domain_data):
    """
    Creates a radar chart for overall expertise visualization
    
    Parameters:
    -----------
    domain_data : list of dicts
        List containing domain expertise data with domain, years and projects count
    
    Returns:
    --------
    plotly.graph_objects.Figure
        A plotly figure object for the radar chart
    """
    df = pd.DataFrame(domain_data)
    
    # Normalize years and projects to scale 0-10
    df['years_norm'] = df['years'] / df['years'].max() * 10
    df['projects_norm'] = df['projects'] / df['projects'].max() * 10
    
    # Calculate overall expertise score
    df['expertise_score'] = (df['years_norm'] * 0.6) + (df['projects_norm'] * 0.4)
    
    # Create radar chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=df['expertise_score'],
        theta=df['domain'],
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
    
    return fig

def create_project_distribution(projects_data):
    """
    Creates a pie chart showing the distribution of projects by category
    
    Parameters:
    -----------
    projects_data : list of dicts
        List containing project data with category information
    
    Returns:
    --------
    plotly.graph_objects.Figure
        A plotly figure object for the pie chart
    """
    df = pd.DataFrame(projects_data)
    category_counts = df['category'].value_counts().reset_index()
    category_counts.columns = ['category', 'count']
    
    fig = px.pie(
        category_counts,
        values='count',
        names='category',
        title='Projects by Category',
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    
    return fig

def create_tech_bubble_chart(projects_data):
    """
    Creates a bubble chart showing the frequency of technologies used in projects
    
    Parameters:
    -----------
    projects_data : list of dicts
        List containing project data with technology information
    
    Returns:
    --------
    plotly.graph_objects.Figure
        A plotly figure object for the bubble chart
    """
    df = pd.DataFrame(projects_data)
    
    # Extract all technologies used across projects
    tech_list = []
    for techs in df['tech']:
        tech_list.extend(techs)
    
    # Count frequency of each technology
    tech_counts = pd.Series(tech_list).value_counts().reset_index()
    tech_counts.columns = ['technology', 'count']
    
    # Create bubble chart
    fig = px.scatter(
        tech_counts,
        x='technology',
        y='count',
        size='count',
        color='technology',
        hover_name='technology',
        title='Technologies Used Across Projects',
        height=400
    )
    
    fig.update_layout(
        xaxis_title=None,
        yaxis_title='Number of Projects',
        showlegend=False
    )
    
    return fig
