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