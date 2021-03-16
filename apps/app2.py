import dash_core_components as dcc
import dash_html_components as html
import os
import itertools
from dash.dependencies import Input, Output
import functools
import operator

from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import pairwise2
from Bio import File
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import GC, MeltingTemp, GC_skew, seq3
from BioSQL import BioSeqDatabase

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import plotly.figure_factory as ff

from app import app

import sqlite3
import dash_table

import seaborn as sns

# import dash_alternative_viz as dav
import plotly.express as px
import dash_bio as dashbio

# record_dict = SeqIO.index("SubsetDatabase10.fasta", "fasta")
# input_seq_iterator = SeqIO.parse("SubsetDatabase10.fasta", "fasta")

# server = BioSeqDatabase.open_database(driver="sqlite3", db="database.db")
# db = server.new_database("proteins", description="Proteins from FASTA")
# count = db.load(SeqIO.parse("SubsetDatabaseFull.fasta", "fasta"))
# print("Loaded %i records" % count)

# server.commit()
# server.close()

""" conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")

df = pd.read_sql("SELECT * FROM users", conn)



        dash_table.DataTable(
            id="table",
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
        ), """


tips = sns.load_dataset("tips")

styles = {"pre": {"border": "thin lightgrey solid", "overflowX": "scroll"}}

df = pd.DataFrame(
    {"x": [1, 2, 1, 2], "y": [1, 2, 3, 4], "customdata": [1, 2, 3, 4], "fruit": ["apple", "apple", "orange", "orange"]}
)

fig = px.scatter(df, x="x", y="y", color="fruit", custom_data=["customdata"])

fig.update_layout(clickmode="event+select")

fig.update_traces(marker_size=20)

layout = (
    html.Div(
        [
            html.H1("Hello Dash"),
            dcc.Graph(id="basic-interactions", figure=fig),
        ]
    ),
)
# The @app.callback decorator needs to be directly above the callback function declaration.
@app.callback(Output("app2-output", "children"), Input("app2-input", "value"))
def display_value(value):
    return "Output: {}".format(value)
