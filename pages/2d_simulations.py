import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Page configuration
st.set_page_config(
    page_title="2D Safety Simulator",
    page_icon="🏃",
    layout="wide"
)

def check_collision(person_pos, zone_pos, threshold=0.5):
    """Check if person is within threshold distance of a zone"""
    return abs(person_pos[0] - zone_pos[0]) < threshold and abs(person_pos[1] - zone_pos[1]) < threshold

def create_classroom_scene(person_position, safe_zones, hazards, scenario):
    """Create a 2D classroom scene with interactive elements"""
    fig = go.Figure()

    # Room boundaries
    room_width = 10
    room_height = 8

    # Draw room walls
    fig.add_trace(go.Scatter(
        x=[0, room_width, room_width, 0, 0],
        y=[0, 0, room_height, room_height, 0],
        mode='lines',
        name='Walls',
        line=dict(color='black', width=2)
    ))

    # Add furniture based on scenario
    if scenario in ['earthquake', 'tornado']:
        # Desks for shelter
        desks = [
            ([2, 3, 3, 2, 2], [2, 2, 3, 3, 2]),
            ([6, 7, 7, 6, 6], [2, 2, 3, 3, 2]),
            ([4, 6, 6, 4, 4], [6, 6, 7, 7, 6])
        ]
        for i, (x, y) in enumerate(desks):
            fig.add_trace(go.Scatter(
                x=x, y=y,
                mode='lines',
                fill='toself',
                name=f'Desk {i+1}',
                fillcolor='rgb(139,69,19)',
                line=dict(color='rgb(139,69,19)')
            ))

    elif scenario == 'fire':
        # Exits and windows
        exits = [
            # Main door
            dict(x=[4.5, 5.5], y=[0, 0], name='Main Exit'),
            # Emergency exits
            dict(x=[0, 0], y=[3, 4], name='Emergency Exit 1'),
            dict(x=[10, 10], y=[3, 4], name='Emergency Exit 2')
        ]
        for exit_door in exits:
            fig.add_trace(go.Scatter(
                x=exit_door['x'],
                y=exit_door['y'],
                mode='lines',
                name=exit_door['name'],
                line=dict(color='rgb(0,255,0)', width=5)
            ))

    # Add person with current status color
    person_in_hazard = any(check_collision(person_position, hazard) for hazard in hazards)
    person_in_safe = any(check_collision(person_position, safe) for safe in safe_zones)
    
    person_color = 'rgb(255,0,0)' if person_in_hazard else 'rgb(0,255,0)' if person_in_safe else 'rgb(0,0,255)'
    
    fig.add_trace(go.Scatter(
        x=[person_position[0]],
        y=[person_position[1]],
        mode='markers+text',
        name='You',
        marker=dict(size=20, symbol='circle', color=person_color),
        text=['👤'],
        textposition='top center'
    ))

    # Add hazards with specific icons based on scenario
    hazard_icons = {
        'earthquake': '🏚️',
        'fire': '🔥',
        'tornado': '🌪️'
    }
    
    for hazard in hazards:
        fig.add_trace(go.Scatter(
            x=[hazard[0]],
            y=[hazard[1]],
            mode='markers+text',
            name='Hazard',
            marker=dict(size=25, symbol='x', color='rgb(255,0,0)'),
            text=[hazard_icons.get(scenario, '⚠️')],
            textposition='top center'
        ))

    # Add safe zones with specific icons
    safe_icons = {
        'earthquake': '🏗️',
        'fire': '🚪',
        'tornado': '🏢'
    }
    
    for zone in safe_zones:
        fig.add_trace(go.Scatter(
            x=[zone[0]],
            y=[zone[1]],
            mode='markers+text',
            name='Safe Zone',
            marker=dict(size=25, symbol='circle', color='rgb(0,255,0)'),
            text=[safe_icons.get(scenario, '✅')],
            textposition='top center'
        ))

    # Update layout
    fig.update_layout(
        title=f"2D Safety Simulator - {scenario.title()} Scenario",
        xaxis=dict(range=[-1, room_width + 1], showgrid=False),
        yaxis=dict(range=[-1, room_height + 1], showgrid=False),
        height=600,
        showlegend=True,
        plot_bgcolor='white'
    )

    return fig, person_in_hazard, person_in_safe

def main():
    st.title("🏃 2D Safety Simulator")
    st.markdown("### Learn how to stay safe in different emergency situations!")

    # Scenario definitions
    scenarios = {
        "earthquake": {
            "safe_zones": [(2.5, 2.5), (6.5, 2.5)],  # Under desks
            "hazards": [(8, 7), (2, 7)],  # Falling objects
            "instructions": """
            ### Earthquake Safety Instructions:
            1. DROP to the ground
            2. COVER under a sturdy desk
            3. HOLD ON until shaking stops
            4. Stay away from windows and tall furniture
            """
        },
        "fire": {
            "safe_zones": [(5, 0), (0, 3.5), (10, 3.5)],  # Exits
            "hazards": [(7, 7), (3, 6), (8, 3)],  # Fire spots
            "instructions": """
            ### Fire Safety Instructions:
            1. Stay low to avoid smoke
            2. Use nearest exit
            3. Don't use elevators
            4. Meet at assembly point
            """
        },
        "tornado": {
            "safe_zones": [(2.5, 2.5), (6.5, 2.5)],  # Interior rooms
            "hazards": [(0, 3.5), (10, 3.5)],  # Windows
            "instructions": """
            ### Tornado Safety Instructions:
            1. Go to lowest floor
            2. Stay away from windows
            3. Get under sturdy furniture
            4. Cover your head
            """
        }
    }

    # Select scenario
    scenario = st.selectbox(
        "Choose a Scenario:",
        list(scenarios.keys())
    )

    # Initialize session state
    if 'person_position' not in st.session_state:
        st.session_state.person_position = [5, 4]
    if 'game_status' not in st.session_state:
        st.session_state.game_status = "active"

    # Movement controls and display
    col1, col2 = st.columns([3, 1])
    
    with col1:
        fig, in_hazard, in_safe = create_classroom_scene(
            st.session_state.person_position,
            scenarios[scenario]["safe_zones"],
            scenarios[scenario]["hazards"],
            scenario
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### Controls")
        move_distance = 0.5
        
        # Movement buttons with keyboard-like layout
        _, up, _ = st.columns(3)
        left, down, right = st.columns(3)
        
        with up:
            if st.button("⬆️"):
                st.session_state.person_position[1] += move_distance
        with left:
            if st.button("⬅️"):
                st.session_state.person_position[0] -= move_distance
        with down:
            if st.button("⬇️"):
                st.session_state.person_position[1] -= move_distance
        with right:
            if st.button("➡️"):
                st.session_state.person_position[0] += move_distance

        # Status feedback
        if in_hazard:
            st.error("⚠️ DANGER! Move to a safe location!")
        elif in_safe:
            st.success("✅ You're in a safe position! Well done!")
        else:
            st.warning("🎯 Find a safe position!")

        # Display instructions
        st.markdown(scenarios[scenario]["instructions"])

    # Reset button
    if st.button("Reset Position"):
        st.session_state.person_position = [5, 4]
        st.session_state.game_status = "active"
        st.experimental_rerun()

if __name__ == "__main__":
    main()