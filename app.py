#streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", project_icon="★")

st_title("Growth Mindset Challenge: Web App with Streamlit")

st.header(" 💫 welcome to your growth journy!")
st.write("Embrace Challenges, Learn from Mistakes and unlock your full potential. this AI-powered app helps you build a growth minthset reflection, challenges and achievements 🌟")

#quote section
st.header(" Today's Growth mindset quote")
st.write("Failure is simply the opportunity to begin again, this time more intelligently." - Henry Ford )

st.header( "What's your challenge today?")
user_input = st.text_input("describe a challenge you're facinf:")

#conditions
if user.input:
    st.success(f"you are facing: {user.input}. keep pushing forward towards your goal!")
else:
    st.warning("tell us aboiut your challengue to get started")

#reflexing
st.header("reflect to your learning")
reflection = st.text_area("write your reflection here:")

if reflection: 
    st.success(f" great insight! your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! share your difficulties")


#acheivement
st.header("celebrate your Wins!")
acheivement = st.text_input("share something you've recently accomplished:")

if acheivement:
    st.success("😍 Amazing you achieved: {"achieved"}")
else:
    st.info("big or small every achievement counts! share one now 💐")

#footer
st.write(" -  -  -")
st.write("Believe in your capacity. Growth is a journy not a destination! ✷ ")
st.write("**✍ created by MADIHA**")

