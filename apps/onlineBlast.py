import dash_core_components as dcc
import dash_html_components as html
import os
import itertools
from dash.dependencies import Input, Output

from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import pairwise2
from Bio import File
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import GC,MeltingTemp,GC_skew,seq3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import plotly.figure_factory as ff

from app import app
from apps import home, app2, onlineBlast, sequenceViewer      

blast_results = []

def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/onlineBlast.py':
        fasta_string = open("SubsetDatabase1.fasta").read()
        print("Got here")
        result_handle = NCBIWWW.qblast("blastp", "nr", fasta_string)
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

                    #blast_results=([
                    #html.H6("****Alignment****"),
                    #html.H6("sequence:", alignment.title),
                    #html.H6("length:", alignment.length),
                    #html.H6("e value:", hsp.expect),
                    #html.H6(hsp.query[0:75] + "..."),
                    #html.H6(hsp.match[0:75] + "..."),
                    #html.H6(hsp.sbjct[0:75] + "...")
                    #])
    else:
        return '404'
        


layout = html.Div([
    blast_results,
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div(["Input: ",
              dcc.Input(id='onlineBlast-input', value='initial value', type='text')]),
    html.Br(),
    html.Div(id='onlineBlast-output'),
])

#The @app.callback decorator needs to be directly above the callback function declaration.
@app.callback(
    Output('onlineBlast-output', 'children'),
    Input('onlineBlast-input', 'value'))
def display_value(value):
    return 'Output: {}'.format(value)