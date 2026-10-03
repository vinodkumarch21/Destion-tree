import streamlit as st
import joblib

model=joblib.load('svc_model.pkl')
st.title("Machine learing project")

sl=st.number_input(label='sepal length',min_value=0.0,max_value=10.0)
sw=st.number_input(label='sepal_width',min_value=0.0,max_value=10.0)
pl=st.number_input(label='petal_length',min_value=0.0,max_value=10.0)
pw=st.number_input(label='petal_width',min_value=0.0,max_value=10.0)

if st.button(label='predict'):
    result=model.predict([[sl,sw,pl,pw]])
    if result==0:
        st.success('setosa')
    elif result==1:
        st.success('versicolor')
    else:
        st.success('virginica')