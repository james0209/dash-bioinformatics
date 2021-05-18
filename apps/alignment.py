import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from Bio import SeqIO
import dash_bio as dashbio
import base64

from Bio.Blast.Applications import NcbiblastpCommandline

from app import app

alignment_data = open("./SubsetDatabase1.fasta", "r", encoding="utf-8").read()

layout = html.Div(
    [
        html.Div(id="container"),
        html.Div(
            children=[
                html.Div(
                    className="column is-three-fifths is-centered",
                    children=[
                        # Here is alignment chart!
                        dashbio.AlignmentChart(
                            id="fmt_alignment_viewer",
                            data=alignment_data,
                            extension="fasta",  # If your data contains clustal output, turn it into "clustal". # If yo would like to change the color schema, work on here.
                            showgap=False,
                            showconsensus=True,  # If you would like to just enable alignment part, turn it into False.
                            showconservation=False,  # If you would like to just enable alignment part, turn it into False.
                            tilewidth=20,  # It defines the width of the each amino acid/nucleotid box.
                            tileheight=10,  # It defines the height of the each amino acid/nucleotid box.
                            showid=False,
                            overview=None,  # If you would like to change, turn it into "heatmap" or "slider".
                            height=200,
                            width="95%",
                        ),  # ends of alignment chart
                    ],
                ),
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
