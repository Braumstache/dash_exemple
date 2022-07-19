
from dash import Dash, dcc, html, Input, Output, State, dash_table
from app import app,server
from components.function import dfmap,dftable1
import pygal
import json
import plotly.express as px
@app.callback(
    Output('france','figure'),
    Input('choix_Carburant','value'))
def carte_france(choix_carbu):
    df1=dfmap[dfmap.carburant==choix_carbu]
    
    with open('./demo/data/a-dep2021.json') as fp:
        
        geo = json.load(fp)

    fig = px.choropleth(df1,
                            locations='code_departement',
                            geojson=geo,
                            featureidkey='properties.dep',
                            hover_name='departement',
                            color_continuous_scale="Oryel",
                            color="prix",
                            projection='gnomonic',
                            center={'lon':48.864716,'lat':2.349014} 
                            )
    fig.update_geos(showcountries=False, showcoastlines=False, showland=False, fitbounds="locations")
    fig.update_layout(margin={'l': 10, 'r': 10, 't': 10, 'b': 10})
    fig.update_layout(plot_bgcolor='rgb(0,0,0)')
    
    return fig
    
@app.callback(
    Output('choix_dep', 'options'),
    Input('choix_reg', 'value'))
def set_dep_options(reg):
    dftable2=dftable1[dftable1.region==reg]
    liste=dftable2['departement'].unique()
    return list(liste)

@app.callback(
    Output('choix_vil', 'options'),
    State('choix_reg', 'value'),
    Input('choix_dep', 'value'))
def set_ville_options(reg, dep):
    dftable3=dftable1[(dftable1.region==reg) &(dftable1.departement==dep)]
    liste2=dftable3["ville"].unique()
    return list(liste2)
@app.callback(
    Output('table', "data"),
    Input('choix_vil','value'))
def tableinput(ville):
    dftable=dftable1.copy()
    
    df=dftable[dftable.ville==ville]
    return df.to_dict('records')
    
        
        
    
    