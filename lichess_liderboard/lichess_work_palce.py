import my_hypotheses as hyp
import LichessAnalys as li
from dash import Dash, html, dcc, dash_table, Input, Output, callback
import pandas as pd
import plotly.express as px
import json
from dash.dash_table import FormatTemplate, DataTable
from dash.dash_table.Format import Group, Scheme, Symbol, Format
from dash.exceptions import PreventUpdate

lichessAnalys = li.LichessAnalys()
hypotheses = hyp.ProgressivePlayerCanBeACheater()

classical_data = pd.read_csv('D:\dev\DataScience\lichess_liderboard\df_classical.csv', sep=';')




df = classical_data

app = Dash(__name__, suppress_callback_exceptions=True)


app.layout = html.Div(
    [
        html.H4("Simple interactive table"),
        html.A("Link to external site", href='link', target="_blank"),
        html.P(id="table_out"),
        dash_table.DataTable(
            id="table",
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
            style_cell=dict(textAlign="left"),
            style_header=dict(backgroundColor="paleturquoise"),
            style_data=dict(backgroundColor="lavender"),
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)

# from dash import Dash, html
# from dash.dependencies import Input, Output
# from dash.exceptions import PreventUpdate

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     html.Button('Click here to see the content', id='show-secret'),
#     html.Div(id='body-div')
# ])

# @app.callback(
#     Output(component_id='table', component_property='children'),
#     Input(component_id='show-secret', component_property='n_clicks')
# )
# def update_output(n_clicks):
#     if n_clicks is None:
#         raise PreventUpdate
#     else:
#         return "Elephants are the only animal that can't jump"

# if __name__ == '__main__':
#     app.run_server(debug=True)

