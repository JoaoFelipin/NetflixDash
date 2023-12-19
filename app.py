from dash import Dash, dash_table, html,dcc
import dash_bootstrap_components as dbc

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dcc.Store(id='store'),
    html.H1('Netflix Dashboard'),
    html.Hr(),
    dbc.Tabs([
        dbc.Tab(label='Distribuição geográfica de conteúdo',tab_id='tab1'),
        dbc.Tab(label='Classificação de conteúdo',tab_id='tab2'),
        
    ],
             id='tabs',active_tab='tab1'),
    html.Div(id='tab-content',className='p-4'),

])

if __name__ == '__main__':
    app.run_server(debug=True)
    