import streamlit as st
import openai
import os
def genimage(prompt):
    st.session_state["imagedescn"]=prompt
    print("Somebody clicked generate image...so generating")
    print("generating image for " + st.session_state["imagedescn"] )
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Image.create(prompt=prompt, n=1, size="256x256")
    st.session_state["imageurl"]=(response["data"][0]["url"])
    print(response["data"][0]["url"])
