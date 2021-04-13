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


def get_peptides(bioentry_id):
    conn = sqlite3.connect("database.db")
    queryPeptides = "SELECT peptide FROM peptides WHERE bioentry_id = ?"
    params = [bioentry_id]
    peptides = pd.read_sql(queryPeptides, conn, params=params)
    conn.close()
    return peptides


def get_bioentries():
    conn = sqlite3.connect("database.db")
    bioentries = pd.read_sql_query("SELECT DISTINCT bioentry_id FROM bioentry", conn)
    conn.close()
    return bioentries


def create_figure(bioentry_id):
    peptides = []

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    query1 = "SELECT bioentry_id, seq FROM biosequence WHERE bioentry_id = ?"
    query2 = "SELECT bioentry_id, peptide FROM peptides WHERE bioentry_id = ?"
    params = [bioentry_id]
    df1 = pd.read_sql(query1, conn, params=params)
    df2 = pd.read_sql(query2, conn, params=params)
    # df2 = pd.read_sql("SELECT bioentry_id, peptide FROM peptides WHERE bioentry_id = ?", 41, conn)

    seq = df1.loc[df1["bioentry_id"] == bioentry_id, "seq"].item()
    # pep = df2.loc[df2["bioentry_id"] == 41, "peptide"].values[0]

    for index, row in df2.iterrows():
        # peptides.append(row["peptide"])
        start = seq.find(row["peptide"])
        end = start + len(row["peptide"])
        peptides.append([start, end, "green"])
    return dashbio.SequenceViewer(
        id="my-sequence-viewer",
        sequence=seq,
    )


df3 = get_bioentries()

layout = html.Div(
    [
        dbc.Container(
            [
                html.Label(
                    [
                        "Bioentry Dropdown",
                        dcc.Dropdown(
                            id="my-dynamic-dropdown",
                            options=[{"label": i, "value": i} for i in df3.bioentry_id.unique()],
                        ),
                    ]
                ),
                html.Div(id="viewer-module"),
                html.Button("Sequence Viewer", id="btn-3"),
                # dashbio.SequenceViewer(id="my-sequence-viewer", sequence=seq, selection=[]),
                html.Div(id="sequence-viewer-output"),
                dcc.RadioItems(
                    id="peptide-radio",
                    labelStyle={"display": "block"},
                    options=[],
                ),
            ]
        ),
    ]
)


@app.callback(
    dash.dependencies.Output("my-dynamic-dropdown", "options"),
    [dash.dependencies.Input("my-dynamic-dropdown", "search_value")],
)
def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    else:
        return search_value


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
    [
        dash.dependencies.Input("btn-3", "n_clicks"),
        dash.dependencies.Input("my-dynamic-dropdown", "value"),
    ],
)
def display_value(n_clicks, bioentry_id):
    if n_clicks is None:
        raise PreventUpdate
    else:
        if bioentry_id is not None:
            return create_figure(bioentry_id)
        else:
            raise PreventUpdate


@app.callback(
    dash.dependencies.Output("peptide-radio", "options"),
    [
        dash.dependencies.Input("my-dynamic-dropdown", "value"),
        dash.dependencies.Input("btn-3", "n_clicks"),
    ],
)
def display_peptides(bioentry_id, n_clicks):
    if bioentry_id is None:
        return []
    else:
        if n_clicks is None:
            return []
        else:
            peptides = get_peptides(bioentry_id)
            new_options = [{"label": i, "value": i} for i in peptides.peptide.unique()]
            return new_options


@app.callback(
    dash.dependencies.Output("my-sequence-viewer", "selection"),
    [
        dash.dependencies.Input("peptide-radio", "value"),
        dash.dependencies.Input("my-sequence-viewer", "sequence"),
    ],
)
def highlightPeptide(radioSelection, sequence):
    if radioSelection is None:
        return []
    else:

        start = sequence.find(radioSelection)
        end = start + len(radioSelection)
        peptides = [start, end, "green"]
        return peptides


if __name__ == "__main__":
    app.run_server(debug=True)
