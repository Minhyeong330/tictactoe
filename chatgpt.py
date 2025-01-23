import dash
from dash import html, Input, Output, State, ctx
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Function to create a button with an ID
def make_button(button_id):
    return dbc.Col(
        html.Button(
            ".", 
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

# Layout with unique button IDs
app.layout = dbc.Container([
    dbc.Row([
        make_button("button-1"),
        make_button("button-2"),
        make_button("button-3")
    ]),
    dbc.Row([
        make_button("button-4"),
        make_button("button-5"),
        make_button("button-6")
    ]),
    dbc.Row([
        make_button("button-7"),
        make_button("button-8"),
        make_button("button-9")
    ])
], style={"text-align": "center", "margin-top": "50px"})

# Callback to toggle button text between "X" and "O"
@app.callback(
    [Output(f"button-{i}", "children") for i in range(1, 10)],
    [Input(f"button-{i}", "n_clicks") for i in range(1, 10)],
    prevent_initial_call=True
)
def update_buttons(*n_clicks):
    # Determine the button clicked
    button_states = [("X" if n % 2 == 1 else "O") if n else "." for n in n_clicks]
    return button_states

if __name__ == "__main__":
    app.run_server(debug=True)
