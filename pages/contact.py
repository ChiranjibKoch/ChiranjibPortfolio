import streamlit as st
import pandas as pd
from utils.visitor_counter import display_visitor_counter

# Page configuration
st.set_page_config(
    page_title="Contact - Chiranjib Koch",
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
st.title("Contact Information")
st.markdown("""
Feel free to reach out to me for project inquiries, collaborations, or any questions about my work.
I'm always open to discussing new opportunities and ideas.
""")

# Contact form
st.markdown("### Send Me a Message")
with st.form(key="contact_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.text_input("Subject")
    
    with col2:
        message = st.text_area("Message", height=123)
    
    submit_button = st.form_submit_button(label="Send Message")
    
    if submit_button:
        if name and email and subject and message:
            st.success("Thank you for your message! I'll get back to you soon.")
            # In a real application, you would process the form data here
            # For example, sending an email or storing in a database
        else:
            st.error("Please fill in all fields.")

# Contact information
st.markdown("### Other Ways to Connect")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("#### Contact Details")
        st.markdown("""
        **Email:** chiranjib.koch@example.com
        
        **Phone:** +91123
        
        **Location:** New Delhi, India
        """)

with col2:
    with st.container(border=True):
        st.markdown("#### Social Media")
        st.markdown("""
        **LinkedIn:** [linkedin.com/in/chiranjibkoch](https://linkedin.com/in/chiranjibkoch)
        
        **GitHub:** [github.com/chiranjibkoch](https://github.com/chiranjibkoch)
        
        **Twitter:** [@chiranjibkoch](https://twitter.com/chiranjibkoch)
        """)

# Availability
st.markdown("### Availability")
st.info("""
I'm currently available for freelance projects, consulting, and part-time collaborations.
For full-time opportunities, please contact me to discuss availability.
""")

# FAQ
st.markdown("### Frequently Asked Questions")

faq = [
    {
        "question": "What types of projects do you typically work on?",
        "answer": """
        I specialize in AI/ML applications, data analysis systems, database optimization, 
        and automation solutions including Telegram bots. I particularly enjoy working on 
        projects that involve complex data processing challenges or require integration of 
        multiple technologies.
        """
    },
    {
        "question": "How do you charge for your services?",
        "answer": """
        My pricing model depends on the project scope and requirements. I offer hourly rates, 
        fixed project fees, and retainer arrangements. After understanding your project needs, 
        I'll provide a detailed proposal with transparent pricing options.
        """
    },
    {
        "question": "Can you work with existing teams or codebases?",
        "answer": """
        Absolutely! I have extensive experience collaborating with development teams and 
        working with established codebases. I'm comfortable adapting to your team's workflow, 
        coding standards, and communication practices.
        """
    },
    {
        "question": "What is your typical development process?",
        "answer": """
        My process typically includes: initial consultation, requirements gathering, design/planning, 
        iterative development with regular check-ins, testing, deployment, and optional maintenance. 
        I emphasize clear communication throughout the process and can adapt to your preferred 
        methodology (Agile, Scrum, etc.).
        """
    }
]

for i, item in enumerate(faq):
    with st.expander(item["question"]):
        st.markdown(item["answer"])

# Display visitor counter at the bottom
display_visitor_counter()
