import base64
from datetime import datetime
import streamlit as st
from PIL.Image import Image


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
st.title('Late Sheet Name place holder')
options = ('Customer visit', 'Hospital visit', 'Vendor visit', 'Business trip', 'Personal excuse', 'Reporting late')
selection = st.selectbox("Dear NA u have been late for today's attendance for '00:00', please choose a reason", options)

if selection == 'Customer visit':
    clm1, clm2, clm3,clm4,clm5 = st.columns(5)
    client_name_1 = clm1.text_input('Client name 1')
    client_name_2 = clm1.text_input('Client name 2')
    client_name_3 = clm1.text_input('Client name 3')
    loc1=clm3.text_input('location:',key=1)
    loc2=clm3.text_input('location:',key=2)
    loc3=clm3.text_input('location:',key=3)
    country1=clm2.text_input('country:',key=1)
    country2=clm2.text_input('country:',key=2)
    country3=clm2.text_input('country:',key=3)
    start_time1 = clm4.time_input('from:', datetime.now(), 1)
    end_time1 = clm5.time_input('to:', datetime.now(), 1)
    start_time_2 = clm4.time_input('from:', datetime.now(), 2)
    end_time_2 = clm5.time_input('to:', datetime.now(), 2)
    start_time_3 = clm4.time_input('from:', datetime.now(), 3)
    end_time_3 = clm5.time_input('to:', datetime.now(), 3)
    clm4.button('save/add')
    save_exit_button = clm5.button('save/exit')
elif selection == 'Hospital visit':
    clm1, clm2, clm3 = st.columns(3)
    clm1.text_input('location')
    start_time1 = clm2.time_input('from:', datetime.now(), 1)
    end_time1 = clm3.time_input('to:', datetime.now(), 1)
    clm2.button('save/add')
    save_exit_button = clm3.button('save/exit')
elif selection == 'Vendor visit':
    clm1, clm2, clm3 = st.columns(3)
    vendor_name_1 = clm1.text_input('vendor name 1')
    vendor_name_2 = clm1.text_input('vendor name 2')
    start_time1 = clm2.time_input('from:', datetime.now(), 1)
    end_time1 = clm3.time_input('to:', datetime.now(), 1)
    start_time_2 = clm2.time_input('from:', datetime.now(), 2)
    end_time_2 = clm3.time_input('to:', datetime.now(), 2)
    clm2.button('save/add')
    save_exit_button = clm3.button('save/exit')
elif selection == 'Business trip':
    clm1, clm2, clm3,clm4 = st.columns(4)
    clm1.text_input('country:')
    clm2.text_input('location:')
    date_from = clm3.date_input('from')
    date_to = clm4.date_input('to')
    clm3.button('save/add')
    save_exit_button = clm4.button('save/exit')
elif selection == 'Personal excuse':
    clm1, clm2, clm3 = st.columns(3)
    start_time1 = clm2.time_input('from:', datetime.now(), 1)
    end_time1 = clm3.time_input('to:', datetime.now(), 1)
    clm2.button('save/add')
    save_exit_button = clm3.button('save/exit')
elif selection == 'Reporting late':
    clm1, clm2, clm3 = st.columns(3)
    start_time1 = clm2.time_input('from:', datetime.now(), 1)
    end_time1 = clm3.time_input('to:', datetime.now(), 1)
    clm2.button('save/add')
    save_exit_button = clm3.button('save/exit')



