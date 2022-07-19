from dash import dcc, html
from dash.dependencies import Input, Output
import components.callbacks
from template.header import navbar
from template.layout_dashboard import dashboards
from template.layout_table import table
from app import app,server

#layout rendu par l'application
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    navbar,
    html.Div(id='page-content')
])
 
#callback pour mettre à jour les pages
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname=='/table' or pathname=='/':
        return table
    elif pathname=='/dashboard':
        return dashboards
 
 
if __name__ == '__main__':
    app.run_server(debug=True)