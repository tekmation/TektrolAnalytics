import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc

# Define the file path
file_path = './data/ScadaFlow_01-07-2024_To_16-08-2024-cleaned.xlsx'

# Define the specific columns for each sheet
columns_volumeP = ['ReportDate', 'Volumetric Flow G Previous Hour Total (MSCF)', 'Volumetric Flow L Previous Hour Total (bbl)', 'Volumetric Flow G App Previous Hour Total (MSCF)']
columns_volume = ['ReportDate', 'Volumetric Flow G Previous Rate (MSCF) * 24', 'Volumetric Flow L Previous Rate (bbl/hr) * 24', 'Volumetric Flow G App Previous Rate (MSCF) * 24']
columns_line = ['ReportDate', 'Line Pressure (psi)', 'Line Temperature (F)']
columns_h20 = ['ReportDate', 'D Pppl (InH2O)', 'D Pr (InH2O)', 'D Pt (InH2O)']

# Load the specific sheets with the defined columns
volumeP_df = pd.read_excel(file_path, sheet_name='Volume', usecols=columns_volume)
volume_df = pd.read_excel(file_path, sheet_name='Volume', usecols=columns_volume)
line_df = pd.read_excel(file_path, sheet_name='Line', usecols=columns_line)
h20_df = pd.read_excel(file_path, sheet_name='H20', usecols=columns_h20)

# Convert ReportDate to datetime
volumeP_df['ReportDate'] = pd.to_datetime(volume_df['ReportDate'])
volume_df['ReportDate'] = pd.to_datetime(volume_df['ReportDate'])
line_df['ReportDate'] = pd.to_datetime(line_df['ReportDate'])
h20_df['ReportDate'] = pd.to_datetime(h20_df['ReportDate'])

# Create Dash app
app = Dash(__name__)

# Create plots
volumeP_fig = go.Figure()
volumeP_fig.add_trace(go.Scatter(x=volume_df['ReportDate'], y=volume_df['Volumetric Flow G Previous Hour Total (MSCF)'], mode='lines', name='Volumetric Flow G (MSCF)'))
volumeP_fig.add_trace(go.Scatter(x=volume_df['ReportDate'], y=volume_df['Volumetric Flow L Previous Hour Total (bbl/hr)'], mode='lines', name='Volumetric Flow L (bbl/hr)'))
volumeP_fig.add_trace(go.Scatter(x=volume_df['ReportDate'], y=volume_df['Volumetric Flow G App Previous Hour Total (MSCF)'], mode='lines', name='Volumetric Flow G App (MSCF)'))
volumeP_fig.update_layout(title='VolumeP Comparison', xaxis_title='Report Date', yaxis_title='Flow Rate')

volume_fig = go.Figure()
volume_fig.add_trace(go.Scatter(x=volume_df['ReportDate'], y=volume_df['Volumetric Flow G Previous Rate (MSCF) * 24'], mode='lines', name='Volumetric Flow G (MSCF) * 24'))
volume_fig.add_trace(go.Scatter(x=volume_df['ReportDate'], y=volume_df['Volumetric Flow L Previous Rate (bbl/hr) * 24'], mode='lines', name='Volumetric Flow L (bbl/hr) * 24'))
volume_fig.add_trace(go.Scatter(x=volume_df['ReportDate'], y=volume_df['Volumetric Flow G App Previous Rate (MSCF) * 24'], mode='lines', name='Volumetric Flow G App (MSCF) * 24'))
volume_fig.update_layout(title='Volume Comparison', xaxis_title='Report Date', yaxis_title='Flow Rate')

line_fig = go.Figure()
line_fig.add_trace(go.Scatter(x=line_df['ReportDate'], y=line_df['Line Pressure (psi)'], mode='lines', name='Line Pressure (psi)'))
line_fig.add_trace(go.Scatter(x=line_df['ReportDate'], y=line_df['Line Temperature (F)'], mode='lines', name='Line Temperature (F)'))
line_fig.update_layout(title='Line Comparison', xaxis_title='Report Date', yaxis_title='Value')

h20_fig = go.Figure()
h20_fig.add_trace(go.Scatter(x=h20_df['ReportDate'], y=h20_df['D Pppl (InH2O)'], mode='lines', name='D Pppl (InH2O)'))
h20_fig.add_trace(go.Scatter(x=h20_df['ReportDate'], y=h20_df['D Pr (InH2O)'], mode='lines', name='D Pr (InH2O)'))
h20_fig.add_trace(go.Scatter(x=h20_df['ReportDate'], y=h20_df['D Pt (InH2O)'], mode='lines', name='D Pt (InH2O)'))
h20_fig.update_layout(title='H20 Comparison', xaxis_title='Report Date', yaxis_title='InH2O')

# Define layout
app.layout = html.Div([
	html.H1('SCADA Data Visualization Dashboard'),
	html.Div([
		html.Div(dcc.Graph(figure=volume_fig), className='card'),
		html.Div(dcc.Graph(figure=line_fig), className='card'),
		html.Div(dcc.Graph(figure=h20_fig), className='card')
	], className='grid-container')
])

# Run app
if __name__ == '__main__':
	app.run_server(debug=True, port=8080)