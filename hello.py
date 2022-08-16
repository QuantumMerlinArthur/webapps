import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as nps

####### import google sheet 

############# questions and stuff

### data

testString = io.StringIO(""" Frage,Antwort,Anzahl
1990 lebten 58% der Weltbevölkerung in Ländern mit niedrigen Einkommen. Wo liegt dieser Anteil heute?,richtig,2
1990 lebten 58% der Weltbevölkerung in Ländern mit niedrigen Einkommen. Wo liegt dieser Anteil heute?,ca. 9%,2
1990 lebten 58% der Weltbevölkerung in Ländern mit niedrigen Einkommen. Wo liegt dieser Anteil heute?,ca. 37%,1
1990 lebten 58% der Weltbevölkerung in Ländern mit niedrigen Einkommen. Wo liegt dieser Anteil heute?,ca. 61%,1
" Welchen Anteil haben Fischeri, Land- und Forstwirtschaft and der Weltwirtschaft?",richtig,1
" Welchen Anteil haben Fischeri, Land- und Forstwirtschaft and der Weltwirtschaft?",ca. 5%,1
" Welchen Anteil haben Fischeri, Land- und Forstwirtschaft and der Weltwirtschaft?",ca. 25%,1
" Welchen Anteil haben Fischeri, Land- und Forstwirtschaft and der Weltwirtschaft?",ca. 45%,1
In wie vielen Ländern gelten Gesetze gegen sexuelle Belästigung?,richtig,1
In wie vielen Ländern gelten Gesetze gegen sexuelle Belästigung?,ca. 30%,1
In wie vielen Ländern gelten Gesetze gegen sexuelle Belästigung?,ca. 70%,1
In wie vielen Ländern gelten Gesetze gegen sexuelle Belästigung?,ca. 50%,1
Welcher Anteil der Welbevölkerung lebt in Megacitys (mehr als 10 Millionen Menschen),richtig,1
Welcher Anteil der Welbevölkerung lebt in Megacitys (mehr als 10 Millionen Menschen),ca. 48%,1
Welcher Anteil der Welbevölkerung lebt in Megacitys (mehr als 10 Millionen Menschen),ca. 28%,1
Welcher Anteil der Welbevölkerung lebt in Megacitys (mehr als 10 Millionen Menschen),ca. 8%,1
"Welcher Anteil der Erderwärmung wird von den Ozeanen aufgenommen. (Wärmeenergie, nicht CO2)",richtig,1
"Welcher Anteil der Erderwärmung wird von den Ozeanen aufgenommen. (Wärmeenergie, nicht CO2)",ca. 10% ,0
"Welcher Anteil der Erderwärmung wird von den Ozeanen aufgenommen. (Wärmeenergie, nicht CO2)",ca. 50%,1
"Welcher Anteil der Erderwärmung wird von den Ozeanen aufgenommen. (Wärmeenergie, nicht CO2)",ca. 90%,1
Welcher Anteil des weltweiten Plastimülls landet in den Ozeanen?,richtig,1
Welcher Anteil des weltweiten Plastimülls landet in den Ozeanen?,ca. 36%,1
Welcher Anteil des weltweiten Plastimülls landet in den Ozeanen?,weniger als 6%,1
Welcher Anteil des weltweiten Plastimülls landet in den Ozeanen?,mehr als 66%,1
Wie viele der 140.000 evaluerten Tier- und Pflanzenarten sind gefährdet oder bedroht?,richtig,1
Wie viele der 140.000 evaluerten Tier- und Pflanzenarten sind gefährdet oder bedroht?,ca. 30%,1
Wie viele der 140.000 evaluerten Tier- und Pflanzenarten sind gefährdet oder bedroht?,ca. 60%,1
Wie viele der 140.000 evaluerten Tier- und Pflanzenarten sind gefährdet oder bedroht?,ca. 90%,1
Wie viele Menschen auf der Welt sind international auf der Flucht? (Keine Binnenflüchtlinge),richtig,0
Wie viele Menschen auf der Welt sind international auf der Flucht? (Keine Binnenflüchtlinge),ca. 15.5%,0
Wie viele Menschen auf der Welt sind international auf der Flucht? (Keine Binnenflüchtlinge),ca. 5.5%,0
Wie viele Menschen auf der Welt sind international auf der Flucht? (Keine Binnenflüchtlinge),ca. 0.5%,0
Einkommensstarke Länder bekommen welchen Anteil ihrer Einkünfte aus Zöllen und Importabgaben?,richtig,1
Einkommensstarke Länder bekommen welchen Anteil ihrer Einkünfte aus Zöllen und Importabgaben?,ca. 12%,1
Einkommensstarke Länder bekommen welchen Anteil ihrer Einkünfte aus Zöllen und Importabgaben?,ca. 2%,1
Einkommensstarke Länder bekommen welchen Anteil ihrer Einkünfte aus Zöllen und Importabgaben?,ca. 22%,1
Eight billion people in the world today. Which map best shows where they live? (Each figure:  1 billion people.),richtig,1
Eight billion people in the world today. Which map best shows where they live? (Each figure:  1 billion people.),A,1
Eight billion people in the world today. Which map best shows where they live? (Each figure:  1 billion people.),B,1
Eight billion people in the world today. Which map best shows where they live? (Each figure:  1 billion people.),C,1
"Wie hat sich der gesamte, jährliche Rohstoffverbrauch der Welt seit 2000 geändert?",richtig,1
"Wie hat sich der gesamte, jährliche Rohstoffverbrauch der Welt seit 2000 geändert?",ungefähr gleich geblieben,1
"Wie hat sich der gesamte, jährliche Rohstoffverbrauch der Welt seit 2000 geändert?",um ca. 35% zugenommen,0
"Wie hat sich der gesamte, jährliche Rohstoffverbrauch der Welt seit 2000 geändert?",um ca. 70% zugenommen,1
Welche Ländern haben in den letzten 5 Jahren die meisten Truppen für die UN-Friedenstruppen (Blauhelme) gestellt?,richtig,1
Welche Ländern haben in den letzten 5 Jahren die meisten Truppen für die UN-Friedenstruppen (Blauhelme) gestellt?,"Deutschland, Schweden, Niederlande, Irland",1
Welche Ländern haben in den letzten 5 Jahren die meisten Truppen für die UN-Friedenstruppen (Blauhelme) gestellt?,"Ethiopien, Ruanda, Bangladesch, Indien, Nepal",1
Welche Ländern haben in den letzten 5 Jahren die meisten Truppen für die UN-Friedenstruppen (Blauhelme) gestellt?,"Frankreich, USA, Japan, Südkorea, Schweiz, UK",1
"Welcher Anteil der Bevölkerung der Länder mit hohem Einkommen (wie Deutschland, USA) lebt in extremer Armut ( <2$/Tag)",richtig,0
"Welcher Anteil der Bevölkerung der Länder mit hohem Einkommen (wie Deutschland, USA) lebt in extremer Armut ( <2$/Tag)",Weniger als 1%,0
"Welcher Anteil der Bevölkerung der Länder mit hohem Einkommen (wie Deutschland, USA) lebt in extremer Armut ( <2$/Tag)",ca. 11%,2
"Welcher Anteil der Bevölkerung der Länder mit hohem Einkommen (wie Deutschland, USA) lebt in extremer Armut ( <2$/Tag)",ca. 21%,1
"Welcher Anteil der Weltbevölkerung hat nicht genug  Essen, um den täglichen Bedarf zu decken? ",richtig,0
"Welcher Anteil der Weltbevölkerung hat nicht genug  Essen, um den täglichen Bedarf zu decken? ",ca 23%,0
"Welcher Anteil der Weltbevölkerung hat nicht genug  Essen, um den täglichen Bedarf zu decken? ",ca 11%,0
"Welcher Anteil der Weltbevölkerung hat nicht genug  Essen, um den täglichen Bedarf zu decken? ",ca. 37%,1
Wie hat sich die globale Suizidrate in den letzten 20 Jahren entwickelt? ,richtig,0
Wie hat sich die globale Suizidrate in den letzten 20 Jahren entwickelt? ,In etwa gleich geblieben,0
Wie hat sich die globale Suizidrate in den letzten 20 Jahren entwickelt? ,Abnahme um ca. 25%,0
Wie hat sich die globale Suizidrate in den letzten 20 Jahren entwickelt? ,Anstieg um ca 25%,0
Wie viele Unternehmen weltweit werden von einer Frau als Top-Managerin oder CEO geleitet? ,richtig,1
Wie viele Unternehmen weltweit werden von einer Frau als Top-Managerin oder CEO geleitet? ,ca. 18%,1
Wie viele Unternehmen weltweit werden von einer Frau als Top-Managerin oder CEO geleitet? ,ca. 2%,1
Wie viele Unternehmen weltweit werden von einer Frau als Top-Managerin oder CEO geleitet? ,ca. 10%,1
Wie viele Mädchen gingen mind. bis zum Alter von 11 Jahren in einkommensschwachen Ländern zur Schule? (vor Corona),richtig,1
Wie viele Mädchen gingen mind. bis zum Alter von 11 Jahren in einkommensschwachen Ländern zur Schule? (vor Corona),ca. 40%,1
Wie viele Mädchen gingen mind. bis zum Alter von 11 Jahren in einkommensschwachen Ländern zur Schule? (vor Corona),ca. 20%,1
Wie viele Mädchen gingen mind. bis zum Alter von 11 Jahren in einkommensschwachen Ländern zur Schule? (vor Corona),ca. 60%,1
Wie viele Menschen haben Zugang zu sauberem Trinkwasser in oder nahe ihres Zuhauses?,richtig,1
Wie viele Menschen haben Zugang zu sauberem Trinkwasser in oder nahe ihres Zuhauses?,ca. 70%,1
Wie viele Menschen haben Zugang zu sauberem Trinkwasser in oder nahe ihres Zuhauses?,ca. 50%,1
Wie viele Menschen haben Zugang zu sauberem Trinkwasser in oder nahe ihres Zuhauses?,ca. 30%,1
"Welchen Anteil haben Kohle, Öl und Gas am gesamten Energieverbrauch der Welt?",richtig,1
"Welchen Anteil haben Kohle, Öl und Gas am gesamten Energieverbrauch der Welt?",ca. 42%,1
"Welchen Anteil haben Kohle, Öl und Gas am gesamten Energieverbrauch der Welt?",ca. 62%,1
"Welchen Anteil haben Kohle, Öl und Gas am gesamten Energieverbrauch der Welt?",ca. 82%,1
""");
final = pd.read_csv(testString,sep=",")
final=final.set_index(["Frage","Antwort"])
##### main page
st.title("19 questions")

    
    
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
