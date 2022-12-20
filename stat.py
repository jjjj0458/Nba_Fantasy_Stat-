# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 13:39:35 2022

@author: JackCCChang
"""
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

data = pd.read_csv('game_stat.csv')

rows = 4
cols= 3
specs = [[{'type':'xy'}] * cols] * rows
fig = make_subplots(rows =rows, cols=cols,subplot_titles=data['CAT_NAME'].unique(),specs = specs)
for i ,j in enumerate(data['CAT_NAME'].unique()):
    row =  (i//3)+1
    col = (i%3)+1
    df_temp = data[data['CAT_NAME']==j]
    df_temp = df_temp.set_index('CAT_NAME')
    if j =='TO':
        df_temp = df_temp.sort_values(by=j,axis=1,ascending = True)
    else:
        df_temp = df_temp.sort_values(by=j,axis=1,ascending = False)
    text = df_temp.iloc[0,0:].round(4).astype(str).reset_index(drop=True)
    rank = pd.Series(range(1,11)).astype(str)
    text = text + "(" + rank + ")"
    x_text = df_temp.columns[0:]
    y_text = df_temp.iloc[0,0:]
    fig.add_trace(go.Bar(x=x_text, y=y_text,name = j,showlegend = False,text=text,textposition='outside',textfont_size=8),row = row,col = col)


fig.update_layout(title_text="'SBL傻逼佬'")
fig.update_layout(barmode='stack',dragmode = 'pan',template= 'plotly',clickmode = None,width=2400, height=1600,margin=dict(autoexpand = True,l=20, r=20, t=70, b=20),paper_bgcolor="#ADD8E6")

fig.show()
