from flask import Flask, render_template
import pandas as pd
import plotly
import plotly.graph_objs as go
import csv
import time

app = Flask(__name__)

WINDOW_SIZE = 100

# Get data
def get_data_from_csv(filename):
    data = pd.read_csv(filename)
    return data

# Generate graph
def generate_graph(data):

    recent_data = data[-WINDOW_SIZE:]

    x_data = recent_data['time']

    y_data_rpm = recent_data['rpm']
    y_data_water_temp = recent_data['water_temp']
    y_data_oil_temp = recent_data['oil_temp']
    y_data_gear_voltage = recent_data['gear_volt']

    trace_rpm = go.Scatter(
        x=x_data,
        y=y_data_rpm,
        mode='lines+markers',
        name='RPM moteur',
        yaxis='y1'
    )

    trace_water_temp = go.Scatter(
        x=x_data,
        y=y_data_water_temp,
        mode='lines+markers',
        name='Temp eau',
        yaxis='y2'
    )

    trace_oil_temp = go.Scatter(
        x=x_data,
        y=y_data_oil_temp,
        mode='lines+markers',
        name='Temp huile',
        yaxis='y2'
    )

    trace_gear_voltage = go.Scatter(
        x=x_data,
        y=y_data_gear_voltage,
        mode='lines+markers',
        name='Voltage boite',
        yaxis='y3'
    )

    layout = go.Layout(
        title='Données de la voiture',
        xaxis=dict(title='Temps'),
        yaxis=dict(title='RPM moteur', range=[1000, 6000], domain=[0, 0.3]),
        yaxis2=dict(title='Températures', range=[20, 150], domain=[0.35, 0.65]),
        yaxis3=dict(title='Voltage boite', range=[10, 15], domain=[0.7, 1])
    )

    graph = go.Figure(data=[trace_rpm, trace_water_temp, trace_oil_temp, trace_gear_voltage], layout=layout)
    graphJSON = plotly.io.to_json(graph)
    return graphJSON

# Main route
@app.route('/')
def index():
    return render_template('index.html')

# Update page
@app.route('/update_graph')
def update_graph():
    data = get_data_from_csv('data/data.csv')
    graphJSON = generate_graph(data)
    return graphJSON

if __name__ == '__main__':
    app.run(debug=True)
