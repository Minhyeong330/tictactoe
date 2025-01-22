import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

def make_button():
    new_button = dbc.Col(html.Div(html.Button(".")), width=1)
    return new_button

app.layout = dbc.Container([
    dbc.Row([
        make_button(),
        make_button(),
        make_button()
    ]),
    dbc.Row([
        make_button(),
        make_button(),
        make_button()
    ]),
    dbc.Row([
        make_button(),
        make_button(),
        make_button()
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)