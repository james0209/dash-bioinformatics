import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output
import time

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

from app import app

blast_results = []


@app.callback(Output("loading-output-1", "children"), [Input("btn-1", "n_clicks")])
def input_triggers_spinner(value):
    time.sleep(1)
    return value


@app.callback(Output("onlineBlast-output", "children"), [Input("btn-1", "n_clicks")])
def runBlast(n_clicks):
    if n_clicks is not None:
        fasta_string = open("SubsetDatabase1.fasta").read()
        print("Got here")
        result_handle = NCBIWWW.qblast("blastp", "nr", fasta_string)
        print("got here as well")
        blast_record = NCBIXML.read(result_handle)
        print("Got here2")
        # Setting the E value to parse with
        E_VALUE_THRESH = 0.05
        # Iterating through the alignments returned
        for alignment in blast_record.alignments:
            # Iterating through the high sequence pairs
            for hsp in alignment.hsps:
                # If the E value for the HSP is higher than the threshhold, print information about HSP
                if hsp.expect < E_VALUE_THRESH:

                    print("Yep")

                    blast_results = [
                        html.H6("****Alignment****"),
                        html.H6("sequence: " + alignment.title),
                        html.H6("length: " + str(alignment.length)),
                        html.H6("e value: " + hsp.expect),
                        html.H6(hsp.query[0:75] + "..."),
                        html.H6(hsp.match[0:75] + "..."),
                        html.H6(hsp.sbjct[0:75] + "..."),
                    ]
                    return blast_results


layout = html.Div(
    [
        html.Button("Run Online Blast", id="btn-1"),
        dcc.Loading(id="loading-1", type="default", children=html.Div(id="loading-output-1")),
        html.Div(id="container"),
        html.Div(id="onlineBlast-output"),
    ]
)


""" @app.callback(Output("container", "children"), Input("btn-1", "n_clicks"))
def display(btn1):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = "No clicks yet"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        runBlast(True)
        return html.Div([html.H1("Running BLAST...")])

    return html.Div(
        [
            html.Table(
                [
                    html.Tr([html.Th("Button 1"), html.Th("Most Recent Click")]),
                    html.Tr([html.Td(btn1 or 0), html.Td(button_id)]),
                ]
            ),
        ]
    ) """
