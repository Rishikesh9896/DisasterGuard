import os
from dotenv import load_dotenv
import streamlit as st
from utils import load_css, display_card, EDUCATIONAL_IMAGES
import together
import time

# Load environment variables
load_dotenv()

# Configure Together AI
API_KEY = os.getenv("TOGETHER_API_KEY")
os.environ["TOGETHER_API_KEY"] = API_KEY

def get_bot_response(prompt: str) -> str:
    try:
        system_prompt = """You are a friendly and helpful educational assistant for children.
Your responses should be:
- Simple and easy to understand
- Positive and encouraging
- Brief (2-3 sentences)
- Include emojis where appropriate
- Educational but fun
Focus on teaching about disasters, sustainability, and environmental topics."""

        full_prompt = f"""<system>{system_prompt}</system>
<user>{prompt}</user>
<assistant>"""

        response = together.Completion.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            prompt=full_prompt,
            max_tokens=200,
            temperature=0.7,
            top_p=0.9,
            top_k=50,
            repetition_penalty=1.0
        )

        if hasattr(response, 'choices') and response.choices:
            response_text = response.choices[0].text
            response_text = response_text.replace('</assistant>', '').strip()
            return response_text
        else:
            return "I'd be happy to help you learn about that! Could you try asking again? 🎓"

    except Exception as e:
        st.error(f"API Error: {str(e)}")
        return "I'm excited to help! Could you please rephrase your question? 🌈"

def main():
    try:
        # Configure the page
        st.set_page_config(
            page_title="Kids Learn: Disaster & Sustainability",
            page_icon="🌍",
            layout="wide"
        )

        # Custom CSS with background image
        st.markdown("""
        <style>
        .stApp {
            background-image: url("https://media.istockphoto.com/id/1333043586/photo/tornado-in-stormy-landscape-climate-change-and-natural-disaster-concept.jpg?b=1&s=612x612&w=0&k=20&c=b4GXbWm4-KVxctCtlu3I_TP0YQZoT5g-mOvodnZOvk4=");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }
        .getting-started-card {
            background: linear-gradient(45deg, rgba(52, 152, 219, 0.9), rgba(41, 128, 185, 0.9));
            color: white;
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .getting-started-card h2 {
            color: white;
            margin-bottom: 15px;
        }
        .getting-started-card ul {
            list-style-type: none;
            padding-left: 0;
        }
        .getting-started-card li {
            margin: 10px 0;
            font-size: 1.1em;
        }
        .stButton > button {
            width: 100%;
            background-color: rgba(52, 152, 219, 0.8);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
            margin: 5px 0;
        }
        .stButton > button:hover {
            background-color: rgba(41, 128, 185, 0.9);
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .feature-section {
            margin-top: 40px;
        }
        .feature-card {
            background: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 10px 0;
            transition: transform 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-5px);
        }
        .feature-card h3 {
            font-weight: 700 !important;
            font-size: 1.3em !important;
            color: #2c3e50 !important;
            text-shadow: none !important;
            margin-bottom: 10px !important;
        }
        .stMarkdown {
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        h1, h2, h3 {
            color: white !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .stChatMessage {
            background-color: rgba(255, 255, 255, 0.9) !important;
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
        }
        .stChatMessage p {
            color: black !important;
            text-shadow: none !important;
        }
        .stChatInput {
            background-color: rgba(255, 255, 255, 0.9) !important;
            border-radius: 10px;
        }
        .stExpander {
            background-color: rgba(255, 255, 255, 0.9) !important;
            border-radius: 10px;
            margin: 10px 0;
        }
        </style>
        """, unsafe_allow_html=True)

        # Create two columns for main layout
        main_col, chat_col = st.columns([2, 1])

        with main_col:
            st.title("Welcome to Disaster Guard! 🌟")
            
            # Getting Started Section
            st.markdown("""
            <div class="getting-started-card">
                <h2>🚀 Getting Started</h2>
                <p>Welcome to our Disaster Management Learning App! Here's how to begin:</p>
                <ul>
                    <li>🎮 Try our interactive safety simulations</li>
                    <li>📚 Read through our fun learning guides</li>
                    <li>✍️ Test what you've learned with quizzes</li>
                    <li>👥 Join our community to share experiences</li>
                    <li>🌟 Track your progress and earn stars!</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            # Quick Access Buttons
            button_cols = st.columns(4)
            
            with button_cols[0]:
                if st.button("🎮 Try Simulation", use_container_width=True, key="sim_button"):
                    st.switch_page("simulations")
            
            with button_cols[1]:
                if st.button("📚 Read Guides", use_container_width=True, key="guide_button"):
                    st.switch_page("documentation")
            
            with button_cols[2]:
                if st.button("✍️ Take Quiz", use_container_width=True, key="quiz_button"):
                    st.switch_page("_test_page")
            
            with button_cols[3]:
                if st.button("👥 Community", use_container_width=True, key="community_button"):
                    st.switch_page("community")

            # Features Section
            st.markdown("### Learn About Disasters and Safety! 🌍")
            col1, col2 = st.columns(2)

            with col1:
                display_card(
                    "**Natural Disasters** 🌋",
                    "Learn about earthquakes, floods, and how to stay safe!",
                    EDUCATIONAL_IMAGES[0]
                )

                display_card(
                    "**Emergency Response** 🚑",
                    "Discover how to help yourself and others during emergencies!",
                    EDUCATIONAL_IMAGES[1]
                )

            with col2:
                display_card(
                    "**Community Forum** 👥",
                    "Share experiences and learn from others in our community!",
                    EDUCATIONAL_IMAGES[2]
                )

                display_card(
                    "**Interactive Learning** 🎯",
                    "Fun games and activities to test your knowledge!",
                    EDUCATIONAL_IMAGES[3]
                )

        # Chatbot section
        with chat_col:
            st.markdown("### Chat with Your Learning Buddy! 🤖")
            
            # Initialize chat history
            if "messages" not in st.session_state:
                st.session_state.messages = []

            # Display chat history
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            # Chat input
            if prompt := st.chat_input("Ask me anything! 😊"):
                # Add user message to chat
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                # Get and display assistant response
                with st.chat_message("assistant"):
                    with st.spinner("Thinking... 🤔"):
                        response = get_bot_response(prompt)
                        time.sleep(0.5)
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})

            # Quick questions
            with st.expander("Try these questions! 💡"):
                quick_questions = {
                    "What is sustainability? 🌱": "What is sustainability?",
                    "How to save water? 💧": "How can I save water?",
                    "Earthquake safety? 🏠": "What should I do during an earthquake?",
                    "Recycling tips? ♻️": "How do I recycle properly?"
                }

                for button_text, question in quick_questions.items():
                    if st.button(button_text):
                        st.session_state.messages.append({"role": "user", "content": question})
                        response = get_bot_response(question)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        st.rerun()

            # Clear chat button
            if st.button("Clear Chat 🗑️"):
                st.session_state.messages = []
                st.rerun()

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()