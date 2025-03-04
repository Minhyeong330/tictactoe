import dash
from dash import html, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from pynput import mouse

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def make_button(button_id):
    return dbc.Col(
        html.Button(
            " ",
            id=button_id,  # Unique ID for each button
            n_clicks=0,  # Tracks the number of clicks
            style={
                "font-size": "24px", 
                "width": "60px", 
                "height": "60px", 
                "text-align": "center"
            }
        ), 
        width=1
    )

app.layout = dbc.Container([
    dbc.Row([
        make_button("bnt-1"), # each bnt-(n) = id
        make_button("bnt-2"),
        make_button("bnt-3")
    ]),
    dbc.Row([
        make_button("bnt-4"),
        make_button("bnt-5"),
        make_button("bnt-6")
    ]),
    dbc.Row([
        make_button("bnt-7"),
        make_button("bnt-8"),
        make_button("bnt-9")
    ])
])

# Callback to toggle button text between "X" and "O" - Got this from Chatgpt (Frontend)
@app.callback(
    [Output(f"bnt-{i}", "children") for i in range(1, 10)],
    [Input(f"bnt-{i}", "n_clicks") for i in range(1, 10)],
    prevent_initial_call=True
)
def update_buttons(*n_clicks):
    # Determine the button clicked
    button_states = [("X" if n % 2 == 1 else "O") if n else " " for n in n_clicks]
    if "bnt-1" == 'O' and "bnt-2" == 'O' and "bnt-3" == 'O':
        button_states = " "
    return button_states


if __name__ == "__main__":
    app.run_server(debug=True)