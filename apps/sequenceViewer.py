import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bio as dashbio
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3
import array as arr
from dash.exceptions import PreventUpdate

from app import app

# seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# TODO: Currently it is trying to load selections before it has been populated. Add this to callback perhaps?

layout = html.Div(
    [
        dbc.Container(
            [
                html.Div(id="viewer-module"),
                html.Button("Sequence Viewer", id="btn-3"),
                # dashbio.SequenceViewer(id="my-sequence-viewer", sequence=seq, selection=[]),
                html.Div(id="sequence-viewer-output"),
            ]
        ),
    ]
)


@app.callback(
    dash.dependencies.Output("sequence-viewer-output", "children"),
    [dash.dependencies.Input("my-sequence-viewer", "mouseSelection")],
)
def update_output(value):
    if value is None or len(value) == 0:
        return "There is no mouse selection."
    return "The mouse selection is {}.".format(value["selection"])


@app.callback(
    dash.dependencies.Output("viewer-module", "children"),
    [dash.dependencies.Input("btn-3", "n_clicks")],
)
def display_value(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        peptides = []

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        df1 = pd.read_sql("SELECT bioentry_id, seq FROM biosequence WHERE bioentry_id = 41", conn)
        df2 = pd.read_sql("SELECT bioentry_id, peptide FROM peptides WHERE bioentry_id = 41", conn)

        seq = df1.loc[df1["bioentry_id"] == 41, "seq"].item()
        # pep = df2.loc[df2["bioentry_id"] == 41, "peptide"].values[0]

        for index, row in df2.iterrows():
            # peptides.append(row["peptide"])
            start = seq.find(row["peptide"])
            end = start + len(row["peptide"])
            peptides.append([start, end, "green"])
        return dashbio.SequenceViewer(id="my-sequence-viewer", sequence=seq, selection=peptides[1])


if __name__ == "__main__":
    app.run_server(debug=True)
