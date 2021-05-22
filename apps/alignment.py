import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bio as dashbio

from app import app

# Reads in static FASTA sequence
file = open("assets/alignments.fasta", "r", encoding="utf-8")
alignment_data = file.read()
file.close()

layout = html.Div(
    [
        html.Div(id="container"),
        html.P(children="This component shows alignments of the sequences present in the alignments FASTA file."),
        html.Br(),
        html.P(
            children="The consensus sequence show at the bottom is the calculated order of most frequent residues found at each position."
        ),
        html.Br(),
        html.P(children="The settings for this chart can be adjusted within the alignment.py file of the application."),
        html.Div(
            children=[
                html.Div(
                    className="column is-three-fifths is-centered",
                    children=[
                        dashbio.AlignmentChart(
                            id="fmt_alignment_viewer",
                            data=alignment_data,
                            extension="fasta",  # If your data contains clustal output, turn it into "clustal".
                            showgap=False,
                            showconsensus=True,  # If you would like to just enable alignment part, turn it into False.
                            showconservation=True,  # If you would like to just enable alignment part, turn it into False.
                            tilewidth=20,  # It defines the width of the each amino acid/nucleotid box.
                            tileheight=10,  # It defines the height of the each amino acid/nucleotid box.
                            showid=False,
                            overview=None,  # If you would like to change, turn it into "heatmap" or "slider".
                            height=400,
                            width="95%",
                        ),
                    ],
                ),
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
