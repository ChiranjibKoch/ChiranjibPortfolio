import streamlit as st
import pandas as pd
import base64
from PIL import Image
from pathlib import Path
from utils.visitor_counter import display_visitor_counter

# Page configuration
st.set_page_config(
    page_title="Chiranjib Koch - AI & ML Expert",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def download_button(object_to_download, download_filename, button_text):
    if isinstance(object_to_download, Path):
        with open(object_to_download, 'rb') as f:
            data = f.read()
    else:
        data = object_to_download

    button_uuid = "download_button"
    
    st.download_button(
        label=button_text,
        data=data,
        file_name=download_filename,
        mime="application/octet-stream",
        key=button_uuid,
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
    
    # Resume download
    st.write("### Download Resume")
    download_button(
        Path("assets/resume.pdf"),
        "Chiranjib_Koch_Resume.pdf",
        "Download Resume 📄"
    )
    
    st.divider()
    st.caption("© 2023 Chiranjib Koch")

# Main content
st.title("Chiranjib Koch")
st.subheader("AI | Machine Learning | Python | MongoDB | Telegram Projects")

# Header section with profile picture
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("""
    <div style="display: flex; justify-content: center;">
        <svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <circle cx="100" cy="80" r="50" fill="#0066cc" />
            <circle cx="100" cy="70" r="40" fill="#ffffff" />
            <path d="M100 200 C 50 140, 150 140, 100 200" fill="#0066cc" />
            <circle cx="85" cy="65" r="5" fill="#000000" />
            <circle cx="115" cy="65" r="5" fill="#000000" />
            <path d="M85 85 Q 100 100, 115 85" stroke="#000000" fill="transparent" stroke-width="2" />
        </svg>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    ## About Me
    
    Hello! I'm **Chiranjib Koch**, an experienced professional specializing in Artificial Intelligence, 
    Machine Learning, Python development, MongoDB database solutions, and Telegram bot projects.
    
    With a passion for leveraging cutting-edge technologies to solve complex problems, 
    I create innovative solutions that drive business value and technological advancement.
    
    Feel free to explore my portfolio to learn more about my expertise and projects.
    """)

# Featured skills
st.markdown("## Featured Skills")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown("### 🧠")
    st.markdown("**AI**")
    st.caption("Deep Learning, NLP, Computer Vision")
with col2:
    st.markdown("### 📊")
    st.markdown("**ML**")
    st.caption("Predictive Analytics, Classification, Clustering")
with col3:
    st.markdown("### 🐍")
    st.markdown("**Python**")
    st.caption("Web Dev, Data Analysis, Automation")
with col4:
    st.markdown("### 🗄️")
    st.markdown("**MongoDB**")
    st.caption("Database Design, Aggregation, Performance")
with col5:
    st.markdown("### 📱")
    st.markdown("**Telegram**")
    st.caption("Bot Development, Automation, Integration")

# Featured projects
st.markdown("## Featured Projects")
featured_projects = [
    {
        "title": "AI-Powered Recommendation System",
        "description": "Developed a recommendation engine using collaborative filtering and deep learning techniques.",
        "tech": ["Python", "TensorFlow", "MongoDB", "Flask"],
        "image": "🤖"
    },
    {
        "title": "Advanced Telegram Bot Framework",
        "description": "Created a robust framework for developing and deploying Telegram bots with advanced functionalities.",
        "tech": ["Python", "Telegram API", "MongoDB", "Docker"],
        "image": "📱"
    },
    {
        "title": "Predictive Analytics Dashboard",
        "description": "Built an interactive dashboard for visualizing ML predictions and business insights.",
        "tech": ["Python", "Streamlit", "Pandas", "Scikit-learn"],
        "image": "📊"
    }
]

# Display featured projects
col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for i, project in enumerate(featured_projects):
    with cols[i]:
        st.markdown(f"### {project['image']} {project['title']}")
        st.write(project['description'])
        st.write("**Technologies:** " + ", ".join(project['tech']))
        if i == 0:
            st.link_button("View Details", "pages/projects.py", use_container_width=True)
        else:
            st.button("View Details", key=f"button_{i}", use_container_width=True)

# Call to action
st.divider()
st.markdown("## Let's Connect")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    Interested in collaborating or learning more about my work?
    
    Check out my full projects list or get in touch through the contact page.
    """)
with col2:
    st.link_button("View All Projects", "pages/projects.py", use_container_width=True)
    st.link_button("Contact Me", "pages/contact.py", use_container_width=True)

# Display visitor counter at the bottom
display_visitor_counter()
