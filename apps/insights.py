import dash_core_components as dcc
import dash_html_components as html
import os
import itertools
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

import sqlite3

import seaborn as sns

# import dash_alternative_viz as dav
import plotly.express as px
import dash_bio as dashbio

df1 = px.data.iris()


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


# tips = sns.load_dataset("tips")

# styles = {"pre": {"border": "thin lightgrey solid", "overflowX": "scroll"}}

# df = pd.DataFrame(
#     {"x": [1, 2, 1, 2], "y": [1, 2, 3, 4], "customdata": [1, 2, 3, 4], "fruit": ["apple", "apple", "orange", "orange"]}
# )

# fig = px.scatter(df, x="x", y="y", color="fruit", custom_data=["customdata"])

# fig.update_layout(clickmode="event+select")

# fig.update_traces(marker_size=20)

layout = dbc.Container(
    [
        html.Div(
            [
                html.H1("Insights"),
                # dcc.Graph(id="basic-interactions", figure=fig),
                html.H2("MW against Interactivity"),
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
    mask = (df1["petal_width"] > low) & (df1["petal_width"] < high)
    fig = px.scatter(
        df1[mask], x="sepal_width", y="sepal_length", color="species", size="petal_length", hover_data=["petal_width"]
    )
    return fig
