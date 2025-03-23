# Chiranjib Koch's Portfolio Website

This repository contains the portfolio website for Chiranjib Koch, showcasing expertise in AI, ML, Python, MongoDB, and Telegram projects.

## Features

- **Dual Hosting Support**: Can be hosted both as a Streamlit app and as a static GitHub Pages site
- **Interactive UI**: Clean and modern interface with responsive design
- **Project Portfolio**: Filterable display of professional projects
- **Skills Visualization**: Visual representations of technical skills and expertise
- **Blog Section**: Technical articles and tutorials
- **Contact Form**: For inquiries and collaborations

## Getting Started

### Streamlit App (Dynamic Version)

1. Clone the repository
2. Install requirements:
   ```
   pip install streamlit pandas plotly pillow
   ```
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

### GitHub Pages (Static Version)

The static version of the site is built with HTML, CSS, and JavaScript, making it suitable for GitHub Pages hosting.

1. Fork this repository
2. Enable GitHub Pages in your repository settings
3. The site will be available at `https://[your-username].github.io/[repository-name]`

## File Structure

```
├── .streamlit/              # Streamlit configuration
├── assets/                  # Images, resume, and other static files
├── pages/                   # Streamlit multi-page app components
│   ├── blog.py              # Blog page
│   ├── contact.py           # Contact page
│   ├── projects.py          # Projects portfolio
│   └── skills.py            # Skills & expertise
├── utils/                   # Utility functions
│   ├── data.py              # Data structures
│   └── visualizations.py    # Visualization components
├── app.py                   # Main Streamlit application
├── index.html               # Static HTML version for GitHub Pages
├── styles.css               # Styles for static site
└── script.js                # JavaScript for static site
```

## Customization

### For Streamlit Version

Modify the content in `app.py`, files in the `pages/` directory, and data structures in `utils/data.py`.

### For Static HTML Version

Edit `index.html`, `styles.css`, and `script.js` to customize the static site version.

## License

MIT

## About

Created by Chiranjib Koch, an expert in AI, ML, Python, MongoDB, and Telegram projects.