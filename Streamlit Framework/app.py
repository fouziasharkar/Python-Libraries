import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('Fouzia is enjoing it.')

st.write('Hello Hi Bye Bye')

st.markdown("""
### My Favorite Movies

- Race 3
- Toofan
- HeeraMandi


""")

st.code("""

def square(input):
    return input*2
    
square(2)

""")

st.latex(

    'x^2+y^2+2=0'

)

#DataFrame

df = pd.DataFrame({
    'name': ['Fouzia','Saima','Susama','Fariha'],
    'subjects': ['Python','Journalism', 'Economics','Policy'],
    'marks': [50,60,70,80]
})

st.dataframe(df)


st.metric('Stock','30000','3%')

st.json({
    'name': ['Fouzia','Saima','Susama','Fariha'],
    'subjects': ['Python','Journalism', 'Economics','Policy'],
    'marks': [50,60,70,80]
})

st.image('image.png')
#st.video()


st.sidebar.title('Sidebar Tittle')

#pasha pashi dekhanor jonno kono image or content
col1, col2, col3 = st.columns(3)

with col1:
    st.image('image.png')
with col2:
    st.image('image.png')
with col3:
    st.image('image.png')



#showing users error/success message

st.error('Login Failed')

st.success('Login Successful')

st.info('It will show a blue color message')

st.warning('It will show a orange color message')


#progress bar

bar = st.progress(0)

for i in range(1,101):
    #time.sleep(0.1)
    bar.progress(i)


#***************** User inputss **************************

#Text Input
email = st.text_input('Email')

#Number Input
num = st.number_input('Number')

#Date Input
date= st.date_input('Date')


#***************** Button/Dropdown **************************
#Go to login_page file

#***************** file upload from user **************************
#go to file_upload file