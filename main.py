import streamlit as st
from datetime import datetime
import time

# Set page config
st.set_page_config(page_title="Countdown Timer", layout="wide")

# Style for countdown and title (timer moved up by reducing height to 45vh)
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 20vh;
        font-size: 48px;
        font-weight: bold;
    }
    .title {
        text-align: center;
        font-size: 64px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title (centered with HTML)
st.markdown("<div class='title'>⏳ Countdown to May 10th, 2025 @ 12:30 AM</div>", unsafe_allow_html=True)

# Center the image using Streamlit columns
left, center, right = st.columns([2, 2, 1])  # Center column is wider
with center:
    st.image("https://i.postimg.cc/C1pBRPqJ/IMG-9590.jpg", width=300)

# Set target date
target_date = datetime(2025, 5, 10, 0, 30, 0)

# Placeholder for the countdown
countdown_placeholder = st.empty()

# Live countdown loop
while True:
    now = datetime.now()
    remaining = target_date - now

    if remaining.total_seconds() <= 0:
        countdown_placeholder.markdown("<div class='centered'>🎉 Countdown complete!</div>", unsafe_allow_html=True)
        break

    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    countdown_text = f"{days}d {hours}h {minutes}m {seconds}s"
    countdown_placeholder.markdown(f"<div class='centered'>{countdown_text}</div>", unsafe_allow_html=True)

    time.sleep(1)
import streamlit as st
from datetime import datetime
import time

# Set page config
st.set_page_config(page_title="Countdown Timer", layout="wide")

# Style for countdown and title (timer moved up by reducing height to 45vh)
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 45vh;
        font-size: 48px;
        font-weight: bold;
    }
    .title {
        text-align: center;
        font-size: 64px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title (centered with HTML)
st.markdown("<div class='title'>⏳ Countdown to May 10th, 2025 @ 12:30 AM</div>", unsafe_allow_html=True)

# Center the image using Streamlit columns
left, center, right = st.columns([2, 2, 1])  # Center column is wider
with center:
    st.image("IMG_9590.JPEG", width=300)

# Set target date
target_date = datetime(2025, 5, 10, 0, 30, 0)

# Placeholder for the countdown
countdown_placeholder = st.empty()

# Live countdown loop
while True:
    now = datetime.now()
    remaining = target_date - now

    if remaining.total_seconds() <= 0:
        countdown_placeholder.markdown("<div class='centered'>🎉 Countdown complete!</div>", unsafe_allow_html=True)
        break

    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    countdown_text = f"{days}d {hours}h {minutes}m {seconds}s"
    countdown_placeholder.markdown(f"<div class='centered'>{countdown_text}</div>", unsafe_allow_html=True)

    time.sleep(1)