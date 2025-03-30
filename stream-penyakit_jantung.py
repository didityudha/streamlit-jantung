 import pickle
 import numpy as np
import streamlit

# load save model
model = pickle.load(open('penyakit_jantung,sav','rb'))

#judul web
st.title('Prediksi Penyakit Jantung')

col1, col2, col3 = st.column(3)

with col1:  
  age = st.text_input('Umur')
with col2:
  sex = st.text_input('Jenis kelamin')
with col3:
  cp = st.text_input('Jenis nyeri dada')
with col1:
  trestbps = st.text_input('Tekanan darah')
with col2:
  chol = st.text_input('Nilai kolestrol')
with col3:
  fbs = st.text_input('Gula darah')
with col1:
  restecg = st.text_input('hasil Elektrokardiografi')
with col2:
  thlach = st.text_input('Detak Jantung Maksimum')
with col3:
  exang = st.text_input('Induksi Angina')
with col1:
  oldpeak = st.text_input('ST Depression')
with col2:
  slope = st.text_input('Slope')
with col3:
  ca = st.text_input('Nilai CA')
with col1:
  thal = st.text_input('Nilai Thal')

  # code for prediction
  heart_dianogsis =''

  # membuat tombol prediksi
  if st.button('Prediksi Penyakit Jantung'):
    heart_prediction = model.predict([age, sex, cp, trestbps, chol, fbs, restecg, thlach, exang, oldpeak, slope, ca, thal ])

    if (heart_prediction[0]==1):
        heart_dianogsis = 'Pasien Terkena Penyakit Jantung'
    else:
        heart_dianogsis = 'Pasien Tidak Terkena Penyakit Jantung'
st.success(heart_dianogsis)

