import streamlit as st
import openai as OpenAI

client = OpenAI(api_key = st.secrets["OPENAI_API_KEY"])