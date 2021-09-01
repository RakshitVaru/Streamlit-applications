import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Penguin Prediction App

This app predicts the **Palmer Penguin** species!
""")

st.sidebar.header("User Input Features")
st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

uploaded_file= st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df= pd.read_csv(uploaded_file)

else:
    def user_input_features():
        island= st.sidebar.selectbox('Island',('Biscoe', 'Dream', 'Torgersen'))
        sex= st.sidebar.selectbox('Sex',('male', 'female'))
        bill_length_mm= st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
        bill_depth_mm= st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
        flipper_length_mm= st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
        body_mass_g= st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
        
        data={
            'island':island,
            'bill_length_mm':bill_length_mm,
            'bill_depth_mm':bill_depth_mm,
            'flipper_length_mm':flipper_length_mm,
            'body_mass_g':body_mass_g,
            'sex':sex
        }
        features= pd.DataFrame(data, index=[0])
        return features
    input_df= user_input_features()


# Combine user input with entire penguin dataset
# This will be used in encoding stage
penguin_raw= pd.read_csv("https://raw.githubusercontent.com/dataprofessor/code/master/streamlit/part3/penguins_cleaned.csv")
penguin= penguin_raw.drop(columns=['species'])
df=pd.concat([input_df,penguin], axis=0)

# Encoding of ordinal features
# https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering

encode= ['sex', 'island']
for i in encode:
    dummy= pd.get_dummies(df[i], prefix=i)
    df=pd.concat([df,dummy], axis=1)
    del df[i]
df= df[:1] # The user input data is only selected

# Displays the user input features
st.subheader('User Input features')

if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)

# Reads in saved Classification model
load_clf= pickle.load(open('penguins_clf.pkl','rb'))

# Apply model to predictions
prediction= load_clf.predict(df)
prediction_proba= load_clf.predict_proba(df)

st.subheader("Predictions")
penguin_species= np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.write(penguin_species[prediction])

st.subheader("Prediction Probability")
st.write(prediction_proba)