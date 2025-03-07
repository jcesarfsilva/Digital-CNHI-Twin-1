import streamlit as st 
from PIL import Image


def app():   
    tab1, tab2 = st.tabs(["📈 Real-Time Optimization", "📈 Static Prediction"])
    

    with tab1:
         c1, c2, c3 = st.columns((1, 5, 1))       
    with c1:
        st.write("")
    with c2: 
        st.image('realtime2.jpg',   use_column_width='never',)     
    with c3:
        st.write("")
        

    with tab2:
        st.markdown("<h1 style='text-align: center; color: black;'>How to use this App</h1>", unsafe_allow_html=True)
        
        c1, c2 = st.columns((2))  
        with c1: 
            st.write(""" 
            ### This App used to predict three output of Polypropylene Reactor.
            #### Predictors values that shall be determined to predict the Targets are :
            ##### 1. Liquid Percent level in Reactor
            ##### 2. Reactor Temperature 
            ##### 3. Reactor Internal Pressure
            ##### 4. Water Volume Flow to reactor 
            ##### 5. Propylene Oxide Volume Flow to Reactor
            ##### 6. Nitrogen Flow to Reactor

            #### Targets values that predicted from targets are :
            ##### A. Vapor Product Flow Outlet Reactor
            ##### B. Concentration of Propylene Glycol Outlet Reactor 
            ##### C. Liquid Product Flow Outlet Reactor
            """)
     
        with c2: 
            st.image('gambarreaktor3.jpg', caption='Predictors and Targets in Polypropylene Process')     

    
