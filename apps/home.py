import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

layout = html.Div(
    [
        dbc.Container(
            [
                html.H1(children="Welcome!"),
                html.Div(
                    children="""
                    This web application toolkit contains bioinformatic modules designed for protein visualisation.
                """
                ),
                html.Br(),
                html.A(
                    "Peptide Viewer",
                    style={
                        "color": "green",
                        "text-decoration": "underline",
                        "fontSize": 20,
                    },
                    href="/apps/DataTable",
                    title="Peptide Viewer",
                ),
                html.Div(
                    children="""
                    This interactive table will allows you to browse through the data in your database - giving you the option to
                    filter, sort, or hide data to find what you are looking for.
                """
                ),
                html.Br(),
                html.A(
                    "Sequence Viewer",
                    style={
                        "color": "green",
                        "text-decoration": "underline",
                        "fontSize": 20,
                    },
                    href="/apps/sequenceViewer",
                    title="Sequence Viewer",
                ),
                html.Div(
                    children="""
                    The centre piece of the application. This component will allow you to select any protein from within the databse, and
                    view the assosicated sequence in a way that is easier on the eyes than one long string of characters.
                """
                ),
                html.Br(),
                html.A(
                    "Alignment Viewer",
                    style={
                        "color": "green",
                        "text-decoration": "underline",
                        "fontSize": 20,
                    },
                    href="/apps/alignment",
                    title="Alignment Viewer",
                ),
                html.Div(
                    children="""
                    This application visualises two or more sequences to allow comparison and alignment. This feature could be used
                    to compare the alignments of sequences after running BLAST for example.
                """
                ),
                html.Br(),
                html.A(
                    "Interaction Viewer",
                    style={
                        "color": "green",
                        "text-decoration": "underline",
                        "fontSize": 20,
                    },
                    href="/apps/interactivity",
                    title="Interaction Viewer",
                ),
                html.Div(
                    children="""
                    A nicer approach to visualising interactivity, this application shows the level of interaction between peptides and bases
                    through the use of scatter plots.
                """
                ),
            ]
        ),
    ],
)

# The @app.callback decorator needs to be directly above the callback function declaration.
# @app.callback(Output("my-output", "children"), Input("my-input", "value"))
# def display_value(value):
#    return "Output: {}".format(value)
