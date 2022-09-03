from dash import Dash, html, dcc
import pandas as pd
import ids


def render(app: Dash, df: pd.DataFrame, id=ids.COLOR_DROPDOWN) -> html.Div:
    return html.Div(
        children=[
            html.H4('time class'),
            dcc.Dropdown(
                id=id,
                multi=True,
                options=[{'label': 'black', 'value': 0},
                         {'label': 'white', 'value': 1}],
                value=[1],
                clearable=False, className='dropdown'
            )],
        className='dropdown_container'
    )
