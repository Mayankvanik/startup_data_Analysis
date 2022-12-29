import streamlit as st
import pandas as pd
import time

st.title('startup dashboard')
st.header('I am Rider')
st.subheader('I Loving IT.')

st.write('Yahh')

st.markdown("""
### My Fav star Tom Cruise
-Mission Impossible 
""")

st.latex('x^2 + y^2 = 0')

df=pd.DataFrame({
    'name':['Mack','Megha'],
    'Marks':[78,88],
    'Profite':[98,99]
})
st.dataframe(df)

st.code("""
def inp(a):
    returen a*2
""")
st.metric('Revenu','Rs 55cr','3%')

st.json({
    'name':['Mack','Megha'],
    'Marks':[78,88],
    'Profite':[98,99]
})

st.image('01.jpg')

c1,c2=st.columns(2)
with c1:
    st.image('01.jpg')

with c2:
    st.image('01.jpg')

st.error('Login Error')
st.success('Login Error')
st.info('Login info')

bar=st.progress(0)

for i in range(0,101):
    time.sleep(0.05)
    bar.progress(i)

email = st.text_input('Enter Email')
password = st.text_input('Enter password')
gender=st.selectbox('select Gender',['male','female','other'])

btn=st.button('Login Here')

if btn:
    if email == '123@gmail.com' and password == '111':
        st.success('Done')
        st.balloons()
        st.write(gender)
    else:
        st.error('Enter Wrong')

import streamlit as st

file=st.file_uploader('upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())