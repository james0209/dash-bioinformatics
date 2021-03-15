import dash
import dash_bootstrap_components as dbc

# from sqlalchemy import create_engine

# from sqlalchemy.orm import declarative_base
# from sqlalchemy import Column, Integer, String
# from flask_sqlalchemy import SQLAlchemy

# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# ENGINE = create_engine("sqlite:///database.db", echo=True)
# Base = declarative_base()


server = app.server
# server.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# db = SQLAlchemy(server)
