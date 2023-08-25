import streamlit as st

def enter_words(input_words):
    file=open('emotions.txt','a')
    file.write(input_words)
    file.write('\n')

with st.container():
    st.write("Input emotions and words/phrases you want enter-")
    words=st.text_input("'Keywords/Phrases': 'Emotions'," )
    enter_words(words)