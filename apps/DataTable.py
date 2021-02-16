import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import datetime

from app import app

import pandas as pd


df = pd.read_csv("./peptides.csv")
df = df[['Protein', 'Peptide', 'Base1', 'Base2', 'Base3', 'Base4', 'Base5', 'Base6', 'Base7', 'Base8']]  # prune columns for example

layout = dash_table.DataTable(
    columns=[
        {'name': 'Protein', 'id': 'Protein', 'type': 'text'},
        {'name': 'Peptide', 'id': 'Peptide', 'type': 'text'},
        {'name': 'Base1', 'id': '35a12_90128_1_1_F (F061400)', 'type': 'numeric'},
        {'name': 'Base2', 'id': '35a12_90128_2_1_H (F061401)', 'type': 'numeric'},
        {'name': 'Base3', 'id': '35a12_90128_3_1_L (F061402)', 'type': 'numeric'},
        {'name': 'Base4', 'id': '35a12_90128_3_2_L (F061403)', 'type': 'numeric'},
        {'name': 'Base5', 'id': '35a12_Cu10_1_1_F (F061404)', 'type': 'numeric'},
        {'name': 'Base6', 'id': '35a12_Cu10_2_1_H (F061405)', 'type': 'numeric'},
        {'name': 'Base7', 'id': '35a12_Cu10_3_1_L (F061406)', 'type': 'numeric'},
        {'name': 'Base8', 'id': '35a12_Cu10_3_2_L (F061407)', 'type': 'numeric'}
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