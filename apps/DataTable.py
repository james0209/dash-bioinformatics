import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

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

layout = dbc.Container(
    [
        html.Div(
            [
                dcc.Checklist(
                    options=[
                        {"label": " Only show proteins with length higher than ", "value": "protLengthOption"},
                    ],
                ),
                dcc.Input(
                    id="dtrue",
                    type="number",
                    debounce=True,
                    placeholder="Protein Length",
                ),
                html.Br(),
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
