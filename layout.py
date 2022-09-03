import ids
from dash import Dash, html
from cards import card1, card2
import dash_bootstrap_components as dbc
import pandas as pd


def create_layout(app: Dash, df: pd.DataFrame) -> html.Div:
    tab1 = card1.render(app, df)
    tab2 = card2.render(app, df)
    return dbc.Tabs(
        [
            dbc.Tab(tab1, label="Tab 1"),
            dbc.Tab(tab2, label="Tab 2")
        ]
    )
