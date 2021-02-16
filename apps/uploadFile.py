import dash_core_components as dcc
import dash_html_components as html
import os
import itertools
from dash.dependencies import Input, Output, State

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
import base64
import datetime
import io
import tempfile

from app import app
from apps import proteinReader as pr

#https://github.com/plotly/dash-bio-utils/blob/master/dash_bio_utils/protein_reader.py
#https://github.com/plotly/dash-bio/blob/master/tests/dashbio_demos/dash-sequence-viewer/app.py

record_dict = SeqIO.index("SubsetDatabase10.fasta", "fasta")
input_seq_iterator = SeqIO.parse("SubsetDatabase10.fasta", "fasta")


layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])

@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'value'))
def display_value(upload_contents):
    data = ""
    try:
        content_type, content_string = upload_contents.split(',')
        data = base64.b64decode(content_string).decode('UTF-8')

    except AttributeError:
        pass
    proteins = pr.read_fasta(data, is_datafile=False)
    return 'Output: {}'.format(upload_contents)