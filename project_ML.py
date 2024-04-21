import streamlit as st
import pickle
from PIL import Image



def main():
    st.title(":rainbow[ADULT INCOME PREDICTIONS]")
    image = Image.open('income image.jpg')
    st.image(image, width=800)
    age = st.sidebar.slider('age', 0,100,1,step=1)
    fnlwgt = st.sidebar.text_input(' final weight', placeholder='enter fnlwgt value')
    option2 = st.sidebar.selectbox('education', ('Preschool', '1st-4th', '5th-6th', '7th-8th', '9th', '10th',
                                          '11th', '12th', 'HS-grad', 'Prof-school', 'Assoc-acdm',
                                          'Some-college', 'Assoc-voc', 'Bachelors', 'Masters', 'Doctorate'))
    data2 = {'11th':0, 'HS-grad':1, 'Assoc-acdm':2, 'Some-college':3, '10th':4, 'Prof-school':5,
             '7th-8th':6, 'Bachelors':7, 'Masters':8, 'Doctorate':9, '5th-6th':10, 'Assoc-voc':11,
             '9th':12, '12th':13, '1st-4th':14, 'Preschool':15}
    education = data2[option2]
    educational_num = st.sidebar.text_input('number of years of education', placeholder='enter educational-num value')
    option = st.sidebar.selectbox('marital-status',('Never-married', 'Married-civ-spouse', 'Widowed', 'Divorced',
                                            'Separated', 'Married-spouse-absent', 'Married-AF-spouse'))
    data = {'Never-married':0, 'Married-civ-spouse':1, 'Widowed':2, 'Divorced':3,
            'Separated':4, 'Married-spouse-absent':5, 'Married-AF-spouse':6}
    marital_status = data[option]
    option1=st.sidebar.selectbox('relationship',('Own-child', 'Husband', 'Not-in-family', 'Unmarried', 'Wife','Other-relative'))
    data1={'Own-child':0,'Husband':1,'Not-in-family':2,'Unmarried':3,'Wife':4,'Other-relative':5}
    relationship = data1[option1]
    # relationship = st.text_input('relationship', placeholder='enter relationship value')
    gender = st.sidebar.radio('Sex', ['Male', 'Female'])
    if gender == 'Male':
        sex = 1
    else:
        sex = 0
    capital_gain = st.sidebar.text_input('capital-gain', placeholder='enter capital-gain value')
    capital_loss = st.sidebar.text_input('capital_loss', placeholder='enter capital-loss value')
    hours_per_week = st.sidebar.text_input('hours_per_week', placeholder='enter hours-per-week value')
    native_country = st.sidebar.text_input('native_country', placeholder='enter native-country value')
    features = [age, fnlwgt, education, educational_num, marital_status, relationship,
                sex, capital_gain, capital_loss, hours_per_week, native_country]
    model = pickle.load(open('model1 (1).sav', 'rb'))
    scaler = pickle.load(open('scaler1 (1).sav', 'rb'))
    pred = st.button('PREDICT')
    if pred:
        prediction = model.predict(scaler.transform([features]))
        if prediction == 0:
            st.markdown('*The person earns less than 50000*')
        else:
            st.markdown('*The person earns more than 50000*')


main()