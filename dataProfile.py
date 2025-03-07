import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import streamlit as st
from comum import renameColumns, lerArquivo,dropna




def app():
    header = st.container()
    with header:
        st.markdown("<h2 style='text-align: center; color: black;'>Dashboard</h1>", unsafe_allow_html=True)

        df = lerArquivo()

        if df is None or df.empty:  # Verifica se o DataFrame está vazio
            return  

        renameColumns(df)
        dropna(df)

        # Verificar se a coluna 'BaseCutRPM' contém apenas valores escalares
        if 'BaseCutRPM' in df.columns:
            mask = df['BaseCutRPM'].apply(lambda x: pd.api.types.is_scalar(x))
            df = df[mask]

        print(df)
        profile = ProfileReport(df, explorative=True)
        st_profile_report(profile)
