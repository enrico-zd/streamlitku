import pickle
import numpy as np
import streamlit as st

# load save model
model1 = pickle.load(open('predict_rain_model_logreg_fix.pkl', 'rb'))
model2 = pickle.load(open('predict_rain_model_svm_fix.pkl', 'rb'))


# judul web
st.title('Rain Tomorrow Predict')

max_temp = st.text_input('Maximum Temperature')

wgs = st.text_input('Wind Gust Speed')

hum9am = st.text_input('Humiditty 9am')

hum3pm = st.text_input('Humidity 3pm')

pres9am = st.text_input('Pressure 9am')

pres3pm = st.text_input('Pressure 3pm')

temp3pm = st.text_input('Temperature 3pm')

rain_today = st.text_input('Rain Today')

# code foor prediction 
rain_predict = ''

# membuat tombol prediksi 
if st.button('Predict Rain Tomorrow with Logistic Regression') :
    rain_predict = model1.predict([[max_temp, wgs, hum9am, hum3pm, pres9am, pres3pm, temp3pm, rain_today]])
    if (rain_predict[0]==1):
        rain_predict = 'Tomorrow will rain'
    else : 
        rain_predict = 'Tomorrow will not rain'
elif st.button('Predict Rain Tomorrow with SVM') :
    rain_predict = model2.predict([[max_temp, wgs, hum9am, hum3pm, pres9am, pres3pm, temp3pm, rain_today]])
    if (rain_predict[0]==1):
        rain_predict = 'Tomorrow will rain'
    else : 
        rain_predict = 'Tomorrow will not rain'

st.success(rain_predict)
