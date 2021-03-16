import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
import os
from Bio import SeqIO

from Bio.Blast.Applications import NcbiblastpCommandline

from app import app


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
