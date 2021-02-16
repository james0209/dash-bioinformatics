import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bio as dashbio
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import os
import itertools

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

from apps import proteinReader as pr

seq = "ABCD"

layout = html.Div([
    dbc.Container([
    dashbio.SequenceViewer(
        id='my-sequence-viewer',
        sequence=seq
    ),
    html.Div(id='sequence-viewer-output')
    ]),
])


@app.callback(
    dash.dependencies.Output('sequence-viewer-output', 'children'),
    [dash.dependencies.Input('my-sequence-viewer', 'mouseSelection')]
)
def update_output(value):
    if value is None or len(value) == 0:
        return 'There is no mouse selection.'
    return 'The mouse selection is {}.'.format(value['selection'])


if __name__ == '__main__':
    app.run_server(debug=True)