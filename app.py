from dash import Dash
import dash_bootstrap_components as dbc
from layout import create_layout
import pandas as pd

def get_df() -> pd.DataFrame:
    df =  pd.read_csv('Barabasz60.csv')
    df['date'] = pd.to_datetime(df['date'])
    df.index = df['date']
    return df


app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = 'chess dashboard'
app.layout = create_layout(app, get_df()) 
if __name__ == '__main__':
    app.run_server(debug=True)
