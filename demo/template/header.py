import dash_bootstrap_components as dbc
from dash import html
from dash_bootstrap_components._components.Container import Container

logo='assets/light_plotly_dash_logo.png'
navbar = dbc.Navbar(
    html.Div(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=logo, height="50px")),
                        dbc.Col(dbc.NavLink("Table", href="/table")),
                        dbc.Col(dbc.NavLink("Dashboard", href="/dashboard"))
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
        ]
    ),
    color="dark",
    dark=True,
)

