import streamlit as st
from utils import load_css, display_card

# Direct page content
st.title("Disaster Education 🚨")
st.markdown("### Learn About Natural Disasters and Stay Safe!")

col1, col2 = st.columns(2)

with col1:
    display_card(
        "Earthquakes 🌋",
        "Learn what causes earthquakes and how to stay safe.",
        "https://images.unsplash.com/photo-1533000759938-aa0ba70beceb"  # Earthquake image
    )
    
    display_card(
        "Floods 🌊",
        "Discover important flood safety tips and preparation.",
        "https://images.unsplash.com/photo-1547683917-9a5f618d7c80"  # Flood image
    )

with col2:
    display_card(
        "Hurricanes 🌪️",
        "Understanding hurricanes and how to prepare for them.",
        "https://images.unsplash.com/photo-1584267385494-9fdd9a71ad75"  # Hurricane image
    )
    
    display_card(
        "Fire Safety 🔥",
        "Learn about fire prevention and emergency procedures.",
        "https://images.unsplash.com/photo-1486162928267-e664739fb150"  # Fire safety image
    )

# Add interactive element
with st.expander("Safety Tips 📝"):
    st.markdown("""
    - Stay calm during emergencies 🧘
    - Know emergency numbers 📞
    - Have an emergency kit ready 🎒
    - Follow evacuation instructions 🚶
    """)