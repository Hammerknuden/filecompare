import streamlit as st
st.text('compare URL file names')
file_1 = st.text_input("indsæt file 1  HTTPS://  ")
file_2 = st.text_input("indsæt file 2  HTTPS://  ")

if file_1 == file_2:
    st.markdown("Files are identical  ")
else:
    st.markdown("Files are not identical")

