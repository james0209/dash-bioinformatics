import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from pandas._config.config import options
from dash.exceptions import PreventUpdate

from app import app

import sqlite3

import plotly.express as px
import pandas as pd


def getScores():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    df = pd.read_sql_query(
        "SELECT f061400, f061401, f061402, f061403, f061404, f061405, f061406, f061407 FROM peptides", conn
    )
    options = []
    for col in df.columns:
        options.append({"label": "{}".format(col, col), "value": col})
    # df = pd.DataFrame(c.fetchall(), columns=['Brand','Price'])
    conn.close()
    return options


def create_figure(base):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    # resoverall = cur.execute("SELECT peptide, '%s' FROM peptides" % base)
    # df = DataFrame(resoverall.fetchall())
    query1 = "SELECT peptide, %s FROM peptides" % base
    df = pd.read_sql(query1, conn)

    data = px.scatter(df, x="peptide", y=base)
    return data


options = getScores()

layout = dbc.Container(
    [
        html.Div(
            [
                html.H1("Insights"),
                html.Label(
                    [
                        "Base Dropdown",
                        dcc.Dropdown(
                            id="base-dropdown",
                            options=options,
                        ),
                    ]
                ),
                html.Label(id="my_label1"),
                html.Button("Show Plot", id="plot-btn"),
            ]
        ),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(
    Output("graph", "figure"),
    Input("plot-btn", "n_clicks"),
    Input("base-dropdown", "value"),
)
def show_graph(n_clicks, base):
    if n_clicks is None:
        raise PreventUpdate
    else:
        if base is not None:
            return create_figure(base)
        else:
            raise PreventUpdate
