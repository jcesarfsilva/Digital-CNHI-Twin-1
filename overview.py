import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import streamlit as st
from comum import renameColumns, lerArquivo




def app():
    header = st.container()
    with header:
        st.markdown("<h2 style='text-align: center; color: black;'>Data Profile</h1>", unsafe_allow_html=True)

        df = lerArquivo()

        if df is None or df.empty:  # Verifica se o DataFrame está vazio
            
            return  

        renameColumns(df)
        
        profile = ProfileReport(df, explorative=True)
        st_profile_report(profile)