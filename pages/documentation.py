import streamlit as st
from utils import load_css

# Page configuration
st.set_page_config(page_title="Documentation", page_icon="📚", layout="wide")

# Custom CSS for background image and text visibility
st.markdown("""
<style>
/* Background Image */
.stApp {
    background: url("https://png.pngtree.com/thumb_back/fh260/background/20240610/pngtree-concept-of-earthquake-or-natural-disaster-image_15746377.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Improved Text Visibility */
h1, h2, h3, h4, h5, h6, p, .stText {
    color: white !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
}

/* Card Styling */
.card {
    padding: 20px;
    border-radius: 10px;
    margin: 10px 0;
    background: rgba(255, 255, 255, 0.85); /* Light background for readability */
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    cursor: pointer;
    color: black !important;
}
.card:hover {
    transform: translateY(-5px);
}

/* Buttons */
.quiz-button, .stButton > button {
    background-color: #4CAF50;
    color: white !important;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    cursor: pointer;
    font-size: 16px;
    margin-top: 10px;
}
.quiz-button:hover, .stButton > button:hover {
    background-color: #45a049;
}

/* Form Inputs */
.stTextInput label, .stSelectbox label, .stTextArea label {
    color: white !important;
    font-weight: bold;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
}

/* Content Sections */
.content-section {
    padding: 20px;
    border-radius: 10px;
    background: rgba(0, 0, 0, 0.6); /* Dark transparent background */
    color: white !important;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state for content visibility
if 'current_section' not in st.session_state:
    st.session_state.current_section = None

# Function to display card with button
def display_card_with_button(title, description, image_url, key):
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image(image_url, use_container_width=True)
    with col2:
        st.markdown(f"### {title}")
        st.markdown(description)
        if st.button("Learn More", key=key):
            st.session_state.current_section = key

# Main Page Content
st.title("📚 **Documentation**")
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

# Content sections with improved visibility
if st.session_state.current_section:
    st.markdown("---")
    with st.container():
        if st.session_state.current_section == "safety_guides":
            st.markdown("""
            ### 🛑 **Detailed Safety Guides**  
            #### 🏠 Earthquake Safety  
            **Before:** Secure furniture, identify safe spots, have an emergency kit  
            **During:** Drop, Cover, and Hold On  
            **After:** Check for injuries, prepare for aftershocks  
            
            #### 🔥 Fire Safety  
            **Prevention:** Install smoke detectors, plan evacuations  
            **During:** Stay low, feel doors for heat, use stairs  
            """, unsafe_allow_html=True)

        elif st.session_state.current_section == "educational_videos":
            st.markdown("""
            ### 🎥 **Educational Video Library**  
            ✅ Disaster Preparedness Basics  
            ✅ Emergency Response Training  
            ✅ Safety Drills and Procedures  
            """, unsafe_allow_html=True)

        elif st.session_state.current_section == "interactive_quizzes":
            st.markdown("""
            ### ✏️ **Interactive Quizzes**  
            ✅ Basic Safety Knowledge  
            ✅ Disaster-Specific Quizzes  
            ✅ First Aid and Emergency Response  
            """, unsafe_allow_html=True)
            if st.button("🎯 Start a Quiz", key="start_quiz"):
                try:
                    st.switch_page("Test page")
                except:
                    try:
                        st.switch_page("Test_page")
                    except:
                        try:
                            st.switch_page("_test_page")
                        except:
                            st.switch_page("Test Page")

        elif st.session_state.current_section == "additional_resources":
            st.markdown("""
            ### 📑 **Additional Resources & Emergency Contacts**  
            ☎️ **Emergency Services:** 911  
            ☠️ **Poison Control:** 1-800-222-1222  
            🔗 **Useful Links:** [FEMA](https://www.fema.gov) | [Red Cross](https://www.redcross.org)  
            """, unsafe_allow_html=True)

# Expander for tips on using resources
with st.expander("📝 **How to Use These Resources**"):
    st.markdown("""
    ✅ **Browse Categories:** Click any card to view content  
    ✅ **Access Materials:** Download guides, watch videos, take quizzes  
    ✅ **Stay Prepared:** Keep emergency contacts handy, update emergency kits  
    ✅ **Get Help:** Use emergency numbers, follow official guidelines  
    """, unsafe_allow_html=True)
