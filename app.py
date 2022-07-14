import streamlit as st
from bbquote852.api_request import get_quote

st.write('Hello Batch 852!')

number = st.number_input('Insert a number')

st.write('The current number is ', number)

st.write(get_quote())
