import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output

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
        html.Button("Run Local Blast", id="btn-2"),
        dcc.Loading(id="loading-2", type="default", children=html.Div(id="loading-output-2")),
        html.Div(id="container"),
        html.Div(id="onlineBlast-output"),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
