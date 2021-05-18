import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app
from apps import home, interactivity, onlineBlast, sequenceViewer, DataTable, alignment, contact


# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/"),
        dbc.DropdownMenuItem("View all Proteins", href="/apps/DataTable"),
        dbc.DropdownMenuItem("Protein Visualisation", href="/apps/sequenceViewer"),
        dbc.DropdownMenuItem("Alignment Viewer", href="/apps/alignment"),
        dbc.DropdownMenuItem("Interactivty Viewer", href="/apps/interactivity"),
        dbc.DropdownMenuItem("Contact", href="/apps/contact"),
    ],
    nav=True,
    in_navbar=True,
    label="Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("Protein Bioinformatics App", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown],
                    className="ml-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)


app.layout = html.Div([dcc.Location(id="url", refresh=False), navbar, html.Div(id="page-content")])


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/apps/interactivity":
        return interactivity.layout
    elif pathname == "/apps/onlineBlast":
        return onlineBlast.layout
    elif pathname == "/apps/alignment":
        return alignment.layout
    elif pathname == "/apps/contact":
        return contact.layout
    elif pathname == "/apps/sequenceViewer":
        return sequenceViewer.layout
    elif pathname == "/apps/DataTable":
        return DataTable.layout
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)
