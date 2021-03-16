import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bio as dashbio
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from Bio import SeqIO
from Bio import pairwise2
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import GC, MeltingTemp, GC_skew, seq3

from app import app

from apps import proteinReader as pr

seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

layout = html.Div(
    [
        dbc.Container(
            [
                dashbio.SequenceViewer(id="my-sequence-viewer", sequence=seq),
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


if __name__ == "__main__":
    app.run_server(debug=True)
