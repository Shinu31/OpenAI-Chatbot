#pip install openai streamlit python-dotenv
from openai import OpenAI
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.markdown("<h1 style='text-align: center; color: #000000 ; font-size: 48px;'>ChatGPT lite</h1>", unsafe_allow_html=True)
# Decorated Subtitle
st.markdown("<h3 style='text-align: center; color: #708090; font-size: 24px;'>Your Friendly Digital Companion!</h3>", unsafe_allow_html=True)

client = OpenAI(api_key=OPENAI_API_KEY)

if "openai_model" not in st.session_state:

    st.session_state["openai_model"] = "gpt-4o-mini"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Message ChatGPT lite"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
   
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})#pip install openai streamlit python-dotenv
