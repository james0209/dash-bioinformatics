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
alignment_data = open("./SubsetDatabase1.fasta", "r", encoding="utf-8").read()

layout = html.Div(
    [
        dbc.Container(
            [
                dashbio.SequenceViewer(id="my-sequence-viewer", sequence=seq),
                html.Div(id="sequence-viewer-output"),
                # Sequence Viewer Component
                # https://dash.plot.ly/dash-bio/alignmentchart
                html.Div(
                    children=[
                        html.Div(
                            className="column is-three-fifths is-centered",
                            children=[
                                # Here is alignment chart!
                                dashbio.AlignmentChart(
                                    id="fmt_alignment_viewer",
                                    data=alignment_data,
                                    extension="fasta",  # If your data contains clustal output, turn it into "clustal".
                                    colorscale="clustal2",  # If yo would like to change the color schema, work on here.
                                    showgap=False,
                                    showconsensus=True,  # If you would like to just enable alignment part, turn it into False.
                                    showconservation=False,  # If you would like to just enable alignment part, turn it into False.
                                    tilewidth=20,  # It defines the width of the each amino acid/nucleotid box.
                                    tileheight=20,  # It defines the height of the each amino acid/nucleotid box.
                                    showid=False,
                                    overview=None,  # If you would like to change, turn it into "heatmap" or "slider".
                                    height=490,
                                    width="95%",
                                ),  # ends of alignment chart
                            ],
                        ),
                    ],
                ),
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
