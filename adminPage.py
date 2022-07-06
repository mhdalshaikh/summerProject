from datetime import datetime

from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
import base64


def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.

    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
set_bg_hack('C:\\Users\\mohammed_khalil\\Downloads\\background.png')

image = Image.open("C:\\Users\\mohammed_khalil\\Downloads\\OIP.jpg")
st.image(image)
st.title('admin page name place holder')
radio_selection = st.sidebar.selectbox('choose an option:', ('print reports', 'give permission','give privilege'))
if radio_selection == 'print reports':
    select_box_choice = st.selectbox('who to print for:', ('all', 'certain employee'))
    if select_box_choice == 'all':
        clm1, clm2 = st.columns(2)
        date_range = clm1.date_input('from')
        date_range2 = clm2.date_input('to')
        clm1.button('download report')
    elif select_box_choice == 'certain employee':
        clm1, clm2, clm3,clm4 = st.columns(4)
        ID = clm1.text_input('enter employee ID:')
        clm2.text_input(label="", value="asdasd", disabled=True)
        date_range = clm3.date_input('from')
        date_range2 = clm4.date_input('to')
        clm1.button('download report')
elif radio_selection == 'give permission':
    col1,col2=st.columns(2)
    ID = col1.text_input('enter employee ID: ')
    col2.text_input(label="",value="asdasd",disabled=True)
    options = ('Customer site', 'Medical excuse', 'Vacation')
    selection = st.selectbox("please choose a reason",
                             options)

    if selection == 'Customer site':
        clm1, clm2, clm3, clm4, clm5 = st.columns(5)
        client_name_1 = clm1.text_input('Client name: ')
        loc1 = clm3.text_input('location:', key=1)
        country3 = clm2.text_input('country:', key=3)
        start_time1 = clm4.date_input('from:')
        end_time1 = clm5.date_input('to:')
        clm4.button('save/add')
        save_exit_button = clm5.button('save/exit')
    elif selection == 'Medical excuse':
        clm1, clm2, clm3 = st.columns(3)
        date_from = clm1.text_input('Hospital name: ')
        start_time1 = clm2.date_input('from:')
        end_time1 = clm3.date_input('to:')
        clm2.button('save/add')
        save_exit_button = clm3.button('save/exit')
    elif selection == 'Vacation':
        clm1, clm2, clm3 = st.columns(3)
        start_time1 = clm2.date_input('from:')
        end_time_2 = clm3.date_input('to:')
        clm2.button('save/add')
        save_exit_button = clm3.button('save/exit')
elif radio_selection == 'give privilege':
    col1, col2 = st.columns(2)
    ID = col1.text_input('enter employee ID that you want to give privilege to : ')
    col2.text_input(label="", value="asdasd", disabled=True)
    col2.button('confirm')
