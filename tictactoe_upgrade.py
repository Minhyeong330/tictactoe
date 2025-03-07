import dash
from dash import dcc, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Tic-Tac-Toe board state
board = [None] * 9
current_player = "O"

# Define the layout
app.layout = html.Div([              #Define Division
    html.H1("Tic-Tac-Toe Game Board"),  #H1 - Headline 1 = The order of headline
    html.Div(               #This division is for button
        [
            html.Button(        #For button
                " ",            #Default value of the button
                id=f"cell-{i}", #Assign Button id
                n_clicks=0,     #The # of clicks
                style={         #Define the style of the board - Location of the button
                    "width": "80px",
                    "height": "80px",
                    "font-size": "24px",
                    "margin": "5px"
                }
            )
            for i in range(9) #Array[0~8] because I need 9 buttons on the board
        ],
        style={"display": "grid", "grid-template-columns": "repeat(3, 1fr)"} # Button Style - CSS Styling dictionary / # grid-template-columns : repeat(3, 1fr) => 1fr(hard to understand) = 1 fraction of the available space, making all colums equal in width
    ),
    html.H2(id="winner-text", children="Player O's Turn"),  # Display game status - Headline 2
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
    if None not in board: # the board is full = None not in board, but there is no winner
        return "Tie"  # If the board is full and no winner, it's a tie
    return None  # No winner yet

# Callback to handle player moves
@app.callback(
    Output("board-store", "data"),
    Output("player-store", "data"),
    Output("winner-text", "children"),
    [Output(f"cell-{i}", "children") for i in range(9)], # list comprehension - make better readability
    [Input(f"cell-{i}", "n_clicks") for i in range(9)], # list comprehension -> args[0~8]
    Input("reset-btn", "n_clicks"),  # Reset button input -> args[9] = args[-3]
    State("board-store", "data"), # -> args[10] = args[-2]
    State("player-store", "data"), # -> args[11] = args[-1]
    prevent_initial_call=True
)
def update_board(*args): # args
    board = args[-2]  # Retrieve current board state
    current_player = args[-1]  # Retrieve current player
    reset_clicks = args[-3]  # Reset button clicks
    triggered_id = ctx.triggered_id  # Get which button was clicked

    # Reset game when reset button is clicked
    if "reset-btn" in triggered_id: # stores the ID of the component that triggered the callback
        return [None] * 9, "O", "Player O's Turn", *[" "] * 9 # Resets the board (9 empty spaces) "O" = Sets player O as the next turn

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