import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Load preprocessed data
vehicles_df = pd.read_csv('combined_vehicles.csv')

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([
    dbc.Row([
        html.H1("PyData UniConnect 2025 WUSL - Assessment", className="text-center my-4"),
        html.H2("Group 09 - CASE 03: The Wheels in Motion", className="text-center mb-4"),
        html.H4("Illinois Public Passenger Vehicle Analytics", className="text-center mb-4"),
    ]),
    dbc.Row([
        dbc.Col([
            html.Label("Vehicle Type", className="mb-2"),
            dcc.Dropdown(
                id='vehicle-type-filter',
                options=[{'label': vt, 'value': vt} for vt in sorted(vehicles_df['Vehicle Type'].dropna().unique())],
                value=sorted(vehicles_df['Vehicle Type'].dropna().unique()),
                multi=True,
                placeholder="Select Vehicle Type",
                className="mb-3"
            )
        ], md=4),
        dbc.Col([
            html.Label("Fuel Type", className="mb-2"),
            dcc.Dropdown(
                id='fuel-filter',
                options=[{'label': f, 'value': f} for f in sorted(vehicles_df['Vehicle Fuel Source'].dropna().unique())],
                value=sorted(vehicles_df['Vehicle Fuel Source'].dropna().unique()),
                multi=True,
                placeholder="Select Fuel Types",
                className="mb-3"
            )
        ], md=4),
        dbc.Col([
            html.Label("Vehicle Model Year", className="mb-2"),
            dcc.RangeSlider(
                id='year-slider',
                min=1980,
                max=2025,
                step=1,
                value=[1980, 2025],
                marks={str(year): str(year) for year in range(int(vehicles_df['Vehicle Model Year'].min()), int(vehicles_df['Vehicle Model Year'].max())+1, 5)},
                tooltip={"placement": "bottom"},
                className="p-3"
            )
        ], md=4)
    ], className="mb-4"),
    dbc.Row([
        dbc.Col(dcc.Graph(id='type-fuel-composition'), md=6),
        dbc.Col(dcc.Graph(id='status-fuel-distribution'), md=6)
    ], className="mb-4"),
    dbc.Row([
        dbc.Col(dcc.Graph(id='top-companies'), md=4),
        dbc.Col(dcc.Graph(id='wheelchair-access'), md=4),
        dbc.Col(dcc.Graph(id='age-distribution'), md=4)
    ], className="mb-4"),
    dbc.Row([
        dbc.Col(dcc.Graph(id='vehicle-make-bar'), md=6),
        dbc.Col(dcc.Graph(id='vehicle-model-bar'), md=6)
    ], className="mb-4"),
], fluid=True)

@callback(
    [
        Output('type-fuel-composition', 'figure'),
        Output('status-fuel-distribution', 'figure'),
        Output('top-companies', 'figure'),
        Output('wheelchair-access', 'figure'),
        Output('age-distribution', 'figure'),
        Output('vehicle-make-bar', 'figure'),
        Output('vehicle-model-bar', 'figure')
    ],
    [
        Input('vehicle-type-filter', 'value'),
        Input('fuel-filter', 'value'),
        Input('year-slider', 'value')
    ]
)
def update_charts(selected_types, selected_fuels, year_range):
    filtered_df = vehicles_df[
        vehicles_df['Vehicle Type'].isin(selected_types) &
        vehicles_df['Vehicle Fuel Source'].isin(selected_fuels) &
        vehicles_df['Vehicle Model Year'].between(year_range[0], year_range[1])
    ]
    # Type-Fuel Composition (Treemap)
    treemap = px.treemap(
        filtered_df,
        path=['Vehicle Type', 'Vehicle Fuel Source'],
        title='Fleet Composition by Type & Fuel'
    )
    # Status-Fuel Distribution (Sunburst)
    sunburst = px.sunburst(
        filtered_df,
        path=['Status', 'Vehicle Fuel Source'],
        title='Operational Status & Fuel Distribution'
    )
    # Top Companies (Horizontal Bar)
    top_companies = px.bar(
        filtered_df['Company Name'].value_counts().head(10).reset_index(),
        x='count', y='Company Name',
        title='Top 10 Fleet Operators',
        orientation='h',
        labels={'count': 'Number of Vehicles', 'Company Name': 'Company'}
    )
    # Wheelchair Access (Pie)
    wheelchair_pie = px.pie(
        filtered_df,
        names='Wheelchair Accessible',
        title='Wheelchair Accessibility',
        hole=0.4
    )
    # Age Distribution (Histogram)
    age_hist = px.histogram(
        filtered_df,
        x='Vehicle Model Year',
        title='Vehicle Age Distribution',
        nbins=20
    )
    # Vehicle Make (Bar Chart)
    make_counts = filtered_df['Vehicle Make'].value_counts().head(15).reset_index()
    make_counts.columns = ['Vehicle Make', 'Count']
    vehicle_make_bar = px.bar(
        make_counts,
        x='Vehicle Make',
        y='Count',
        title='Top 15 Vehicle Makes',
        labels={'Count': 'Number of Vehicles', 'Vehicle Make': 'Make'},
        color='Count',
        color_continuous_scale='Blues'
    )
    # Vehicle Model (Bar Chart)
    model_counts = filtered_df['Vehicle Model'].value_counts().head(15).reset_index()
    model_counts.columns = ['Vehicle Model', 'Count']
    vehicle_model_bar = px.bar(
        model_counts,
        x='Vehicle Model',
        y='Count',
        title='Top 15 Vehicle Models',
        labels={'Count': 'Number of Vehicles', 'Vehicle Model': 'Model'},
        color='Count',
        color_continuous_scale='Greens'
    )
    return treemap, sunburst, top_companies, wheelchair_pie, age_hist, vehicle_make_bar, vehicle_model_bar

if __name__ == '__main__':
    app.run(debug=True)
