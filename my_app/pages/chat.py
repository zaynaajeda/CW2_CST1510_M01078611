import streamlit as st
from openai import OpenAI

#Initialise OpenAI client
client = OpenAI(api_key = st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role":"system", "content":"You are a helpful assistant."}
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append(
        {"role":"user", "content":user_input}
    )

    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = st.session_state.messages,
        stream = True
    )
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content

                full_response += content

                message_placeholder.markdown(full_response + " ")
