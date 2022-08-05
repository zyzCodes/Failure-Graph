from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.express as px
import environment
import plotly
from plotly.offline import iplot
import plotly.graph_objs as go
import dash, dash_core_components as dcc, dash_html_components as html, dash_renderer
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots
import plotly.subplots as sp
import useful as usf
import datetime
import db
from datetime import date, datetime as dt

external_stylesheets = [
 'https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {'graphBackground':'#f5f5f5', 
 'background':'#ffffff', 
 'text':'#000000'}

app=dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title='Project Failure - Dashboard'
server=app.server

changed_id='submit-val-01.n_clicks'

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
        html.Label('Project Failure - Dashboard v1.0'),
       # html.Label('Updated by Diego Arana'),
        html.Label('@ Eurotranciatura Mexico. July, 2022')
    ], style={'margin':'20px'}),
#END PAGE CONTENT------------------------------------------------------------------------------------------------------------------------------------------
])  
@app.callback(
    [Output('Mygraph', 'figure'),
    Output('Piegraph', 'figure')],
    #Output('piegraph-tpt', 'children'),
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
    
    if [p['prop_id'] for p in dash.callback_context.triggered][0]!='interval-component.n_intervals':
        changed_id=[p['prop_id'] for p in dash.callback_context.triggered][0]
        
    component_type=usf.getComponentType(changed_id)
    proyect_id=usf.getProyectId(changed_id)
    
    selected_dates=usf.GetDatesToQuery(start_date, end_date, dropdown1, dropdown2, dropdown3, dropdown4)
    start_time=selected_dates[0]
    end_time=selected_dates[1]
    start_local_time=selected_dates[2]
    end_local_time=selected_dates[3]
    now=datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M')
    then=datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M')
    total_time=now-then
    #'2022-04-08 13:00:00', '2022-04-08 19:30:00'
    df = parse_data(proyect_id, component_type, start_time, end_time)  #makes query

    sampledata = df
    sampledata['DIF']=sampledata['DIF'].astype(str)
    sampledata['DIF']=sampledata['DIF'].str.slice(10,19)    
    sampledata['DIF']=pd.to_timedelta(sampledata['DIF'])
    sampledata.insert(1, 'MINUTES', sampledata['DIF'].dt.total_seconds().div(60).astype(int))
    del sampledata['DIF']
    df=sampledata
    data=['Tiempo Total', total_time]
    dftt=pd.DataFrame([data], columns=['FALLA', 'DIF'])
    dftt.insert(1, 'MINUTES', dftt['DIF'].dt.total_seconds().div(60).astype(int))
    total_failure_time=0
    for i in sampledata['MINUTES']:
        total_failure_time+=i
    total_productive_time=0
    for i in dftt['MINUTES']:
        total_productive_time+=i
    total_productive_time-=total_failure_time
    print('####################################################################################')
    data=['Total Productive Time', total_productive_time]
    dftpt=pd.DataFrame([data], columns=['FALLA', 'MINUTES'])
    df=pd.concat([dftpt, df], ignore_index=True)
    print(df)
    
    
    
    #BARCHART-----------------------------------------------------------------------------------------------------------
    figure1 = px.bar(sampledata, x='MINUTES', y='FALLA', color='FALLA', orientation='h')
    figure1.update_layout(
        title=str(proyect_id)+' '+str(component_type)+' from {0} to {1}.'.format(start_local_time, end_local_time),
        xaxis = dict(
            title='TIME (minutes)', 
            rangeslider = dict(
                visible=True, 
                thickness=0.05
            )
        ),
        yaxis = dict(
            title='FALLA'
            
        ), 
        paper_bgcolor='#FFFFFF', 
        showlegend=False,
    )
    figure1.update_traces(
        width=0.5
    )
    #PIE GRAPH---------------------------------------------------------------------------------------------------------------
    raw=pd.DataFrame({'FALLA':sampledata['FALLA']})
    s=raw['FALLA'].value_counts()
    new = pd.DataFrame({'FALLA':s.index, 'FRECUENCIA':s.values})
    failure_list=[]
    frecuencylist=[]
    minutelist=[]
    failure_list2=[]
    for i in new['FRECUENCIA']:
        frecuencylist.append(i)
    for i in new['FALLA']:
        failure_list.append(i)
    for i in df['MINUTES']:
        minutelist.append(i)
    for i in df['FALLA']:
        failure_list2.append(i)
        
    print(minutelist)
    print(failure_list2)
   # figure2=px.pie(new, values='FRECUENCIA', names='FALLA', title='Faillure Frequency.')  
    
    figure2 = make_subplots(rows=1, cols=2, subplot_titles=['Failure Frecuency', 'Total Time = {0}'.format(total_time)], specs=[[{'type':'domain'}, {'type':'domain'}]])
    figure2.add_trace(go.Pie(labels=failure_list, values=frecuencylist, name="Failure Frecuency"),
              1, 1)
    
    
    
    
    
    figure2.add_trace(go.Pie(labels=failure_list2, values=minutelist, name="Total Time"),
              1, 2)
    return(figure1, figure2)



 
def parse_data(proyect_id, component_type, start, end):
    env=environment.Environment('production')
    conx=db.SQLConnection(env)
    conx.ExecuteQueryDataFrame(proyect_id, component_type, start, end)
    conx.RemoveColumns()
    
    conx.StripString('FALLA')
    return conx.GetDF()

def ReturnDefaultOrError(error):
    fig = go.Figure()
    iplot(fig)
    return (fig, error)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port='1237', debug=False, dev_tools_ui=False, dev_tools_props_check=False)
    
    
