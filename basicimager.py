import streamlit as st
import openai
import os

from openai import InvalidRequestError

import imagegen

try:
    #Initialize state variable
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if "imageurl" not in st.session_state:
        st.session_state["imageurl"] = "https://static.streamlit.io/examples/cat.jpg"

    if "imagedescn" not in st.session_state:
        st.session_state["imagedescn"]="<What would you like me to draw?>"

    st.header(":blue[Pictionary Anyone?] :frame_with_picture:")
    input_text = st.text_area(label='Mr.Da Vinci at your service...What picture would you like:', value=st.session_state["imagedescn"], height=50)

    st.button(
        "Generate",
        on_click=imagegen.genimage(input_text),
        kwargs={"prompt": input_text},
    )
    st.image(st.session_state["imageurl"], width=256)

except  InvalidRequestError:
    print("That's an invalid request")
    st.session_state["imagedescn"]="That was a duh request...Bruh!"

except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


