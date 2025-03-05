#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icons="★")
st.title("Growth Mindset Challenge: Web App with Streamlit ")

st.header("🚀 Welcome to Your Growth Journey")
st.write("Embrace challenge, learn from mistakes,and unlock your full potential.This AI-powered app helps you builda growth mindset with reflection.challenges,and achievement! 💐 ")

#quote section
st.header("🌟 Today's Growth Mindset Quotes")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.")

st.header("⚒️ What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f"💪 You re facing: {user_input}.keep pushing forward towards your goals! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")   

#reflexing
st.header(" Reflect on Your Learning") 
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f" 💠Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! share your difficulties") 

#acheivements
st.header("🏆 celebrate Your Wins!")
acheivment = st.text_input("Share something you've recently accomplished:")


if acheivment:
    st.success(f"🎉 Amazing! you achieved: {acheivment}")
else:
    st.info("Big or small, every acheivment counts! share one now 😍")  



#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟 ")
st.write("**Ⓒ created by Jackson Chohan**")      