from dash import Dash, html, dcc
import pandas as pd
import ids


def get_years(df: pd.DataFrame) -> list:
    return [int(v) for v in df['date'].dt.year.unique()]


def render(app: Dash, df: pd.DataFrame, id=ids.YEAR_DROPDOWN) -> html.Div:
    return html.Div(
        children=[
            html.H4('year'),
            dcc.Dropdown(
                id=id,
                multi=True,
                clearable=False,
                options=get_years(df),
                value=[get_years(df)[0]], 
                className='dropdown'
            )],
        className='dropdown_container')
