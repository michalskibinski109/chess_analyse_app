from dash import Dash, html, dcc
import pandas as pd
import ids


def get_time_class(df: pd.DataFrame) -> list:
    labels = [v for v in df['time_class'].unique()]
    return labels


def render(app: Dash, df: pd.DataFrame, id=ids.TIME_CLASS_DROPDOWN) -> html.Div:
    return html.Div(
        children=[
            html.H4('time class'),
            dcc.Dropdown(
                id=id,
                multi=True,
                options=get_time_class(df),
                value='rapid',
                clearable=False,className='dropdown'
            )],
        className='dropdown_container'
    )
