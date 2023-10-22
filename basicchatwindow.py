import streamlit as st
import openai
import os
from openai import InvalidRequestError
import chat
import recognizevoice
import multiprocessing

try:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    #Initialize state variable
    if "chatanswer" not in st.session_state:
        st.session_state["chatanswer"] = "<Answer>"
    if "chatquestion" not in st.session_state:
        st.session_state["chatquestion"] = "What day is it today?"

    #Title of the Application
    st.title(":blue[Ask a Question] :sunglasses: :+1: ")

    #Header of the Application
    st.header(":blue[Q&A Anyone?] :question:")
    input_text = st.text_area(label='What be y''er question? Arrgh?', value=st.session_state["chatquestion"], height=150)

    st.button(
        "Answer",
        on_click=chat.return_answer(input_text),
        kwargs={"prompt": input_text},
    )
    output_text = st.text_area(label='Answer:',value=st.session_state["chatanswer"], height=250)



except  InvalidRequestError:
    st.session_state["chatquestion"]="That was a duh question"
    st.session_state["chatanswer"] = "It deserved a duh answer"
    print("That's an invalid request")
except  Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise