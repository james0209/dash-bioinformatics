# Dot Plot (Bioinformatics)
# Use for the CSV of Peptides - Base interactions
# Show tooltip on hover showing the score
# Have the dot be a darker colour if higher score

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bio as dashbio
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_html_components.H1 import H1

import matplotlib.pyplot as plt

from app import app

# Read in CSV

layout = html.Div(
    [
        dbc.Container(
            [
                html.H1("Dot Plot"),
            ]
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
