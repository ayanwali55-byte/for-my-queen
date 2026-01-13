import streamlit as st
import time
from datetime import datetime

# Page setup
st.set_page_config(page_title="Special Invite for Bhondu", page_icon="💌")

# Initialize session state
if 'stage' not in st.session_state:
    st.session_state.stage = 0

def move_to_next():
    st.session_state.stage += 1

# --- STAGE 0: THE DATE INVITE ---
if st.session_state.stage == 0:
    st.title("Hey Bhondu! ❤️")
    st.subheader("I've been thinking... we need more memories together.")
    st.write("I've planned a little journey for you here. Are you ready?")
    
    if st.button("Let's Go! 🚀"):
        move_to_next()

# --- STAGE 1: PLAN THE DATE ---
elif st.session_state.stage == 1:
    st.title("Step 1: The Plan 🍕")
    st.write("Pick our next adventure:")
    
    date_type = st.selectbox("Where are we going?", 
                             ["Romantic Dinner 🕯️", "Late Night Drive 🚗", "Movie & Popcorn 🍿", "Street Food Crawl 🥘"])
    
    st.write("And what time should I pick you up?")
    pick_up_time = st.time_input("Select a time", value=datetime.now())
    
    if st.button("Lock the Date! ✅"):
        st.session_state.date_choice = date_type
        st.session_state.time_choice = pick_up_time.strftime("%I:%M %p")
        st.success(f"Great! {date_type} at {st.session_state.time_choice} is locked in!")
        time.sleep(1.5)
        move_to_next()

# --- STAGE 2: THE COUNTDOWN GAME ---
elif st.session_state.stage == 2:
    st.title("Step 2: The Excitement Meter ⏳")
    st.write("How excited are you for this date?")
    
    excitement = st.slider("Move the bar to 100%!", 0, 100, 50)
    
    if excitement < 100:
        st.warning("Higher, Bhondu! Move it to the max! 😤")
    else:
        st.success("THAT'S WHAT I LIKE TO SEE!")
        if st.button("Unlock Final Surprise 🔓"):
            # A fake countdown for dramatic effect
            with st.empty():
                for seconds in range(3, 0, -1):
                    st.header(f"Loading Love in... {seconds}")
                    time.sleep(1)
                st.write("READY!")
            move_to_next()

# --- STAGE 3: THE PROPOSAL ---
elif st.session_state.stage == 3:
    st.balloons()
    st.title("To my dearest Bhondu... ❤️")
    st.markdown(f"""
    So, we have a **{st.session_state.date_choice}** planned for **{st.session_state.time_choice}**. 
    But there's one more thing I need to ask you...
    """)
    
    st.header("Will you be mine forever? 💍")
    
    col_yes, col_no = st.columns(2)
    
    with col_yes:
        if st.button("YES! ❤️"):
            st.snow()
            st.header("I love you, Bhondu! 🥰")
            st.subheader("See you on our date! 🥂")
            
    with col_no:
        if st.button("No (Button broken) 😜"):
            st.error("This button is for decoration only. Please click the Yes button!")
