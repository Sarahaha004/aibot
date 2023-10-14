import streamlit as st
from embedchain import App
import os
from api import getkey
import pandas as pd

os.environ['OPENAI_API_KEY']= getkey()
app = App()
st.title("Health Assistant Bot")

choice=st.sidebar.selectbox("Choose your choice",("Keto","Vegan"))
if choice=='Keto':
    file_path="dietbot\Data\keto.csv"
    data=pd.read_csv(file_path)
    st.header(choice)

elif choice =='Vegan':
    file_path="dietbot\Data\vegan.csv"
    data=pd.read_csv(file_path)
    st.header(choice)

else:
    pass

st.sidebar.dataframe(data.sample(10))

app.add(file_path,data_type="csv")

prompt = st.text_input("Enter your query")
if prompt:
    with st.spinner("Generating..."):
        
        response = app.query(prompt)
        st.write(response)