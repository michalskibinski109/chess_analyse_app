from dash import Dash, html, dcc
import plotly.express as px
import ids
import pandas as pd
from dash.dependencies import Input, Output


def get_win_ratio_per_opening(df: pd.DataFrame) -> pd.DataFrame:
    dff = df.copy()
    dff['opening'] =  [str(o).split(':')[0] for o in dff['opening']]
    dff2 = pd.DataFrame(dff.groupby('opening')['player_result'].count())
    dff2['win_ratio'] = round(dff.groupby('opening')['player_result'].sum()/dff2['player_result'],2)
    return dff2


def render(app: Dash, df: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.OPENING_CHART, 'children'),
        [Input(ids.YEAR_DROPDOWN_2, 'value'), Input(ids.COLOR_DROPDOWN, 'value')])
    def update_bar_chart(years: list, color) -> html.Div:
        dff = df.query('date.dt.year in @years')
        dff = dff.query('player_color in @color')
        fig = px.bar(get_win_ratio_per_opening(dff),
                     barmode='group', text_auto=True, orientation='h',height=4000, width=1000)
        return html.Div(dcc.Graph(figure=fig), id=ids.OPENING_CHART, className='openings-chart')
    return html.Div(id=ids.OPENING_CHART, className='openings-chart')
