from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.express as px

import plotly
import plotly.graph_objs as go
import dash, dash_core_components as dcc, dash_html_components as html, dash_renderer
from dash.dependencies import Input, Output, State
from datetime import date, datetime as dt
from plotly.subplots import make_subplots
import plotly.subplots as sp
import useful as usf

external_stylesheets = [
 'https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {'graphBackground':'#f5f5f5', 
 'background':'#ffffff', 
 'text':'#000000'}


app=dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title='Press Failures - Dashboard'
server=app.server



def optionlist(x):
    """
    Returns option label and value that will be used 
    as the start-date/end-date input for the graph
    """
    optionlista=[]
    for i in range(0,x+1):
        if i<=9:
            option={'label': '0{}'.format(i), 'value': '0{}'.format(i)}
        else:
            option={'label': '{}'.format(i), 'value': '{}'.format(i)}
        optionlista.append(option)
    return optionlista

app.layout=html.Div([  
#START PAGE CONENT--------------------------------------------------------------------------------------------------------
           
    html.Div([  
        html.Div([
            html.Img(src=(app.get_asset_url('logoEuroMexico.jpg'))) 
        ], className='banner', style={'float': 'right'}),
        html.Div([
            html.Button('ED40-ROTOR', id='submit-val-01', n_clicks=1, style={'margin-left':'10px'}),
            html.Button('ED40-ESTATOR', id='submit-val-02', n_clicks=2, style={'margin-left':'10px'}),
        ]),
    ]),
    html.Br(),
    html.Div([
        dcc.DatePickerRange(id='datePicker',
            display_format='YYYY-MM-DD',
            first_day_of_week=1,
            minimum_nights=0,
            clearable=False,
            with_portal=False,
            start_date=(dt.now()),
            min_date_allowed=(dt(2017, 6, 21)))
    ]),
    
    html.Div([
        html.Label('         ', style={'display':'inline-block',  'margin-left':'8px'}),
        dcc.Dropdown(
            id='dropdown1',
            options=optionlist(23),#values from 0-23
            style={'width':'50px', 'display':'inline-block',  'text-align':'center'},
            clearable=False,
            placeholder='Hr',
            value='00'
        ),
        html.Label(' : ', style={'display':'inline-block',  'margin-left':'8px'}),
        dcc.Dropdown(
            id='dropdown2',
            options=optionlist(59),#values from 0-59
            style={'width':'50px', 'display':'inline-block',  'text-align':'center'},
            clearable=False,
            placeholder='Min',
            value='00'
        ),

        html.Label('         ', style={'display':'inline-block',  'margin-left':'8px'}),
        dcc.Dropdown(
            id='dropdown3',
            options=optionlist(23),#values from 0-23
            style={'width':'50px', 'display':'inline-block',  'text-align':'center'},
            clearable=False,
            placeholder='Hr',
            value='00'
        ),

        html.Label(' : ', style={'display':'inline-block',  'margin-left':'8px'}),
        dcc.Dropdown(
            id='dropdown4',
            options=optionlist(59),#values from 0-59
            style={'width':'50px', 'display':'inline-block',  'text-align':'center'},
            clearable=False,
            placeholder='Min',
            value='00'
        ),
    ]),
    
    html.Div([
        html.Hr(style={'margin-bottom':'10px'}),
        dcc.Graph(id='Mygraph'),
        dcc.Interval(
            id='interval-component',
            interval=120000,
            n_intervals=0
        )
    ], style={'margin':'20px'}),
    
    html.Div([
        html.Hr(style={'margin-bottom':'10px'}),
        dcc.Graph(id='Piegraph'),
    ], style={'margin':'20px'}),

    html.Div([
        html.Hr(style={'margin-bottom': '10px'}),
        html.Label('Press Failure - Dashboard v1.0'),
       # html.Label('Updated by Diego Arana'),
        html.Label('@ Eurotranciatura Mexico. July, 2022')
    ], style={'margin':'20px'}),
    
    
    
#END PAGE CONTENT------------------------------------------------------------------------------------------------------------------------------------------
])  


changed_id='submit-val-01.n_clicks'

@app.callback(
    Output('Mygraph', 'figure'),
    Output('Piegraph', 'figure'),
    [Input('submit-val-01', 'n_clicks'),
    Input('submit-val-02', 'n_clicks'),
    Input('interval-component', 'children')],
    [State('datePicker', 'start_date'),
     State('datePicker', 'end_date'),
     State('dropdown1', 'value'),
     State('dropdown2', 'value'),
     State('dropdown3', 'value'),
     State('dropdown4', 'value')]
)
def update_output(b1, b2, interval, start_date, end_date, dropdown1, dropdown2, dropdown3, dropdown4):
    global changed_id
    figure1='test'
    figure2='test'
    if [p['prop_id'] for p in dash.callback_context.triggered][0]!='interval-component.n_intervals':
        changed_id=[p['prop_id'] for p in dash.callback_context.triggered][0]
        
    component_type=usf.getComponentType(changed_id)
    proyect_id=usf.getProyectId(changed_id)
        
        
        
        
    
    return(figure1, figure2)
    
 

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port='1237', debug=False, dev_tools_ui=False, dev_tools_props_check=False)