import streamlit as st
import os
import time 
from src.update_database import *

print("Test")
st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state['messages'] = []
    st.session_state['first_message'] = False
    st.session_state['second_message'] = False
    st.session_state['final_message'] = False

# Display existing messages
for msg in st.session_state['messages']:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input(placeholder= "")

if (st.session_state['first_message'] == False):
    response = "Why did you change the scheduled employee?"
    st.chat_message("assistant").write(response)
    st.session_state['messages'].append({"role": "assistant", "content": response})
    st.session_state['first_message'] = True

elif (st.session_state['second_message'] == False):
    if prompt:
        os.system('clear')
        st.chat_message("user").write(prompt)
        st.session_state['messages'].append({"role": "user", "content": prompt})

        prompt=prompt.replace("'", "")
        txt=st.session_state['messages'][0]['content']
        print("test")
        print(f"Updating db with {txt} and {prompt}")
        update_database(txt1=txt, txt2=prompt)
        pass
        time.sleep(2) # Sleep for 3 seconds
        response = "Is there anything else I should know about why you changed the employee's schedule that will help me make a better assignment in the future?"
        st.session_state['messages'].append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
        st.session_state['second_message'] = True
        

elif ( st.session_state['final_message']== False):
    if prompt:
        os.system('clear')
        st.chat_message("user").write(prompt)
        st.session_state['messages'].append({"role": "user", "content": prompt})
        time.sleep(2) # Sleep for 3 seconds

        response = "Thank you for your feedback."
        st.session_state['messages'].append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

        st.session_state['final_message'] = True
        prompt=prompt.replace("'", "")
        txt=st.session_state['messages'][2]['content'].replace("'", "")
        print(f"Updating db with {txt} and {prompt}")
        update_database(txt1=txt, txt2=prompt)
        pass
