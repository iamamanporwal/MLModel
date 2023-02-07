$pip install scikit-learn
$pip install streamlit
import streamlit as st 
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image 

model = pickle.load(open('model.sav', 'rb'))

st.title('prediction model')
st.sidebar.header('Data')
image = Image.open(image.jpg)
st.image(image, '')
