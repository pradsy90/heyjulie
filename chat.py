import os
import openai
import streamlit as st

def return_answer(prompt):
    print("Somebody clicked answer... so answering")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if(len(str(openai.api_key))>5):
        print("Found it")

    #answers = openai.ChatCompletion.create(
    #    model="gpt-3.5-turbo",
    #    temperature=0.8,
    #    max_tokens=200,
    #    messages=[
    #        #{"role": "user", "content": "Suggest less famous beaches with clear blue waters."}
    #        {"role":"user", "content":question}
    #   ])
    #st.session_state["answers"]="Hello, how do you do?"
    st.session_state["chatquestion"]=prompt
    print ("Trying to answer question --- " + prompt)
    answers = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=200,
        messages=[
            {"role":"user", "content":prompt}
        ]
    )["choices"][0]["message"]["content"]
    print (type(answers))
    print (answers)
    #st.session_state["chatanswer"]=answers
    #print (st.session_state["chatanswer"])
    return answers