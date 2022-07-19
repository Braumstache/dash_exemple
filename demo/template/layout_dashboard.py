from dash import dcc, html
from dash.dependencies import Input, Output
from components.function import liste_carburant

dashboards=html.Div([
    dcc.Dropdown(id="choix_Carburant",
                        options=liste_carburant, 
                        value="Gazole"),
    dcc.Graph(id="france")
])