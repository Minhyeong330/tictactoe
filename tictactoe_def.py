import dash
from dash import html, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from pynput import mouse

def mouse_click(button, pressed):
    if pressed:
        if button == mouse.Button.left:
            return "O"
        if button == mouse.Button.right:
            return "X"

def count_clicks(pressed, n_click):
    if pressed:
        n_click == 0
        if mouse.Button.left:
            n_click += 1
            return n_click
        if mouse.Button.right:
            n_click += 1
            return n_click
        
def check_winner():
    # Horizontal 'O'
    if (board[0] == 'O' and board[1] == 'O' and board[2] == 'O' or
        board[3] == 'O' and board[4] == 'O' and board[5] == 'O' or
        board[6] == 'O' and board[7] == 'O' and board[8] == 'O'):
        return 'Player 1 win'
    # Vertical 'O'    
    elif (board[0] == 'O' and board[3] == 'O' and board[6] == 'O' or
        board[1] == 'O' and board[4] == 'O' and board[7] == 'O' or
        board[2] == 'O' and board[5] == 'O' and board[8] == 'O'):
        return 'Player 1 win'
    # Diagonal 'O'
    elif (board[0] == 'O' and board[4] == 'O' and board[8] == 'O' or
        board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
        return 'Player 1 win'
    # Horizontal 'X'
    elif (board[0] == 'X' and board[1] == 'X' and board[2] == 'X' or
        board[3] == 'X' and board[4] == 'X' and board[5] == 'X' or
        board[6] == 'X' and board[7] == 'X' and board[8] == 'X'):
        return 'Player 2 win'
    # Vertical 'X'
    elif (board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or
        board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or
        board[2] == 'X' and board[5] == 'X' and board[8] == 'X'):
        return 'Player 2 win'
    # Diagonal 'X'
    elif (board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or
        board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
        return 'Player 2 win'
