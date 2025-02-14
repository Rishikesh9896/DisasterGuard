import streamlit as st
from utils import load_css, display_card, SUSTAINABILITY_IMAGES

# Direct page content
st.title("Sustainability Education 🌱")
st.markdown("### Learn How to Protect Our Planet!")

col1, col2 = st.columns(2)

with col1:
    display_card(
        "Recycling ♻️",
        "Learn why and how to recycle different materials.",
        SUSTAINABILITY_IMAGES[0]
    )
    
    display_card(
        "Save Energy 💡",
        "Discover ways to save energy at home and school.",
        SUSTAINABILITY_IMAGES[1]
    )

with col2:
    display_card(
        "Water Conservation 💧",
        "Learn how to save water in your daily life.",
        SUSTAINABILITY_IMAGES[2]
    )
    
    display_card(
        "Green Living 🌿",
        "Simple tips for living an eco-friendly life.",
        SUSTAINABILITY_IMAGES[3]
    )

# Add interactive element
with st.expander("Daily Green Tips 🌟"):
    st.markdown("""
    - Turn off lights when leaving a room 💡
    - Use reusable water bottles 🚰
    - Recycle paper and plastic ♻️
    - Take shorter showers 🚿
    """)