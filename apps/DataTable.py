import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app

import pandas as pd
import sqlite3

# TODO: Look into having csv as a pandas dataframe and use the derived_filter_query_structure in conjunction with pandas filters
# https://dash.plotly.com/datatable/filtering

# TODO: Make the Protein names href and link to the Protein Visulization page, passing the name as a paramter? To link them together

# TODO: Use State to pass data between callbacks and apps

conn = sqlite3.connect("database.db")
c = conn.cursor()
# df = pd.DataFrame(c.fetchall(), columns=['Brand','Price'])
dataframe = pd.read_sql("SELECT * FROM peptides", conn)
# dataframe = pd.transforms.dataframe


df = pd.read_csv("https://raw.githubusercontent.com/james0209/dash-bioinformatics/main/assets/peptides.csv")
df = df[
    [
        "Protein",
        "Peptide",
        "35a12_90128_1_1_F (F061400)",
        "35a12_90128_2_1_H (F061401)",
        "35a12_90128_3_1_L (F061402)",
        "35a12_90128_3_2_L (F061403)",
        "35a12_Cu10_1_1_F (F061404)",
        "35a12_Cu10_2_1_H (F061405)",
        "35a12_Cu10_3_1_L (F061406)",
        "35a12_Cu10_3_2_L (F061407)",
    ]
]  # prune columns for example

layout = dbc.Container(
    [
        html.Div(
            [
                dash_table.DataTable(
                    id="datatable-interactivity",
                    columns=[{"name": i, "id": i} for i in dataframe.columns],
                    data=dataframe.to_dict("records"),
                    filter_action="native",
                    style_data={
                        "overflow": "hidden",
                        "textOverflow": "ellipsis",
                    },
                    editable=False,
                    sort_action="native",
                    sort_mode="multi",
                    column_selectable="single",
                    row_selectable="multi",
                    row_deletable=True,
                    selected_columns=[],
                    selected_rows=[],
                    page_action="native",
                    page_current=0,
                    page_size=15,
                    fill_width=False,
                ),
            ]
        )
    ]
)


@app.callback(
    Output("datatable-interactivity", "style_data_conditional"), Input("datatable-interactivity", "selected_columns")
)
def update_styles(selected_columns):
    return [{"if": {"column_id": i}, "background_color": "#D2F3FF"} for i in selected_columns]


if __name__ == "__main__":
    app.run_server(debug=True)
