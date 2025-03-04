import dash
from dash import html, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from pynput import mouse
from tictactoe_def import *

board = [None, None, None, None, None, None, None, None, None]

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
        
