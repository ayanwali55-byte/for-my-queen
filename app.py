import streamlit as st
import random
import time

# Page Config
st.set_page_config(page_title="A Special Message", page_icon="❤️")

# Initializing session state to track progress
if 'stage' not in st.session_state:
    st.session_state.stage = 0

def next_stage():
    st.session_state.stage += 1

# --- STAGE 0: The Intro ---
if st.session_state.stage == 0:
    st.title("Hey Beautiful... ❤️")
    st.write("I made something small for you. I hope it makes you smile.")
    if st.button("Click to see what it is"):
        next_stage()

# --- STAGE 1: The "Funny" Game ---
elif st.session_state.stage == 1:
    st.title("First, a quick test!")
    st.write("Do you love me more than pizza? 🍕")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes, absolutely!"):
            st.balloons()
            time.sleep(1)
            next_stage()
            
    with col2:
        # The "Running" No Button
        # In a real web app, we'd use JS, but here we can make it "disappear" or move
        no_clicked = st.button("No way.")
        if no_clicked:
            st.warning("Error 404: Button not found. Try the other one! 😉")

# --- STAGE 2: The Proposal ---
elif st.session_state.stage == 2:
    st.title("Okay, serious question now... 💍")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpbmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/L4lvBpHWkARu8/giphy.gif")
    
    st.subheader("You make every day better just by being in it.")
    st.write("Will you be my forever person?")

    # The Final Interaction
    if st.button("YES! ❤️"):
        st.snow()
        st.header("YAY! I'm the luckiest person alive! 🥂")
        st.confetti = True # Visual flair
    
    if st.button("I'll think about it... (Just kidding, click Yes)"):
        st.write("Nice try! The 'Yes' button is right there!")
