import base64
import time
from datetime import datetime
import datetime as dt
from datetime import date
import streamlit as st
from PIL import Image
import pyodbc


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
st.title('Late Sheet Name place holder')
options = ('Customer visit', 'Hospital visit', 'Vendor visit', 'Business trip', 'Personal excuse', 'Reporting late')
selection = st.selectbox("Dear NA u have been late for today's attendance for '00:00', please choose a reason", options)


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-PUSE1ERN;'
                      'Database=testDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
#cursor.execute('CREATE table attendance(ID varchar(255),Name varchar(255),Date varchar(255),total_hours varchar(255),'
 #              'total_office_hours varchar(255),Customer_visit varchar(255),customer_name varchar(255),'
  #             'country varchar(255),location varchar(255),hospital_visit varchar(255),location varchar(255),'
   #            'vendor_visit varchar(255),vendor_name varchar(255),business_trip varchar(255),country varchar(255),'
    #           'location varchar(255),from varchar(255),to varchar(255),personal_excuse varchar(255),reporting_late '
     #          'varchar(255))')
#mods='asdasd'
#dates=f"{datetime.now():%d-%m-%Y}"
#print(dates)
#cursor.execute("INSERT into attendance(ID,Name,Date) VALUES(?,?,?)",('111',mods,dates))

#cursor.execute("SELECT * FROM attendance")

# fetch all the matching rows
#result = cursor.fetchall()

# loop through the rows
#for row in result:
 #   print(row)
  #  print("\n")
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



    save_add_button= clm4.button('save/add')
    if save_add_button:
        timeList = [start_time1, end_time1]
        start_time1
        end_time1
        mysum = dt.timedelta()
        (h, m,s) = start_time1.split(':')
        (h2, m2,s2) =end_time1.split(':')
        h
        d = dt.timedelta(hours=int(h), minutes=int(m),seconds=int(s))
        d2 = dt.timedelta(hours=int(h2), minutes=int(m2),seconds=int(s2))
        mysum = d2-d
        str(mysum)
        mysum
    save_exit_button = clm5.button('save/exit')

elif selection == 'Hospital visit':
    clm1, clm2, clm3 = st.columns(3)
    clm1.text_input('location')
    start_time1 = str(clm2.time_input('from:', datetime.now(), 1))
    end_time1 = str(clm3.time_input('to:', datetime.now(), 1))
    save_add_button= clm2.button('save/add')
    save_exit_button = clm3.button('save/exit')
elif selection == 'Vendor visit':
    clm1, clm2, clm3 = st.columns(3)
    vendor_name_1 = clm1.text_input('vendor name 1')
    vendor_name_2 = clm1.text_input('vendor name 2')
    start_time1 = str(clm2.time_input('from:', datetime.now(), 1))
    end_time1 = str(clm3.time_input('to:', datetime.now(), 1))
    start_time_2 = str(clm2.time_input('from:', datetime.now(), 2))
    end_time_2 = str(clm3.time_input('to:', datetime.now(), 2))
    clm2.button('save/add')
    save_exit_button = clm3.button('save/exit')
elif selection == 'Business trip':
    clm1, clm2, clm3,clm4 = st.columns(4)
    clm1.text_input('country:')
    clm2.text_input('location:')
    date_from = str(clm3.date_input('from'))
    date_to = str(clm4.date_input('to'))
    clm3.button('save/add')
    save_exit_button = clm4.button('save/exit')
elif selection == 'Personal excuse':
    clm1, clm2, clm3 = st.columns(3)
    start_time1 = str(clm2.time_input('from:', datetime.now(), 1))
    end_time1 = str(clm3.time_input('to:', datetime.now(), 1))
    clm2.button('save/add')
    save_exit_button = clm3.button('save/exit')
elif selection == 'Reporting late':
    clm1, clm2, clm3 = st.columns(3)
    start_time1 = str(clm2.time_input('from:', datetime.now(), 1))
    end_time1 = str(clm3.time_input('to:', datetime.now(), 1))
    clm2.button('save/add')
    save_exit_button = clm3.button('save/exit')



