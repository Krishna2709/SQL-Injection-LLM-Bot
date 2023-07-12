import streamlit as st
from utils import get_answer


previous_response = st.experimental_get_query_params().get("previous_response", "")

if isinstance(previous_response, list):
    previous_response = ' '.join(previous_response)

st.sidebar.text_area("Previous Response:", value=previous_response, height=300, max_chars=None, key=None)


user_input = st.text_input("Enter your message:")

# Create a button to generate the response
if st.button("Generate Response"):

    response = get_answer(user_prompt=user_input)
    if isinstance(response, list):
        response = ' '.join(response)
    
    st.text_area("Response:", value=response, height=400, max_chars=None, key=None)
    st.experimental_set_query_params(previous_response=response)
