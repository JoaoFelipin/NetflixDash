import pandas as pd 
import plotly.express as px
from dash import dcc,html

df = pd.read_csv("C:/Users/anali/Downloads/netflix_titles.csv")

df['country'] = df['country'].str.split(',').apply(lambda x: x[0].strip() if isinstance(x,list) else None)
df['year_added'] = pd.to_datetime(df['date_added'],format='mixed').dt.year
df = df.dropna(subset=['country','year_added'])

df_counts = df.groupby(['country','year_added']).size().reset_index(name='count')
df_counts = df_counts.sort_values('year_added')

fig1 = px.choropleth(
    df_counts,
    locationmode='country names',
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

df_year_count = df.groupby(['year_added','type']).size().reset_index(name='count')
fig2 = px.line(df_year_count,x='year_added',y='count',color='type',
               title='Distribuição dos conteúdos ao longo dos anos',
               markers=True,
               color_discrete_map={'Movie':'dodgerblue','TV Show':'darkblue'}
)

fig2.update_traces(marker=dict(size=12))
fig2.update_layout(width=1280,height=720,title_x=0.5)

layout = html.Div([
    dcc.Graph(figure=fig1),
    html.Hr(),
    dcc.Graph(figure=fig2)
])