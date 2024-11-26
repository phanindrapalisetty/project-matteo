#%%
import streamlit as st 
import os 
import requests 
import json 
from dotenv import load_dotenv
import os
from src.models import return_calculator

# Access the variables
project_name = os.getenv("PROJECT_NAME")

# Function to create a synchronized slider and text box
def synced_input(label, min_value, max_value, default_value, key_prefix, step):
    """
    Creates a slider and text box that are synchronized.

    Parameters:
        - label: The label for the input fields.
        - min_value: Minimum value for the slider.
        - max_value: Maximum value for the slider.
        - default_value: Default value for both inputs.
        - key_prefix: Unique key prefix to ensure separate session states.

    Returns:
        - The current value of the input (shared by slider and text box).
    """

    slider_key = f"{key_prefix}_slider"
    numeric_key = f"{key_prefix}_text"

    # Initialize session state for the shared value
    if slider_key not in st.session_state:
        st.session_state[slider_key] = default_value
        st.session_state[numeric_key] = default_value

    # Update functions
    def update_from_text():
        try:
            value = int(st.session_state[numeric_key])
            value = max(min(value, max_value), min_value)  # Clamp within range
            st.session_state[slider_key] = value
        except ValueError:
            st.error(f"Please enter a valid number for {label}")

    def update_from_slider():
        st.session_state[numeric_key] = st.session_state[slider_key]

    # Layout: Text Input beside Label and Slider below
    with st.container():
        st.markdown(f"#### {label}")  # Display label
        cols = st.columns([3, 1])  # Adjust column widths
        # cols[0].markdown(f"## {label}")  # Display label
        cols[0].slider(
        f"{label} (Slider):",
        min_value=min_value,
        max_value=max_value,
        key=slider_key,
        on_change=update_from_slider,
        step = step, 
        label_visibility='hidden'
    )
        cols[1].number_input(
        f"{label}",
        key=numeric_key,
        on_change=update_from_text,
        min_value=min_value,
        max_value=max_value,
        step=step,
        label_visibility='hidden'
    )

    # Return the current value
    return st.session_state[slider_key]

def main():
    st.set_page_config(
        page_title= project_name,
        page_icon=":whale:",
        initial_sidebar_state="auto"
        ) 
    
    st.title(project_name)

    col1, col2 = st.columns([3, 2])

    with col1:
        interest_rate  = synced_input(label = "Annual Return Rate", min_value=1e-9, max_value=50.0, default_value = 12.0, key_prefix='interest_rate', step=0.1)
    
        principal_amount = synced_input(label = 'Monthly Investment', min_value = 100, max_value=400000, default_value = 25000, key_prefix = 'principal_amount', step=100)
        
        st.markdown(f"#### Tenure in Years/Months")  # Display label
        
        ucol1, ucol2 = st.columns(2)

        with ucol1:
            frequency_of_tenure = st.radio(label = 'frequency_of_tenure',
                                options = ["Years", "Months"],
                                horizontal=True,
                                index=None,
                                label_visibility='hidden'
                                )
        
        with ucol2:
            # st.write(frequency_of_tenure)
            if frequency_of_tenure == 'Years':
                tenure_max_value = 30
                tenure = st.number_input(label='Tenure', min_value=1, max_value=tenure_max_value, key = 'tenure', label_visibility='hidden')
            elif frequency_of_tenure == 'Months':
                tenure_max_value = 30*12
                tenure = st.number_input(label='Tenure', min_value=12, max_value=tenure_max_value, key = 'tenure', label_visibility='hidden')
            else:
                tenure = None
                # st.write(tenure)

        tenure_in_months = tenure*12 if frequency_of_tenure == 'Years' else tenure
    
    with col2:
        st.markdown('### Split of Earnings')

        if interest_rate and principal_amount and frequency_of_tenure:
            sip = return_calculator.SIPCalculator(monthly_amount=principal_amount, annual_return=interest_rate, tenure_in_months=tenure_in_months)
            st.write(sip.get_return_amount())
        else:
            st.write('Please select inputs')

    

if __name__ == '__main__':
    main()