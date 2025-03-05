import dash
from dash import dcc, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Tic-Tac-Toe board state
board = [None] * 9
current_player = "O"

# Define the layout
app.layout = html.Div([
    html.H2("Tic-Tac-Toe"),
    html.Div(
        [
            html.Button(
                " ",
                id=f"cell-{i}",
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
    html.H3(id="winner-text", children="Player O's Turn"),  # Display game status
    html.Button("Reset", id="reset-btn", n_clicks=0, style={"margin-top": "10px"}),
    dcc.Store(id="board-store", data=board),  # Store board state
    dcc.Store(id="player-store", data=current_player),  # Store current player
])

# Function to check for a winner
def check_winner(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]  # Return winner ("O" or "X")
    if None not in board:
        return "Tie"  # If the board is full and no winner, it's a tie
    return None  # No winner yet

# Callback to handle player moves
@app.callback(
    Output("board-store", "data"),
    Output("player-store", "data"),
    Output("winner-text", "children"),
    Output("cell-0", "children"), Output("cell-1", "children"), Output("cell-2", "children"),
    Output("cell-3", "children"), Output("cell-4", "children"), Output("cell-5", "children"),
    Output("cell-6", "children"), Output("cell-7", "children"), Output("cell-8", "children"),
    Input("cell-0", "n_clicks"), Input("cell-1", "n_clicks"), Input("cell-2", "n_clicks"),
    Input("cell-3", "n_clicks"), Input("cell-4", "n_clicks"), Input("cell-5", "n_clicks"),
    Input("cell-6", "n_clicks"), Input("cell-7", "n_clicks"), Input("cell-8", "n_clicks"),
    Input("reset-btn", "n_clicks"),  # Reset button input
    State("board-store", "data"),
    State("player-store", "data"),
    prevent_initial_call=True
)
def update_board(*args):
    board = args[-2]  # Retrieve current board state
    current_player = args[-1]  # Retrieve current player
    reset_clicks = args[-3]  # Reset button clicks
    triggered_id = ctx.triggered_id  # Get which button was clicked

    # Reset game when reset button is clicked
    if "reset-btn" in triggered_id:
        return [None] * 9, "O", "Player O's Turn", *[" "] * 9

    # Identify clicked cell
    cell_index = int(triggered_id.split("-")[1])
    
    # If cell is already filled, ignore the click
    if board[cell_index] is not None:
        return board, current_player, f"Player {current_player}'s Turn", *[x if x else " " for x in board]

    # Update the board with the current player's move
    board[cell_index] = current_player

    # Check if there is a winner
    winner = check_winner(board)
    if winner:
        if winner == "Tie":
            return [None] * 9, "O", "It's a Tie! Resetting board...", *[" "] * 9
        return [None] * 9, "O", f"Player {winner} Wins! Resetting board...", *[" "] * 9

    # Switch players
    next_player = "X" if current_player == "O" else "O"

    return board, next_player, f"Player {next_player}'s Turn", *[x if x else " " for x in board]

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
