import streamlit as st
import time
import random

# Page Config
st.set_page_config(page_title="A Night for Us ❤️", page_icon="🌙")

# Custom CSS for a romantic aesthetic
st.markdown("""
    <style>
    .main {
        background-color: #fff0f3;
    }
    .stButton>button {
        background-color: #ff4d6d;
        color: white;
        border-radius: 20px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #c9184a;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

if 'stage' not in st.session_state:
    st.session_state.stage = 0

# --- STAGE 0: THE TEASE ---
if st.session_state.stage == 0:
    st.title("Hey Mommy... ❤️")
    st.subheader("I've been thinking about you all day.")
    st.write("I have a special plan for tonight, but you have to unlock it first.")
    if st.button("Unlock my heart 🔓"):
        st.session_state.stage = 1
        st.rerun()

# --- STAGE 1: THE ROMANTIC GAME (SCRATCH CARD) ---
elif st.session_state.stage == 1:
    st.title("The Mystery Date Game 🎲")
    st.write("Pick a 'Mystery Card' to see what's in store for us tonight:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Card 1 💌"):
            st.info("A night full of endless cuddles and your favorite movie.")
    with col2:
        if st.button("Card 2 🍷"):
            st.info("Slow dancing in the kitchen with a glass of wine.")
    with col3:
        if st.button("Card 3 🔥"):
            st.info("A very special, long massage followed by 'us' time.")

    st.write("---")
    if st.button("I want all of them! 😍"):
        st.session_state.stage = 2
        st.rerun()

# --- STAGE 2: THE PICK-UP LINE GENERATOR ---
elif st.session_state.stage == 2:
    st.title("A Little Something for You... ✨")
    
    lines = [
        "Are you a magician? Because whenever I look at you, everyone else disappears.",
        "Your hand looks heavy—can I hold it for you tonight?",
        "I was going to wait for a star to fall to make a wish, but then I remembered I have you.",
        "If you were a library book, I’d never return you."
    ]
    
    if st.button("Click for a sweet thought 💭"):
        st.header(random.choice(lines))
    
    if st.button("Final Surprise... 🌹"):
        st.session_state.stage = 3
        st.rerun()

# --- STAGE 3: THE PROPOSAL & DATE INVITE ---
elif st.session_state.stage == 3:
    st.balloons()
    st.title("Tonight is all about YOU. ❤️")
    st.write("I've got the mood set, the snacks ready, and my heart waiting.")
    
    st.subheader("Will you give me the honor of a perfect night together, Bhondu?")
    
    if st.button("YES, I'm all yours! 🥰"):
        st.snow()
        st.success("Counting down the minutes until I see you! ❤️🔥")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJpbmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l4pTdcifPKUYMlV1S/giphy.gif")
