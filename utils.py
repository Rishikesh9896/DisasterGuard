import streamlit as st
import plotly.graph_objects as go
import os
from typing import Dict, List

def load_css():
    """Load CSS with proper path handling"""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        css_path = os.path.join(current_dir, 'style.css')

        if not os.path.exists(css_path):
            st.error(f"CSS file not found at: {css_path}")
            return

        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Failed to load CSS: {str(e)}")

def display_card(title: str, content: str, image_url: str = None):
    """Display card with fallback image handling"""
    try:
        card_style = """
            <style>
            .child-friendly-card {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 15px;
                margin: 10px 0;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                border: 2px solid #3498db;
            }
            .child-friendly-card img {
                width: 100%;
                max-height: 200px;
                object-fit: cover;
                border-radius: 10px;
                margin-bottom: 15px;
            }
            .child-friendly-card h3 {
                color: #2980b9;
                margin: 10px 0;
            }
            .child-friendly-card p {
                color: #34495e;
                font-size: 16px;
            }
            </style>
        """
        
        with st.container():
            st.markdown(card_style, unsafe_allow_html=True)
            
            # Use a default placeholder if image_url is None or empty
            if not image_url:
                image_url = "https://placehold.co/600x400/png?text=Learning+is+Fun!"

            html_content = f"""
            <div class="child-friendly-card">
                <img src="{image_url}" 
                     alt="{title}"
                     onerror="this.onerror=null;this.src='https://placehold.co/600x400/png?text=Image+Not+Found';">
                <h3>{title}</h3>
                <p>{content}</p>
            </div>
            """
            st.markdown(html_content, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error displaying card: {str(e)}")

# Define image arrays with reliable placeholder images
EDUCATIONAL_IMAGES = [
    "https://placehold.co/600x400/blue/white?text=Education+1",
    "https://placehold.co/600x400/green/white?text=Education+2",
    "https://placehold.co/600x400/orange/white?text=Education+3",
    "https://placehold.co/600x400/purple/white?text=Education+4"
]

DISASTER_IMAGES = [
    "https://placehold.co/600x400/red/white?text=Earthquake+Safety",
    "https://placehold.co/600x400/blue/white?text=Flood+Safety",
    "https://placehold.co/600x400/gray/white?text=Hurricane+Safety",
    "https://placehold.co/600x400/orange/white?text=Fire+Safety"
]

SUSTAINABILITY_IMAGES = [
    "https://placehold.co/600x400/green/white?text=Recycling",
    "https://placehold.co/600x400/yellow/white?text=Energy+Saving",
    "https://placehold.co/600x400/blue/white?text=Water+Conservation",
    "https://placehold.co/600x400/teal/white?text=Green+Living"
]

SIMULATION_IMAGES = [
    "https://placehold.co/600x400/purple/white?text=Simulation+1",
    "https://placehold.co/600x400/blue/white?text=Simulation+2",
    "https://placehold.co/600x400/green/white?text=Simulation+3",
    "https://placehold.co/600x400/orange/white?text=Simulation+4"
]

def create_progress_bar(progress: float, title: str):
    """Create a gauge-style progress bar"""
    try:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=progress * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': title},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#2ECC71"},
                'bgcolor': "#ECF0F1",
                'borderwidth': 2,
                'bordercolor': "#34495E",
            }
        ))
        fig.update_layout(height=200)
        return fig
    except Exception as e:
        st.error(f"Error creating progress bar: {str(e)}")
        return None