import streamlit as st
from utils import load_css

# Page configuration
st.set_page_config(page_title="Documentation", page_icon="📚", layout="wide")

# Custom CSS for cards
st.markdown("""
<style>
.card {
    padding: 20px;
    border-radius: 10px;
    margin: 10px 0;
    background: white;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    cursor: pointer;
}
.card:hover {
    transform: translateY(-5px);
}
.card img {
    width: 100%;
    border-radius: 10px;
    margin-bottom: 10px;
    height: 200px;
    object-fit: cover;
}
.content-section {
    padding: 20px;
    border-radius: 10px;
    background: #f8f9fa;
    margin-top: 20px;
}
.quiz-button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    cursor: pointer;
    font-size: 16px;
    margin-top: 10px;
}
.quiz-button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state for content visibility
if 'current_section' not in st.session_state:
    st.session_state.current_section = None

def display_card_with_button(title, description, image_url, key):
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image(image_url, use_container_width=True)
    with col2:
        st.markdown(f"### {title}")
        st.markdown(description)
        if st.button("Learn More", key=key):
            st.session_state.current_section = key

# Main page content
st.title("Documentation 📚")
st.markdown("### Learning Resources and Guides")

col1, col2 = st.columns(2)

with col1:
    display_card_with_button(
        "Safety Guides 📖",
        "Complete guides for disaster preparedness.",
        "https://images.unsplash.com/photo-1516979187457-637abb4f9353",
        "safety_guides"
    )
    
    display_card_with_button(
        "Educational Videos 🎥",
        "Watch and learn about various topics.",
        "https://images.unsplash.com/photo-1485846234645-a62644f84728",
        "educational_videos"
    )

with col2:
    display_card_with_button(
        "Interactive Quizzes ✏️",
        "Test your knowledge and learn more.",
        "https://images.unsplash.com/photo-1434030216411-0b793f4b4173",
        "interactive_quizzes"
    )
    
    display_card_with_button(
        "Additional Resources 📑",
        "Find more learning materials here.",
        "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8",
        "additional_resources"
    )

# Content sections
if st.session_state.current_section:
    st.markdown("---")
    
    if st.session_state.current_section == "safety_guides":
        st.markdown("""
        ### Detailed Safety Guides 📖
        
        #### Earthquake Safety
        1. **Before an Earthquake**
           - Secure heavy furniture and objects
           - Know safe spots in each room
           - Have an emergency kit ready

        2. **During an Earthquake**
           - Drop, Cover, and Hold On
           - Stay away from windows
           - If indoors, stay inside

        3. **After an Earthquake**
           - Check for injuries
           - Listen to emergency radio
           - Be prepared for aftershocks

        #### Fire Safety
        1. **Prevention**
           - Install smoke detectors
           - Create evacuation plan
           - Keep fire extinguishers ready

        2. **During a Fire**
           - Stay low to avoid smoke
           - Feel doors for heat
           - Use stairs, not elevators
        """)

    elif st.session_state.current_section == "educational_videos":
        st.markdown("""
        ### Educational Video Library 🎥
        
        #### Featured Videos
        1. **Disaster Preparedness Basics**
           - Understanding Natural Disasters
           - Basic Safety Protocols
           - Emergency Kit Preparation

        2. **Emergency Response Training**
           - First Aid Basics
           - CPR Techniques
           - Emergency Communications

        3. **Safety Drills and Procedures**
           - School Safety Protocols
           - Workplace Emergency Procedures
           - Home Safety Measures
        
        #### Popular Topics
        - First Aid Basics
        - Emergency Evacuation
        - Natural Disaster Response
        """)

    elif st.session_state.current_section == "interactive_quizzes":
        st.markdown("""
        ### Interactive Learning Quizzes ✏️
        
        Test your knowledge with our interactive quizzes:
        
        #### Available Quiz Topics:
        1. **Basic Safety Knowledge**
           - General Safety Principles
           - Emergency Procedures
           - First Aid Basics

        2. **Disaster-Specific Quizzes**
           - Earthquake Preparedness
           - Fire Safety
           - Tornado Safety

        3. **First Aid and Emergency Response**
           - Basic First Aid
           - Emergency Protocols
           - Safety Procedures
        """)
        
        # Try each of these options one at a time until one works
        if st.button("Start a Quiz Now 🎯", key="start_quiz"):
            try:
                # Option 1: Using the display name
                st.switch_page("Test page")
            except:
                try:
                    # Option 2: Using underscore
                    st.switch_page("Test_page")
                except:
                    try:
                        # Option 3: Using original filename
                        st.switch_page("_test_page")
                    except:
                        # Option 4: Using capitalization
                        st.switch_page("Test Page")

    elif st.session_state.current_section == "additional_resources":
        st.markdown("""
        ### Additional Resources and Links 📑
        
        #### Emergency Contacts
        - **Emergency Services:** 911
        - **Poison Control:** 1-800-222-1222
        - **Local Emergency Management:** [Find your local office](https://www.fema.gov/locations)
        
        #### Useful Links
        - [FEMA Website](https://www.fema.gov)
        - [Red Cross Preparedness](https://www.redcross.org)
        - [Weather Alerts](https://www.weather.gov)
        
        #### Mobile Apps
        1. **Emergency Alert Apps**
           - FEMA App
           - Red Cross Emergency
           - Weather Underground

        2. **First Aid Apps**
           - Red Cross First Aid
           - First Aid by American Heart Association
           - Emergency First Aid & Treatment Guide
        """)

# How to Use Resources section
with st.expander("How to Use Resources 📝"):
    st.markdown("""
    1. **Browse Categories**
       - Click on any card to view detailed content
       - Use the navigation menu for quick access
    
    2. **Access Materials**
       - Download guides for offline use
       - Watch educational videos
       - Take interactive quizzes
    
    3. **Stay Prepared**
       - Keep emergency contacts handy
       - Update your emergency kit regularly
       - Practice safety drills
    
    4. **Get Help**
       - Use emergency numbers when needed
       - Contact local authorities
       - Follow official guidelines
    """)