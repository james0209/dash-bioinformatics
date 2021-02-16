import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import datetime

from app import app

import pandas as pd

#TODO: Look into having csv as a pandas dataframe and use the derived_filter_query_structure in conjunction with pandas filters
# https://dash.plotly.com/datatable/filtering


df = pd.read_csv("https://raw.githubusercontent.com/james0209/dash-bioinformatics/main/assets/peptides.csv")
df = df[['Protein', 'Peptide', '35a12_90128_1_1_F (F061400)', '35a12_90128_2_1_H (F061401)',
 '35a12_90128_3_1_L (F061402)', '35a12_90128_3_2_L (F061403)', '35a12_Cu10_1_1_F (F061404)',
  '35a12_Cu10_2_1_H (F061405)', '35a12_Cu10_3_1_L (F061406)', '35a12_Cu10_3_2_L (F061407)']]  # prune columns for example

layout = dash_table.DataTable(
    columns=[
        {'name': 'Protein', 'id': 'Protein', 'type': 'text'},
        {'name': 'Peptide', 'id': 'Peptide', 'type': 'text'},
        {'name': '35a12_90128_1_1_F (F061400)', 'id': '35a12_90128_1_1_F (F061400)', 'type': 'numeric'},
        {'name': '35a12_90128_2_1_H (F061401)', 'id': '35a12_90128_2_1_H (F061401)', 'type': 'numeric'},
        {'name': '35a12_90128_3_1_L (F061402)', 'id': '35a12_90128_3_1_L (F061402)', 'type': 'numeric'},
        {'name': '35a12_90128_3_2_L (F061403)', 'id': '35a12_90128_3_2_L (F061403)', 'type': 'numeric'},
        {'name': '35a12_Cu10_1_1_F (F061404)', 'id': '35a12_Cu10_1_1_F (F061404)', 'type': 'numeric'},
        {'name': '35a12_Cu10_2_1_H (F061405)', 'id': '35a12_Cu10_2_1_H (F061405)', 'type': 'numeric'},
        {'name': '35a12_Cu10_3_1_L (F061406)', 'id': '35a12_Cu10_3_1_L (F061406)', 'type': 'numeric'},
        {'name': '35a12_Cu10_3_2_L (F061407)', 'id': '35a12_Cu10_3_2_L (F061407)', 'type': 'numeric'}
    ],
    data=df.to_dict('records'),
    filter_action='native',

    style_table={
        'height': 400,
    },
    style_data={
        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)