import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

layout = html.Div(
    [
        dbc.Container(
            [
                dcc.Checklist(
                    options=[
                        {"label": "Only show proteins with length higher than ", "value": "protLengthOption"},
                    ],
                    value=["protLengthOption"],
                ),
                dcc.Input(
                    id="dtrue",
                    type="number",
                    debounce=True,
                    placeholder="Protein Length",
                ),
                # html.H6("Change the value in the text box to see callbacks in action!"),
                # html.Div(["Input: ", dcc.Input(id="my-input", value="initial value", type="text")]),
                # html.Br(),
                # html.Div(id="my-output"),
            ]
        ),
    ],
)

# The @app.callback decorator needs to be directly above the callback function declaration.
# @app.callback(Output("my-output", "children"), Input("my-input", "value"))
# def display_value(value):
#    return "Output: {}".format(value)
