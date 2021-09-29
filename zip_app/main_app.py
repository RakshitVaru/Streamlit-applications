import streamlit as st
import pandas as pd
import zipfile
import base64
import os

st.markdown("""
# **Excel File Merger**

This is the **Excel File Merger App** created in python using the streamlit library.

""")

# Merger Function
def merge(zip_name):
    df= pd.DataFrame()
    archive= zipfile.ZipFile(zip_name,'r')
    with zipfile.ZipFile( zip_name, 'r') as f:
        for file in f.namelist():
            xlfile=  archive.open(file)
            if file.endswith('.xlsx'):
                df_xl= pd.read_excel(xlfile, engine='openpyxl')
                df_xl['Note']=file
                df= df.append(df_xl, ignore_index=True)
    return df

with st.sidebar.header('1. Upload the ZIP file'):
    uploaded_file= st.sidebar.file_uploader("Excel-containing ZIP file", type=["zip"])
    st.sidebar.markdown("""
[Example ZIP input file](https://github.com/dataprofessor/excel-file-merge-app/raw/main/nba_data.zip)
""")

def filedownload(df):
    csv= df.to_csv(index=False)
    b64= base64.b64encode(csv.encode()).decode()
    href= f'<a href="data:file/csv;base64,{b64}" download= "merged_file.csv">Download Merged File as CSV </a>'
    return href


def xldownload(df):
    df.to_excel('data.xlsx', index=False)
    data= open('data.xlsx', 'rb').read()
    b64= base64.b64encode(data).decode('UTF-8')
    href= f'<a href="data:file/csv;base64,{b64}" download= "merged_file.csv">Download Merged File as CSV </a>'
    return href

if st.sidebar.button('Submit'):
    df= merge(uploaded_file)
    st.header("**Merged Data**")
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)
    st.markdown(xldownload(df), unsafe_allow_html=True)
else:
    st.info("Awaiting for ZIP file to be uploaded.")