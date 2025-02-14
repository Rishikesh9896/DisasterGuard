import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils import load_css, display_card

# Page config
st.title("Interactive Simulations 🔬")
st.markdown("### Learn Through Fun Experiments!")

# Tabs for different simulations
tab1, tab2, tab3 = st.tabs(["Earthquake Simulator 🌋", "Hurricane Simulator 🌪️", "Tsunami Simulator 🌊"])

# Earthquake Simulator
with tab1:
    st.subheader("Earthquake Intensity Simulator")
    
    # Earthquake simulation controls
    intensity = st.slider("Select Earthquake Intensity (Richter Scale)", 1.0, 9.0, 5.0, 0.1)
    duration = st.slider("Duration (seconds)", 1, 30, 10)
    
    if st.button("Simulate Earthquake"):
        # Generate simulated earthquake data
        time = np.linspace(0, duration, 100)
        amplitude = np.sin(time) * intensity * np.random.random(100)
        
        # Create earthquake wave plot
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time, y=amplitude, mode='lines', name='Seismic Waves'))
        fig.update_layout(
            title="Simulated Earthquake Waves",
            xaxis_title="Time (seconds)",
            yaxis_title="Wave Amplitude",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Show impact information
        st.info(f"At magnitude {intensity}, this earthquake would:")
        if intensity < 4:
            st.write("- Be felt by few people")
            st.write("- Cause minimal damage")
        elif intensity < 6:
            st.write("- Be felt by most people")
            st.write("- Cause minor damage to buildings")
        else:
            st.write("- Be felt by everyone")
            st.write("- Cause significant damage to buildings")
            st.write("- Require immediate evacuation")

# Hurricane Simulator
with tab2:
    st.subheader("Hurricane Intensity Simulator 🌪️")
    
    # Simple hurricane intensity selection
    intensity = st.radio(
        "Select Hurricane Intensity Level:",
        ["Low", "Moderate", "High", "Extreme"],
        help="Choose the intensity level to see hurricane characteristics and safety measures"
    )
    
    if st.button("Show Hurricane Details"):
        # Create columns for organized display
        col1, col2 = st.columns(2)
        
        # Define hurricane characteristics based on intensity
        hurricane_info = {
            "Low": {
                "category": "Category 1",
                "wind_speed": "74-95 mph",
                "storm_surge": "4-5 feet",
                "color": "yellow",
                "temperature": "75-80°F",
                "precautions": [
                    "Stay indoors",
                    "Keep away from windows",
                    "Have emergency supplies ready",
                    "Monitor weather updates"
                ]
            },
            "Moderate": {
                "category": "Category 2-3",
                "wind_speed": "96-129 mph",
                "storm_surge": "6-12 feet",
                "color": "orange",
                "temperature": "80-85°F",
                "precautions": [
                    "Secure outdoor objects",
                    "Prepare for power outages",
                    "Fill vehicles with fuel",
                    "Have evacuation plan ready",
                    "Stock up on water and food"
                ]
            },
            "High": {
                "category": "Category 4",
                "wind_speed": "130-156 mph",
                "storm_surge": "13-18 feet",
                "color": "red",
                "temperature": "85-90°F",
                "precautions": [
                    "Follow evacuation orders",
                    "Secure all windows and doors",
                    "Expect long-term power outages",
                    "Prepare for severe flooding",
                    "Move to higher ground if needed"
                ]
            },
            "Extreme": {
                "category": "Category 5",
                "wind_speed": "157+ mph",
                "storm_surge": "19+ feet",
                "color": "purple",
                "temperature": ">90°F",
                "precautions": [
                    "IMMEDIATE EVACUATION REQUIRED",
                    "Catastrophic damage expected",
                    "Areas may be uninhabitable",
                    "Seek emergency shelter",
                    "Follow all official instructions"
                ]
            }
        }
        
        info = hurricane_info[intensity]
        
        # Display hurricane characteristics
        with col1:
            st.markdown(f"### Hurricane Characteristics")
            
            # Create gauge for wind speed
            max_speeds = {"Low": 95, "Moderate": 129, "High": 156, "Extreme": 200}
            min_speeds = {"Low": 74, "Moderate": 96, "High": 130, "Extreme": 157}
            
            fig = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = (min_speeds[intensity] + max_speeds[intensity]) / 2,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Wind Speed (mph)"},
                gauge = {
                    'axis': {'range': [0, 200]},
                    'bar': {'color': info['color']},
                    'steps': [
                        {'range': [0, 74], 'color': 'lightgray'},
                        {'range': [74, 95], 'color': 'yellow'},
                        {'range': [96, 129], 'color': 'orange'},
                        {'range': [130, 156], 'color': 'red'},
                        {'range': [157, 200], 'color': 'purple'}
                    ]
                }
            ))
            fig.update_layout(height=250)
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown(f"""
            - **Category**: {info['category']}
            - **Wind Speed**: {info['wind_speed']}
            - **Storm Surge**: {info['storm_surge']}
            - **Temperature**: {info['temperature']}
            """)
        
        # Display safety precautions
        with col2:
            st.markdown("### Safety Precautions")
            for precaution in info['precautions']:
                st.warning(precaution)
            
            # Add visual warning level
            st.markdown(f"""
            <div style='padding: 10px; background-color: {info['color']}; border-radius: 5px; text-align: center;'>
                <h3 style='color: white;'>WARNING LEVEL: {intensity.upper()}</h3>
            </div>
            """, unsafe_allow_html=True)

