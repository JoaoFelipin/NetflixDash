import pandas as pd
import plotly.express as px
from dash import html,dcc 

df = pd.read_csv("C:/Users/anali/Downloads/netflix_titles.csv")

df['listed_in'] = df['listed_in'].str.split(', ')
df = df.explode('listed_in')

df_counts = df.groupby(['type','listed_in']).size().reset_index(name='count')

fig = px.treemap(df_counts,path=['type','listed_in'],values='count',color_continuous_scale='Ice',title='Conteudo por tipo e gênero')

fig.update_layout(width=1280,height=960,title_x=0.5)
fig.update_traces(textinfo='label+percent entry',textfont_size=14)

layout= html.Div([
    dcc.Graph(figure=fig),
])