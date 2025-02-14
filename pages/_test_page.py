import streamlit as st
import json
import random
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Safety Knowledge Test",
    page_icon="📝",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .quiz-container {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .question {
        font-size: 1.2em;
        color: #2c3e50;
        margin-bottom: 15px;
    }
    .score-display {
        font-size: 1.5em;
        text-align: center;
        padding: 20px;
        background: linear-gradient(45deg, #3498db, #2980b9);
        color: white;
        border-radius: 10px;
        margin: 20px 0;
    }
    .leaderboard {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .stButton > button {
        background-color: #2ecc71;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #27ae60;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# Quiz questions database
quiz_questions = {
    "earthquake": [
        {
            "question": "What should you do first during an earthquake?",
            "options": [
                "Run outside",
                "Drop to the ground",
                "Call emergency services",
                "Look out the window"
            ],
            "correct": 1
        },
        {
            "question": "Which is the safest place during an earthquake?",
            "options": [
                "Under a sturdy desk",
                "Near windows",
                "In an elevator",
                "Outside the building"
            ],
            "correct": 0
        },
        {
            "question": "What is the 'Triangle of Life' in earthquake safety?",
            "options": [
                "A warning system",
                "A safety position",
                "A safe space next to solid objects",
                "An emergency kit"
            ],
            "correct": 2
        },
        {
            "question": "What should you do after an earthquake?",
            "options": [
                "Immediately run outside",
                "Use elevators to evacuate",
                "Check for injuries and damage",
                "Call all your friends"
            ],
            "correct": 2
        },
        {
            "question": "Which item is most important in an earthquake kit?",
            "options": [
                "Television",
                "Water supply",
                "Board games",
                "Books"
            ],
            "correct": 1
        }
    ],
    "fire": [
        {
            "question": "What should you do if your clothes catch fire?",
            "options": [
                "Run to find water",
                "Stop, Drop, and Roll",
                "Call for help",
                "Remove clothing"
            ],
            "correct": 1
        },
        {
            "question": "How should you move through a smoke-filled room?",
            "options": [
                "Run quickly",
                "Walk normally",
                "Crawl low to the ground",
                "Hold your breath and sprint"
            ],
            "correct": 2
        },
        {
            "question": "What should you check before opening a door during a fire?",
            "options": [
                "Look through the peephole",
                "Feel the door and handle for heat",
                "Open it slowly",
                "Knock first"
            ],
            "correct": 1
        },
        {
            "question": "Where should you meet your family after evacuating?",
            "options": [
                "In the house",
                "At a predetermined meeting place",
                "At the neighbor's house",
                "By the front door"
            ],
            "correct": 1
        },
        {
            "question": "How often should you test smoke alarms?",
            "options": [
                "Once a year",
                "Every month",
                "Every day",
                "Never"
            ],
            "correct": 1
        }
    ],
    "tornado": [
        {
            "question": "Where is the safest place during a tornado?",
            "options": [
                "Near windows",
                "In a mobile home",
                "In a basement or storm cellar",
                "Outside watching it"
            ],
            "correct": 2
        },
        {
            "question": "What is a tornado watch?",
            "options": [
                "A tornado has been spotted",
                "Conditions are right for a tornado",
                "A tornado has passed",
                "Time to watch the news"
            ],
            "correct": 1
        },
        {
            "question": "What should you do if you're in a car during a tornado?",
            "options": [
                "Drive faster than the tornado",
                "Park under an overpass",
                "Seek sturdy shelter immediately",
                "Stay in the car"
            ],
            "correct": 2
        },
        {
            "question": "What is the best protection during a tornado?",
            "options": [
                "A blanket",
                "A helmet or thick padding",
                "Sunglasses",
                "An umbrella"
            ],
            "correct": 1
        },
        {
            "question": "What weather conditions often precede a tornado?",
            "options": [
                "Clear skies",
                "Heavy snow",
                "Dark, greenish clouds",
                "Extreme heat"
            ],
            "correct": 2
        }
    ]
}

def load_leaderboard():
    try:
        with open('leaderboard.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_leaderboard(leaderboard):
    with open('leaderboard.json', 'w') as f:
        json.dump(leaderboard, f)

def display_leaderboard(leaderboard):
    if leaderboard:
        df = pd.DataFrame(leaderboard)
        df = df.sort_values('score', ascending=False).head(10)
        st.markdown("### 🏆 Top 10 Leaderboard")
        st.dataframe(
            df,
            column_config={
                "name": "Player",
                "score": "Score",
                "date": "Date"
            },
            use_container_width=True
        )
    else:
        st.info("No scores yet. Be the first to take the quiz!")

def main():
    st.title("📝 Safety Knowledge Test")
    st.markdown("### Test your knowledge about disaster safety!")

    # Initialize session state
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
    if 'quiz_completed' not in st.session_state:
        st.session_state.quiz_completed = False
    if 'selected_answer' not in st.session_state:
        st.session_state.selected_answer = None

    # Start quiz button
    if not st.session_state.quiz_started:
        st.markdown("### Choose a disaster type to test your knowledge:")
        disaster_type = st.selectbox(
            "Select disaster type:",
            ["earthquake", "fire", "tornado"]
        )
        if st.button("Start Quiz"):
            st.session_state.questions = quiz_questions[disaster_type]
            random.shuffle(st.session_state.questions)
            st.session_state.quiz_started = True
            st.session_state.selected_answer = None
            st.rerun()

    # Display quiz
    elif not st.session_state.quiz_completed:
        question = st.session_state.questions[st.session_state.current_question]
        
        with st.container():
            st.markdown(f"### Question {st.session_state.current_question + 1} of {len(st.session_state.questions)}")
            st.markdown(f"**{question['question']}**")
            
            # Modified radio button implementation
            answer = st.radio(
                "Choose your answer:",
                question['options'],
                key=f"q_{st.session_state.current_question}",
                index=None  # This ensures no option is pre-selected
            )
            
            submit_button = st.button("Submit Answer")
            
            if submit_button:
                if answer is None:
                    st.warning("Please select an answer before submitting!")
                else:
                    if question['options'].index(answer) == question['correct']:
                        st.success("Correct! 🎉")
                        st.session_state.score += 1
                    else:
                        st.error(f"Wrong! The correct answer was: {question['options'][question['correct']]}")
                    
                    if st.session_state.current_question < len(st.session_state.questions) - 1:
                        st.session_state.current_question += 1
                        st.session_state.selected_answer = None
                        st.rerun()
                    else:
                        st.session_state.quiz_completed = True
                        st.rerun()

    # Show results and update leaderboard
    else:
        final_score = st.session_state.score
        total_questions = len(st.session_state.questions)
        percentage = (final_score / total_questions) * 100

        st.markdown(f"### Quiz Completed! 🎉")
        st.markdown(f"Your score: {final_score}/{total_questions} ({percentage:.1f}%)")

        # Save score to leaderboard
        name = st.text_input("Enter your name to save your score:")
        if name and st.button("Save Score to Leaderboard"):
            leaderboard = load_leaderboard()
            leaderboard.append({
                "name": name,
                "score": final_score,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            save_leaderboard(leaderboard)
            st.success("Score saved!")

        # Display leaderboard
        leaderboard = load_leaderboard()
        display_leaderboard(leaderboard)

        # Restart quiz button
        if st.button("Take Another Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.quiz_started = False
            st.session_state.quiz_completed = False
            st.session_state.selected_answer = None
            st.rerun()

if __name__ == "__main__":
    main()