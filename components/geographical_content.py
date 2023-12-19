import pandas as pd 
import plotly.express as px
from dash import dcc,html

df = pd.read_csv("C:/Users/anali/Downloads/netflix_titles.csv")

df['country'] = df['country'].str.split(',').apply(lambda x: x[0].strip() if isinstance(x,list) else None)
df['year_added'] = pd.to_datetime(df['year_added']).dt.year
df = df.dropna(subset=['country','year_added'])

df_counts = df.groupby(['country','year_added']).size().reset_index(name='count')
df_counts = df_counts.sort_values('year_added')

fig1 = px.choropleth(
    df_counts,
    locationmode='country_names',
    locations='country',
    color='count',
    hover_name='country',
    animation_frame='year_added',
    projection='natural earth',
    title='Conteudo produzido por país',
    color_continuous_scale='YlGnBu',
    range_color=[0,df_counts['count'].max()]
    )

fig1.update_layout(width=1280,height=720,title_x=0.5)

