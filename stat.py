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
    fig.add_trace(go.Scatter(x=df_temp.columns[1:], y=df_temp.iloc[0,1:],name = j,showlegend = False,line = dict(color='royalblue', width=4)),row = row,col = col)


fig.update_layout(title_text="'SBL傻逼佬'")
fig.update_layout(barmode='stack',dragmode = 'pan',template= 'plotly',clickmode = None,width=2400, height=1600,margin=dict(autoexpand = True,l=20, r=20, t=40, b=20),paper_bgcolor="#ADD8E6")

fig.show()