# Tsunami Simulator
with tab3:
    st.subheader("Tsunami Simulator 🌊")
    
    # Tsunami parameters
    st.markdown("### Tsunami Characteristics")
    
    # Select tsunami trigger
    trigger = st.selectbox(
        "What caused the tsunami?",
        ["Underwater Earthquake", "Volcanic Eruption", "Landslide"],
        help="Different events can trigger tsunamis with different characteristics"
    )
    
    # Distance from shore
    distance = st.slider(
        "Distance from Shore (km)",
        0, 1000, 500,
        help="Distance from the tsunami source to the shore"
    )
    
    # Depth of water
    depth = st.slider(
        "Ocean Depth (meters)",
        1000, 10000, 5000,
        help="Average depth of the ocean where tsunami is traveling"
    )

    if st.button("Simulate Tsunami"):
        # Calculate tsunami characteristics
        speed = round(np.sqrt(9.8 * depth) * 3.6, 2)  # Convert m/s to km/h
        
        # Estimated wave height based on trigger and distance
        base_height = {
            "Underwater Earthquake": 15,
            "Volcanic Eruption": 20,
            "Landslide": 10
        }
        
        # Wave height decreases with distance
        wave_height = round(base_height[trigger] * (1 - (distance/2000)), 1)
        wave_height = max(wave_height, 2)  # Minimum wave height
        
        # Estimated arrival time
        arrival_time = round(distance / speed, 2)  # hours
        
        # Create visualization
        col1, col2 = st.columns(2)
        
        with col1:
            # Speed gauge
            fig_speed = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = speed,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Wave Speed (km/h)"},
                gauge = {
                    'axis': {'range': [0, 1000]},
                    'bar': {'color': "blue"},
                    'steps': [
                        {'range': [0, 400], 'color': "lightblue"},
                        {'range': [400, 700], 'color': "royalblue"},
                        {'range': [700, 1000], 'color': "darkblue"}
                    ]
                }
            ))
            fig_speed.update_layout(height=250)
            st.plotly_chart(fig_speed, use_container_width=True)
            
            # Wave height gauge
            fig_height = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = wave_height,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Wave Height (meters)"},
                gauge = {
                    'axis': {'range': [0, 20]},
                    'bar': {'color': "cyan"},
                    'steps': [
                        {'range': [0, 5], 'color': "lightcyan"},
                        {'range': [5, 10], 'color': "turquoise"},
                        {'range': [10, 20], 'color': "teal"}
                    ]
                }
            ))
            fig_height.update_layout(height=250)
            st.plotly_chart(fig_height, use_container_width=True)

        with col2:
            st.markdown("### Tsunami Details")
            st.info(f"""
            #### Wave Characteristics:
            - Speed: {speed} km/h
            - Height: {wave_height} meters
            - Estimated Arrival Time: {arrival_time} hours
            
            #### Trigger: {trigger}
            - Distance from Shore: {distance} km
            - Ocean Depth: {depth} meters
            """)
            
            # Warning level based on wave height
            if wave_height < 5:
                warning_color = "yellow"
                warning_level = "MODERATE"
            elif wave_height < 10:
                warning_color = "orange"
                warning_level = "HIGH"
            else:
                warning_color = "red"
                warning_level = "EXTREME"
                
            st.markdown(f"""
            <div style='padding: 10px; background-color: {warning_color}; 
                        border-radius: 5px; text-align: center; margin: 10px 0;'>
                <h3 style='color: white;'>WARNING LEVEL: {warning_level}</h3>
            </div>
            """, unsafe_allow_html=True)

        # Safety precautions based on warning level
        st.markdown("### Safety Precautions")
        
        immediate_actions = {
            "yellow": [
                "Move to higher ground immediately",
                "Stay away from the beach",
                "Monitor official updates",
                "Prepare emergency kit"
            ],
            "orange": [
                "EVACUATE IMMEDIATELY to higher ground",
                "Take emergency supplies",
                "Follow evacuation routes",
                "Help others if possible",
                "Stay tuned to emergency broadcasts"
            ],
            "red": [
                "IMMEDIATE EVACUATION REQUIRED",
                "Move at least 2 miles inland or 100 feet above sea level",
                "Take only essential items",
                "Follow all official instructions",
                "Do not wait to observe the tsunami"
            ]
        }
        
        for action in immediate_actions[warning_color]:
            st.warning(action)
            
        # Additional information
        with st.expander("Important Tsunami Facts"):
            st.markdown("""
            ### Key Things to Remember:
            1. Natural Warning Signs:
                - Strong earthquake
                - Unusual ocean behavior
                - Loud roaring sound
                
            2. Tsunami Waves:
                - Come as a series, not just one wave
                - First wave may not be the largest
                - Can continue for hours
                
            3. After a Tsunami:
                - Wait for official "all clear"
                - Stay away from damaged areas
                - Help others if safe to do so
                
            4. Never:
                - Wait to see the tsunami
                - Return to the coast too soon
                - Go to the beach to watch
            """)

# Add helpful tips
with st.expander("How to Use the Simulations 🎯"):
    st.markdown("""
    ### Tips for Each Simulation:
    
    #### Earthquake Simulator 🌋
    - Adjust the intensity to see different earthquake strengths
    - Watch how the seismic waves change
    - Learn about safety measures for each intensity level
    
    #### Hurricane Simulator 🌪️
    - Select different intensity levels
    - Learn about wind speeds and storm surge
    - Understand safety precautions for each level
    
    #### Tsunami Simulator 🌊
    - Try different tsunami triggers
    - See how distance affects wave height and arrival time
    - Learn critical safety measures
    - Understand warning signs and evacuation procedures
    
    Remember to explore all features and learn from the simulations! 🌟
    """)