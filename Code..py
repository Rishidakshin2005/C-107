import csv
import pandas as pd 
import plotly.graph_objects as go 
   
df= pd.read_csv("Data.csv")
studentdf=df.loc[df['student_id']=="TRL_abc"]
figure=go.Figure(go.Bar(
    x=studentdf.groupby("level")["attempt"].mean(),
    y=['level1','level2','level3','level4'],
    orientation='h'
))
figure.show()