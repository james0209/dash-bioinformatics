import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

layout = html.Div(
    [
        dbc.Container(
            [
                html.H1(children="Contact"),
                html.Div(
                    children="""
                    This application was created by James Brookes - a BSc Computer Science student at the University of East Anglia.
                """
                ),
                html.Br(),
                html.Div(children="Thank you to the community working on BioPython, Dash, and Plotly."),
            ]
        ),
    ],
)

# The @app.callback decorator needs to be directly above the callback function declaration.
# @app.callback(Output("my-output", "children"), Input("my-input", "value"))
# def display_value(value):
#    return "Output: {}".format(value)
