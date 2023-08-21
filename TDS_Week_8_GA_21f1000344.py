# importing libraries
import streamlit as st

st.title('Find the largest among the 3 given numbers.')

# getting input from user
col1, col2, col3 = st.columns([1,1,1])
with col1:
    num1 = st.number_input("Number 1")
with col2:
    num2 = st.number_input("Number 2")
with col3:
    num3 = st.number_input("Number 3")

# Finding the largest of three given number
ans = 0
if num1 > num2:
    if num1 > num3:
        ans = num1
    else:
        ans = num3
else:
    if num2 > num3:
        ans = num2
    else:
        ans = num3

# showing results
st.markdown(f'### Largest number is {ans}')