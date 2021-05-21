import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from app import app

import pandas as pd
import sqlite3

# Fetch all peptides from db into dataframe
conn = sqlite3.connect("database.db")
c = conn.cursor()
dataframe = pd.read_sql("SELECT * FROM peptides", conn)
conn.close()

layout = dbc.Container(
    [
        html.Div(
            [
                dash_table.DataTable(
                    id="datatable-interactivity",
                    # Loop through dataframe, creating a column for each df column
                    columns=[{"name": i, "id": i} for i in dataframe.columns],
                    # Convert dataframe to dict as pass as data argument
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
    Output("datatable-interactivity", "style_data_conditional"),
    Input("datatable-interactivity", "selected_columns"),
)
def update_styles(selected_columns):
    return [{"if": {"column_id": i}, "background_color": "#D2F3FF"} for i in selected_columns]


if __name__ == "__main__":
    app.run_server(debug=True)
