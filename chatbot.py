import streamlit as st
import os
from dotenv import load_dotenv
import together
import time

# Load environment variables
load_dotenv()

# Configure Together AI
API_KEY = os.getenv("TOGETHER_API_KEY")
os.environ["TOGETHER_API_KEY"] = API_KEY

def get_bot_response(prompt: str) -> str:
    try:
        # Create a child-friendly system prompt
        system_prompt = """You are a friendly and helpful educational assistant for children.
Your responses should be:
- Simple and easy to understand
- Positive and encouraging
- Brief (2-3 sentences)
- Include emojis where appropriate
- Educational but fun
Focus on teaching about disasters, sustainability, and environmental topics."""

        # Format the prompt properly
        full_prompt = f"""<system>{system_prompt}</system>
<user>{prompt}</user>
<assistant>"""

        # Get response from API
        response = together.Completion.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            prompt=full_prompt,
            max_tokens=200,
            temperature=0.7,
            top_p=0.9,
            top_k=50,
            repetition_penalty=1.0
        )

        # Extract the response text correctly
        if hasattr(response, 'choices') and response.choices:
            # Get the text from the first choice
            response_text = response.choices[0].text
            # Clean up the response
            response_text = response_text.replace('</assistant>', '').strip()
            return response_text
        else:
            return "I'd be happy to help you learn about that! Could you try asking again? 🎓"

    except Exception as e:
        st.error(f"API Error: {str(e)}")
        return "I'm excited to help! Could you please rephrase your question? 🌈"

def main():
    # Page configuration
    st.set_page_config(page_title="Learning Assistant", page_icon="🤖")

    # Title and description
    st.title("Chat with Your Learning Assistant 🤖")
    st.markdown("### I'm here to help you learn about disasters and sustainability! 🌍")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask me anything! I'm here to help 😊"):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Let me think about that... 🤔"):
                response = get_bot_response(prompt)
                time.sleep(0.5)  # Small delay for better UX
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

    # Quick questions section
    st.sidebar.markdown("### Quick Questions 💭")
    quick_questions = {
        "What is sustainability? 🌱": "What is sustainability and why is it important?",
        "How to save water? 💧": "What are some simple ways to save water at home?",
        "Earthquake safety? 🏠": "What should I do during an earthquake?",
        "Recycling tips? ♻️": "What are the basic rules of recycling?",
        "Climate change? 🌍": "Can you explain climate change in simple terms?"
    }

    for button_text, question in quick_questions.items():
        if st.sidebar.button(button_text):
            st.session_state.messages.append({"role": "user", "content": question})
            response = get_bot_response(question)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.experimental_rerun()

    # Clear chat button
    if st.sidebar.button("Clear Chat 🗑️"):
        st.session_state.messages = []
        st.experimental_rerun()

    # Tips section
    st.sidebar.markdown("""
    ### Tips for Better Answers 💡
    1. Ask specific questions
    2. One topic at a time
    3. Use simple words
    4. Try the quick questions above
    """)

if __name__ == "__main__":
    main()