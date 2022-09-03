import pandas as pd
from dash import Dash, html
import dash_bootstrap_components as dbc
import ids
from dropdowns import year_dropdown, time_class_dropdown
from charts import bar_chart


def render(app: Dash, df: pd.DataFrame) -> dbc.Card:
    return dbc.Card(
        dbc.CardBody([
            html.Section(
                children=[
                    html.H1('win ratio per hour'),
                    html.Hr(),
                    html.Div(
                        className='dropdowns',
                        children=[
                            year_dropdown.render(app, df, ids.YEAR_DROPDOWN),
                            time_class_dropdown.render(app, df)
                        ]
                    ),
                    bar_chart.render(app, df)
                ])
        ]))
