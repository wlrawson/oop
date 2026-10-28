import streamlit as st
from PIL import Image

col1, col2 = st.columns(2)

with col1:
    st.title("Will Rawson")
    st.header("Cyber Security major at JBU")
    st.text("From Las Cruces, NM")

with col2:
    image = Image.open("python_image.jpg")
    st.image(image, width=200)

st.markdown("About Me")
st.text("I am planning to graduate in the spring of 2030")
st.divider ()

st.markdown("Qualifications")
st.text("N/A")
st.divider ()

st.markdown("Skills")
st.text("Have experience with Python, HTML, Java, CSS and javascript")
st.text("experience working with computers professionally")
st.divider ()

st.markdown("Work experience")
st.text("Building Supply Company, general computer work, and computer diagnosis")
st.text("Building Supply Company, property maintenance and property management")

st.markdown("Contact Information")
st.text("Phone number - 123-456-7890")
st.text("Email address - example@gmail.com")

st.markdown("Contact Me!")
userName = st.text_input("Your Name")
userEmail = st.text_input("Your Email")
userMessage = st.text_input("Your Message")
st.button("Send Message")


