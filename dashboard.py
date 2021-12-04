import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app_path = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(app_path, os.path.join("data", "smarthome.csv")))
df2 = pd.read_csv(os.path.join(app_path, os.path.join("data", "distributions.csv")))

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Enegry Consumption'),
                ],
            ),
        ],
    )


def build_graph():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df['Batch'][:50],
                    'y': df['Techniques'][:50],
                    'name': 'Techniques',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Workplace'][:50],
                    'name': 'Workplace',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Garage'][:50],
                    'name': 'Garage',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Kitchen'][:50],
                    'name': 'Kitchen',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Hall'][:50],
                    'name': 'Hall',
                    'marker': {'size': 12}
                },
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                }
            }
        }
    )


def build_banner2():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.H5('Random samples from different distributions'),
                ],
            ),
        ],
    )


def build_graph2():
    return dcc.Graph(
        figure={
            'data': [
                {
                    'x': df2['Sample'][:50],
                    'y': df2['N(0,1)'][:50],
                    'name': 'N(0,1)',
                    'marker': {'size': 12}
                },
                {
                    'x': df2['Sample'][:50],
                    'y': df2['N(5,1)'][:50],
                    'name': 'N(5,1)',
                    'marker': {'size': 12}
                },
                {
                    'x': df2['Sample'][:50],
                    'y': df2['N(-5,1)'][:50],
                    'name': 'N(-5,1)',
                    'marker': {'size': 12}
                },
                {
                    'x': df2['Sample'][:50],
                    'y': df2['N(0,10)'][:50],
                    'name': 'N(0,10)',
                    'marker': {'size': 12}
                }
            ],
            'layout': {
                'plot_bgcolor': "#6495ed",
                'paper_bgcolor': "#ff4f00",
                'font': {
                    'color': "#000000"
                }
            }
        }
    )


app.layout = html.Div(
	children=[html.Div(
    className='big-app-container',
    children=[
        build_banner(),
        html.Div(
            className='app-container',
            children=[
                build_graph(),
            ]
        )
    ]), html.Div(
		className='big-app-container',
		children=[
			build_banner2(),
			html.Div(
				className='app-container',
				children=[
					build_graph2(),
				]
			)
		]
	)])
