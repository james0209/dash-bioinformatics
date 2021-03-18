import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
from Bio import SeqIO
import dash_bio as dashbio

from Bio.Blast.Applications import NcbiblastpCommandline

from app import app

alignment_data = open("./SubsetDatabase1.fasta", "r", encoding="utf-8").read()


@app.callback(Output("loading-output-2", "children"), [Input("btn-2", "n_clicks")])
def localBlast(n_clicks):
    if n_clicks is not None:
        blastp_cline = NcbiblastpCommandline(
            cmd="blastp", query="SubsetDatabase1.fasta", db="fulldb", evalue=0.001, outfmt=5, out="local_blast.xml"
        )
        blastp_cline()
        print("Succesfully saved to local_blast.xml")
        # NcbiblastpCommandline(cmd="blastp", out="opuntia.xml", outfmt=5, query="opuntia.fasta", db="nr", evalue=0.001)
        # print(blastp_cline)


layout = html.Div(
    [
        html.Div(id="container"),
        html.Div(id="onlineBlast-output"),
        html.Div(
            [
                dcc.Upload(
                    id="upload-data",
                    children=html.Div(["Drag or drop or ", html.A("Select a file")]),
                    style={
                        "width": "100%",
                        "height": "60px",
                        "lineHeight": "60px",
                        "borderWidth": "1px",
                        "borderStyle": "dashed",
                        "borderRadius": "5px",
                        "textAlign": "center",
                    },
                ),
                html.Div(id="output-data-upload"),
            ]
        ),
        html.Button("Run Local Blast", id="btn-2"),
        dcc.Loading(id="loading-2", type="default", children=html.Div(id="loading-output-2")),
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


@app.callback(
    Output("output-data-upload", "children"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    State("upload-data", "last_modified"),
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        input_seq_iterator = SeqIO.parse("SubsetDatabase10.fasta", "fasta")
        localBlast()


if __name__ == "__main__":
    app.run_server(debug=True)
