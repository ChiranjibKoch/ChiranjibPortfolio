import streamlit as st
import json
import os
from datetime import datetime

def load_visitor_data():
    """
    Load visitor data from JSON file
    """
    visitor_file = 'visitor_data.json'
    if os.path.exists(visitor_file):
        try:
            with open(visitor_file, 'r') as f:
                return json.load(f)
        except:
            return {"total_visits": 0, "last_visits": [], "page_visits": {}}
    else:
        return {"total_visits": 0, "last_visits": [], "page_visits": {}}

def save_visitor_data(data):
    """
    Save visitor data to JSON file
    """
    visitor_file = 'visitor_data.json'
    with open(visitor_file, 'w') as f:
        json.dump(data, f)

def track_visit(page="home"):
    """
    Track a new visit to the site
    """
    if 'visitor_counted' not in st.session_state:
        visitor_data = load_visitor_data()
        
        # Increment total visit count
        visitor_data["total_visits"] += 1
        
        # Add timestamp for this visit
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        visitor_data["last_visits"].append(timestamp)
        
        # Keep only last 100 visits in the list
        if len(visitor_data["last_visits"]) > 100:
            visitor_data["last_visits"] = visitor_data["last_visits"][-100:]
        
        # Track page-specific visits
        if page in visitor_data["page_visits"]:
            visitor_data["page_visits"][page] += 1
        else:
            visitor_data["page_visits"][page] = 1
            
        # Save the updated data
        save_visitor_data(visitor_data)
        
        # Mark this session as counted
        st.session_state.visitor_counted = True
        st.session_state.total_visits = visitor_data["total_visits"]
    
    return st.session_state.total_visits

def display_visitor_counter():
    """
    Display a visitor counter at the bottom of the page
    """
    total_visits = track_visit()
    
    # Create a container with a dark background at the bottom of the page
    with st.container():
        st.markdown(
            f"""
            <div style="
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: rgba(0, 0, 0, 0.7);
                color: white;
                text-align: center;
                padding: 10px;
                font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif;
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                z-index: 1000;
            ">
                <span style="font-size: 0.9rem;">
                    <span style="color: #4cc9f0;">Total Portfolio Visitors:</span> {total_visits}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )