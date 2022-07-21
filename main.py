import base64
import csv
import time
from datetime import datetime
import datetime as dt
from datetime import date
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

def insert_client(mysum,client_name_1,loc1,country1,mysum2,client_name_2,loc2,country2,mysum3,client_name_3,loc3,country3):
    array[5] =mysum
    array[6]= client_name_1
    array[7]= loc1
    array[8]= country1
    array[9] =mysum2
    array[10]= client_name_2
    array[11]= loc2
    array[12]= country2
    array[13]=mysum3
    array[14]= client_name_3
    array[15]= loc3
    array[16]= country3
@st.cache(allow_output_mutation=True)
def initialize_array():
    array=['-']*29
    array[0]= "123"
    array[1] ="khalil"
    array[2]= date.today()
    return array
def calculate_time(start_time1, end_time1):
    mysum = dt.timedelta()
    (h, m, s) = start_time1.split(':')
    (h2, m2, s2) = end_time1.split(':')
    d = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    d2 = dt.timedelta(hours=int(h2), minutes=int(m2), seconds=int(s2))
    mysum = d2 - d
    return mysum


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


set_bg_hack('background.png')

image = Image.open("OIP.jpg")
st.image(image)
array=initialize_array()
# fetch all the matching rows
finish = False
st.title('Late Sheet Name place holder')
options = (
'----', 'Customer visit', 'Hospital visit', 'Vendor visit', 'Business trip', 'Personal excuse', 'Reporting late')
selection = st.selectbox("Dear NA u have been late for today's attendance for '00:00', please choose a reason",
                         options)
if selection == 'Customer visit':
    clm1, clm2, clm3, clm4, clm5 = st.columns(5)
    client_name_1 = clm1.text_input('Client name 1')
    client_name_2 = clm1.text_input('Client name 2')
    client_name_3 = clm1.text_input('Client name 3')
    loc1 = clm3.text_input('location:', key=1)
    loc2 = clm3.text_input('location:', key=2)
    loc3 = clm3.text_input('location:', key=3)
    country1 = clm2.text_input('country:', key=1)
    country2 = clm2.text_input('country:', key=2)
    country3 = clm2.text_input('country:', key=3)
    start_time1 = str(clm4.time_input('from:', datetime.now(), 1))
    end_time1 = str(clm5.time_input('to:', datetime.now(), 1))
    start_time_2 = str(clm4.time_input('from:', datetime.now(), 2))
    end_time_2 = str(clm5.time_input('to:', datetime.now(), 2))
    start_time_3 = str(clm4.time_input('from:', datetime.now(), 3))
    end_time_3 = str(clm5.time_input('to:', datetime.now(), 3))
    save_add_button = clm4.button('save/add')
    if save_add_button:
        mysum = calculate_time(start_time1, end_time1)
        mysum2 = calculate_time(start_time_2, end_time_2)
        mysum3 = calculate_time(start_time_3, end_time_3)
        insert_client(mysum,client_name_1,loc1,country1,mysum2,client_name_2,loc2,country2,mysum3,client_name_3,loc3,country3)
        st.success('response added')
    save_exit_button = clm5.button('save/exit')
    if save_exit_button:
        mysum = calculate_time(start_time1, end_time1)
        mysum2 = calculate_time(start_time_2, end_time_2)
        mysum3 = calculate_time(start_time_3, end_time_3)
        insert_client(mysum,client_name_1,loc1,country1,mysum2,client_name_2,loc2,country2,mysum3,client_name_3,loc3,country3)
        finish = True
elif selection == 'Hospital visit':
    clm1, clm2, clm3 = st.columns(3)
    location=clm1.text_input('location')
    start_time1 = str(clm2.time_input('from:', datetime.now(), 1))
    end_time1 = str(clm3.time_input('to:', datetime.now(), 1))
    save_add_button = clm2.button('save/add')
    if save_add_button:
        mysum = calculate_time(start_time1, end_time1)
        array[17]=mysum
        array[18]=location
        st.success('response added')
    save_exit_button = clm3.button('save/exit')
    if save_exit_button:
        mysum = calculate_time(start_time1, end_time1)
        array[17]=mysum
        array[18]=location
        finish = True
elif selection == 'Vendor visit':
    clm1, clm2, clm3 = st.columns(3)
    vendor_name_1 = clm1.text_input('vendor name 1')
    vendor_name_2 = clm1.text_input('vendor name 2')
    start_time1 = str(clm2.time_input('from:', datetime.now(), 1))
    end_time1 = str(clm3.time_input('to:', datetime.now(), 1))
    start_time_2 = str(clm2.time_input('from:', datetime.now(), 2))
    end_time_2 = str(clm3.time_input('to:', datetime.now(), 2))
    save_add_button = clm2.button('save/add')
    if save_add_button:
        mysum = calculate_time(start_time1, end_time1)
        mysum2 = calculate_time(start_time_2, end_time_2)
        array[19]=mysum
        array[20]=vendor_name_1
        array[21]=mysum2
        array[22]=vendor_name_2
        st.success('response added')
    save_exit_button = clm3.button('save/exit')
    if save_exit_button:
        mysum = calculate_time(start_time1, end_time1)
        mysum2 = calculate_time(start_time_2, end_time_2)
        array[19]=mysum
        array[20]=vendor_name_1
        array[21]=mysum2
        array[22]=vendor_name_2
        finish = True
elif selection == 'Business trip':
    clm1, clm2, clm3, clm4 = st.columns(4)
    country=clm1.text_input('country:')
    location=clm2.text_input('location:')
    date_from = str(clm3.date_input('from'))
    date_to = str(clm4.date_input('to'))
    save_add_button = clm3.button('save/add')
    if save_add_button:
        array[23]=country
        array[24]=location
        array[25]=date_from
        array[26]=date_to
        st.success('response added')
    save_exit_button = clm4.button('save/exit')
    if save_exit_button:
        array[23]=country
        array[24]=location
        array[25]=date_from
        array[26]=date_to
        finish = True
elif selection == 'Personal excuse':
    clm1, clm2, clm3 = st.columns(3)
    start_time1 = str(clm2.time_input('from:', datetime.now(), 1))
    end_time1 = str(clm3.time_input('to:', datetime.now(), 1))
    save_add_button = clm2.button('save/add')
    if save_add_button:
        mysum = calculate_time(start_time1, end_time1)
        array[27]=mysum
        st.success('response added')
    save_exit_button = clm3.button('save/exit')
    if save_exit_button:
        mysum = calculate_time(start_time1, end_time1)
        array[27]=mysum
        finish = True
elif selection == 'Reporting late':
    clm1, clm2, clm3 = st.columns(3)
    start_time1 = str(clm2.time_input('from:', datetime.now(), 1))
    end_time1 = str(clm3.time_input('to:', datetime.now(), 1))
    save_add_button = clm2.button('save/add')
    if save_add_button:
        mysum = calculate_time(start_time1, end_time1)
        array[28]=mysum
        st.success('response added')
    save_exit_button = clm3.button('save/exit')
    if save_exit_button:
        mysum = calculate_time(start_time1, end_time1)
        array[28]=mysum
        finish = True
if finish is True:

    with open('out.csv', 'a') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(array)
    st.success('response saved, you can now exit the form')
    st.stop()
