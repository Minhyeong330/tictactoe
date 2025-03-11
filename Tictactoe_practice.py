import dash
from dash import dcc, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

board = [None] * 9
current_player = "O"

app.layout = html.Div([
    html.H1("Tic-Tac-Toe Game Board"),
    html.Div(
        [
            html.Button(
                " ",
                id = f"cell-{i}",
                n_clicks=0,
                style={
                    "width": "80px",
                    "height": "80px",
                    "font-size": "24px",
                    "margin": "5px"
                }
            )
            for i in range(9)
        ],
        style={"display": "grid", "grid-template-columns": "repeat(3, 1fr)"}
    ),
    html.H2(id="winner-text", children="Player O's Turn"),
    html.Button("Reset", id="reset-btn", n_clicks=0, style={"margin-top": "10px"}),
    dcc.Store(id="board-store", data=board),
    dcc.Store(id="player-store", data=current_player),
])

def check_winner(board): # helper function
    # Need to check 3 things
    # 1. If someone win, who won the game
    # 2. If Tie
    # 3. The game keeps going
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8), #Rows
        (0,3,6), (1,4,7), (2,5,8), #Columns
        (0,4,8), (2,4,6) #Diagonals
    ]
    # who won the game
    for a, b, c in win_conditions:
        if board[a] and board[a] == board[b] == board[c]: # a, b, c = "O" or "X"
            return board[a]
        # why not else? - because winner-conditions only needs for loop (a, b, c)
    # Tie
    if None not in board:
        return "Tie" # There is no None in the board, but no winner => Tie
    # The game keeps going
    return None # Because this function only shows winner, tie, gamg is going (No winner yet = None)

@app.callback(
    Output("board-store", "data"),
    Output("player-store", "data"),
    Output("winner-text", "children"), # we want to update contexts dynamically -> use children
    *[Output(f"cell-{i}", "children") for i in range(9)],
    *[Input(f"cell-{i}", "n_clicks") for i in range(9)],
    Input("reset-btn", "n_clicks"),
    State("board-store", "data"),
    State("player-store", "data"),
    prevent_initial_call=True
)

def update_board(*args): # main function [callback function] tied with @callback
    board = args[-2]
    reset_clicks = args [-3]
    current_player = args[-1]
    triggered_id = ctx.triggered_id

    if "reset-btn" in triggered_id:
        return [None] * 9, "O", "Reset button was cliked. Player O's Turn", *[" "] * 9
    
    cell_index = int(triggered_id.split("-")[1])

    if board[cell_index] is not None:
        return board, current_player, f"Player {current_player}'s Turn", *[x if x else " " for x in board]
    
    board[cell_index] = current_player

    winner = check_winner(board)
    if winner:
        if winner == "Tie":
            return [None] * 9, "O", "It's a Tie. Resetting the board", *[" "] * 9
        return [None] * 9, "O", f"Player {winner} Wins. Resetting the board", *[" "] * 9
    
    next_player = "X" if current_player == "O" else "O"
    # Error reason
    # Original code was ["X" if current_player == "O" else "O"]
    # This makes list because the code is within []
    # However, dcc.store is storing a string. That's why the previous code didn't work well. 
    # ***Important part is list comprehension makes list, not string + dcc.store is storing a string.

    return board, next_player, f"Player {next_player}'s Turn", *[x if x else " " for x in board]


if __name__=="__main__":
    app.run_server(debug=True)