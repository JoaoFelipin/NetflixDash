from dash import Dash, dash_table, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Netflix Dashboard'),
    html.Hr(),
])

if __name__ == '__main__':
    app.run_server(debug=True)
    