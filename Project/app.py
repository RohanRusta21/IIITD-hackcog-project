import streamlit as st
import json
from streamlit_lottie import st_lottie
import preprocessor as pp
import sentiment_analyser as sa
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title="my hackathon project",layout="wide")

def graph():
    s=sa.callcount()
    fig, ax1 = plt.subplots()
    ax1.bar(s.keys(), s.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    st.pyplot(fig)

def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
lottie_variable1=load_lottiefile("1.json")   
lottie_variable2=load_lottiefile("2.json")  
lottie_variable3=load_lottiefile("3.json")  
lottie_variable4=load_lottiefile("4.json")   


st.subheader("hello everyone")
st.title("we are working on AI")
st.write("we are passionate coders")
# st.write("[click here to redirect to a link](paste any youtube link here)")

user_list=[]
global df1
df1=pd.DataFrame()
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with right_column:
        st.header("COGNITIVE COMPUTIONG AND SOCIAL SENSING:FILE UPLOADING")
        st.write("##")
        st.write("##")
        st.write("##")

        file=st.file_uploader("upload your txt file here",type=["txt"])
        if st.button("process"):
            if file is not None:
                bytes_data = file.getvalue()
                data = bytes_data.decode("utf-8")
                df1 = pp.preprocess(data)
                user_list = df1['user'].unique().tolist()
                user_list.sort()
                df1.to_csv('temp.csv', index=False)

    with left_column:
        st_lottie(lottie_variable2,height=700,key="catu2")              
global selected_user
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("COGNITIVE COMPUTIONG AND SOCIAL SENSING:DROPDOWN MENU")
        st.write("##")
        st.write("##")
        st.write("##")
        selected_user = st.text_input("Enter Name-")
        df = pd.read_csv('temp.csv')
        filtered_data = df[df['user'] == selected_user]['message']
        print(selected_user)
        st.write('''DESCRIPTION OF ANALYSIS''')
        filtered_data = df[df['user'] == selected_user]['message']
        output_text_file = 'read.txt'
        with open(output_text_file, 'w', encoding='utf-8') as f:
                    for message in filtered_data:
                     f.write(message + '\n')
        st.write(sa.main2())
        st.write(sa.sentiment_analyze())
       
        with right_column:
         st_lottie(lottie_variable3,height=700,key="catu3")    



with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("COGNITIVE COMPUTIONG AND SOCIAL SENSING:GRAPH")
        st.write("##")
        st.write("##")
        st.write("##")

        st.write('''DESCRIPTION OF GRAPH '''
                 )
        if st.button("SHOW GRAPH"):
            graph()
    with right_column:
        st_lottie(lottie_variable1,height=700,key="catu")   
        