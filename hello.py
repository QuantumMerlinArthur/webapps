import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as nps

####### import google sheet 

import streamlit as st
from gsheetsdb import connect

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

############# questions and stuff
row.'1990 lebten 58% der Weltbevölkerung in Ländern mit niedrigen Einkommen. Wo liegt dieser Anteil heute?',
       ' Welchen Anteil haben Fischeri, Land- und Forstwirtschaft and der Weltwirtschaft?',
       'In wie vielen Ländern gelten Gesetze gegen sexuelle Belästigung?',
       'Welcher Anteil der Welbevölkerung lebt in Megacitys (mehr als 10 Millionen Menschen)',
       'Welcher Anteil der Erderwärmung wird von den Ozeanen aufgenommen. (Wärmeenergie, nicht CO2)',
       'Welcher Anteil des weltweiten Plastimülls landet in den Ozeanen?',
       'Wie viele der 140.000 evaluerten Tier- und Pflanzenarten sind gefährdet oder bedroht?',
       'Wie viele Menschen auf der Welt sind international auf der Flucht? (Keine Binnenflüchtlinge)',
       'Einkommensstarke Länder bekommen welchen Anteil ihrer Einkünfte aus Zöllen und Importabgaben?',
       'Eight billion people in the world today. Which map best shows where they live? (Each figure:  1 billion people.)',
       'Wie hat sich der gesamte, jährliche Rohstoffverbrauch der Welt seit 2000 geändert?',
       'Welche Ländern haben in den letzten 5 Jahren die meisten Truppen für die UN-Friedenstruppen (Blauhelme) gestellt?',
       'Welcher Anteil der Bevölkerung der Länder mit hohem Einkommen (wie Deutschland, USA) lebt in extremer Armut ( <2$/Tag)',
       'Welcher Anteil der Weltbevölkerung hat nicht genug  Essen, um den täglichen Bedarf zu decken? ',
       'Wie hat sich die globale Suizidrate in den letzten 20 Jahren entwickelt? ',
       'Wie viele Unternehmen weltweit werden von einer Frau als Top-Managerin oder CEO geleitet? ',
       'Wie viele Mädchen gingen mind. bis zum Alter von 11 Jahren in einkommensschwachen Ländern zur Schule? (vor Corona)',
       'Wie viele Menschen haben Zugang zu sauberem Trinkwasser in oder nahe ihres Zuhauses?',
       'Welchen Anteil haben Kohle, Öl und Gas am gesamten Energieverbrauch der Welt?']
##### main page
st.title("19 questions")

#st.write([ [  row.f  for row in rows] for f in fragen  ])

for row in rows:
    st.write(row['1990 lebten 58% der Weltbevölkerung in Ländern mit niedrigen Einkommen. Wo liegt dieser Anteil heute?'])
    #st.write(type(row))

#add name and study subject
#results=pd.DataFrame
    
    
    
########## old

val=st.radio('Choose favourite pet', ['cats', 'dogs','guinea pigs'])
st.write(f"user input value: {val}")

dict = {"cats":0,"dogs":1,"guinea pigs":2}

#st.write(f"array index: {dict[val]}")
st.button('Save answer',key="save")

poll=np.arange(0.0,5.0,1.0)
if st.session_state.save:
  
  poll[dict[val]]+=1
  
  st.write(">>Saved")

# plotting example

data = [23, 45, 56]
fig, ax = plt.subplots()
ax.bar(['cats', 'dogs','guinea pigs'], data)
st.pyplot(fig)
