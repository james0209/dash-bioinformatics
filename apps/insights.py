import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import GC, MeltingTemp, GC_skew, seq3
from Bio.SeqUtils.ProtParam import ProteinAnalysis

import sqlite3

import seaborn as sns

# import dash_alternative_viz as dav
import plotly.express as px
import dash_bio as dashbio
import plotly.graph_objects as go
import pandas as pd
from collections import deque

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
# cursor.execute("SELECT bioentry_id, biodatabase_id FROM bioentry")
df = pd.read_sql(
    "SELECT bioentry.bioentry_id, biodatabase_id, seq FROM bioentry, biosequence WHERE bioentry.bioentry_id = biosequence.bioentry_id",
    conn,
)

df["initial"] = df["seq"].apply(ProteinAnalysis)
# df.rename(columns={0: "bioentry_id", 1: "biodatabase_id", 2: "seq"}, inplace=True)
# scores = pd.read_sql("", conn)

conn.close()

layout = dbc.Container(
    [
        html.Div(
            [
                html.H1("Insights"),
                # dcc.Graph(id="basic-interactions", figure=fig),
                html.H2("MW against Interactivity"),
                dcc.Dropdown(
                    id="dropdown",
                    options=[{"label": "A", "value": "A"}, {"label": "B", "value": "B"}],
                    placeholder="Select a Base",
                ),
                dcc.Graph(id="scatter-plot"),
                html.P("Petal Width:"),
                dcc.RangeSlider(
                    id="range-slider", min=0, max=2.5, step=0.1, marks={0: "0", 2.5: "2.5"}, value=[0.5, 2]
                ),
            ]
        ),
    ]
)


@app.callback(Output("scatter-plot", "figure"), [Input("range-slider", "value")])
def update_bar_chart(slider_range):
    low, high = slider_range
    mask = (df["bioentry_id"] > low) & (df["bioentry_id"] < high)
    fig = px.scatter(df[mask], x="bioentry_id", y="biodatabase_id")
    return fig
