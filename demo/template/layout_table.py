from dash import Dash, dcc, html, Input, Output, State, dash_table
import plotly.express as plt
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
from components.function import dftable1
from app import app



liste_ville=dftable1.ville.unique()
liste_region=dftable1.region.unique()

table=html.Div(children=[
    html.H1('Prix du carburant'),
    
    html.Br(),
    
    dbc.Row([
        dbc.Col([
            dbc.Label('Région(s) :'),
            dcc.Dropdown(id="choix_reg",
                        options=dftable1['region'].unique(), 
                        value=""),
                        #  multi=True,
            html.Br(),
            
            dbc.Label('Département(s) :'),
            dcc.Dropdown(id="choix_dep"),
            html.Br(),
            
            dbc.Label('Ville(s) :'),
            dcc.Dropdown(id="choix_vil")
        ],width=3) ,
           
        dbc.Col([
            dash_table.DataTable(id='table',
                                columns=[{"name": i, "id": i} for i in dftable1.columns], 
                                data=dftable1.to_dict('records'),
                                style_table={'border': 'thin lightgrey solid'},
                                style_header={'backgroundColor':'lightgrey','fontWeight':'bold','textAlign':'center'},
                                style_cell={'textAlign':'left','width':'12%'})
        ],width=8)        
        
    ],justify='center') 
            
])

 



