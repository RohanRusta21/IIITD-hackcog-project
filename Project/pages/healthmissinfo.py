import streamlit as st
import json
from streamlit_lottie import st_lottie
import preprocessor as pp
import sentiment_analyser as sa
import pandas as pd
import matplotlib.pyplot as plt
# st.set_page_config(page_title="my hackathon project",layout="wide")
# st.set_page_config(
    # page_title="cyberbullying"

st.sidebar.success("select a page")

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
lottie_variable9=load_lottiefile("9.json")   
lottie_variable10=load_lottiefile("10.json")  
lottie_variable11=load_lottiefile("11.json")  
lottie_variable12=load_lottiefile("12.json")   

#header
st.title("EXPRESSION EXCAVATOR protects you from health misinformation")
st.subheader("Health misinformation refers to the spread of inaccurate, misleading, or false information related to health, medical conditions, treatments, and wellness. This type of misinformation can be harmful as it can lead individuals to make decisions about their health based on incorrect or unverified information. Health misinformation can be spread through various channels, including social media,")
st.write("##")
# st.write("we are passionate coders")
# st.write("[click here to redirect to a link](paste any youtube link here)")

user_list=[]
global df1
df1=pd.DataFrame()
with st.container():
    st_lottie(lottie_variable9,height=400,key="catu9") 
    st.write("##")
    st.title("A STEP FORWARD FOR A SAFER TOMORROW")
with st.container():
    st.write("---")
    st.subheader("sample text")
    #file to be added here

with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with right_column:
        st.header("UPLOAD CHAT/TEXT TO BE ANALYZED")
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
        st_lottie(lottie_variable10,height=400,key="catu10")              
global selected_user
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("ENTER NAME OF THE USER")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("Type name of user-")
        for i in range(len(user_list)):
            st.write(i+1,")",user_list[i])
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
         st_lottie(lottie_variable11,height=500,key="catu11")    



with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("CONCLUSIONS DERIVED VIA GRAPH")
        st.write("##")
        st.write("##")
        st.write("##")

        st.write('''DESCRIPTION OF GRAPH '''
                 )
        if st.button("SHOW GRAPH"):
            graph()
        

with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with right_column:
        st.header("MOST USED WORDS")
        st.write("##")
        st.write("##")
        st.write("##")

        st.write('''Word Cloud '''
                 )
        if st.button("SHOW WORD CLOUD"):
            df_wc = sa.create_wordcloud(selected_user)
            fig,ax = plt.subplots()
            ax.imshow(df_wc)
            st.pyplot(fig)
        

