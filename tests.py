import json
from optparse import Values
from turtle import width
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from pandas import Series
from datetime import datetime
import plotly.express as px

import plotly
import plotly.graph_objs as go
from collections import deque
from dash.dependencies import Input, Output, State
from datetime import date, datetime as dt

external_stylesheets = [
 'https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {'graphBackground':'#f5f5f5', 
 'background':'#ffffff', 
 'text':'#000000'}



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
    print(optionlista)
    return optionlista


#optionlist(52)



"TEST DE OBTENCION DE FRECUENCIA"


sampledata = pd.read_csv(r'sampledata.csv')

raw=pd.DataFrame({'FuncGroup':sampledata['FALLA']})

s=raw['FuncGroup'].value_counts()


new = pd.DataFrame({'FuncGroup':s.index, 'Count':s.values})

piefig=px.pie(new, values='Count', names='FuncGroup', title='Frecuencia de los Fallos.')
piefig.show()



figure1='test'
figure2='test2'
figure1_traces = []
figure2_traces = []
this_figure="test3"
for trace in range(len(figure1["data"])):
    figure1_traces.append(figure1["data"][trace])
for trace in range(len(figure2["data"])):
    figure2_traces.append(figure2["data"][trace])

#Create a 1x2 subplot
#this_figure = sp.make_subplots(rows=1, cols=2, specs=[[{"type":"bar"}, {"type":"pie"}]]) 

# Get the Express fig broken down as traces and add the traces to the proper plot within in the subplot
for traces in figure1_traces:
    this_figure.append_trace(traces, row=1, col=1)
for traces in figure2_traces:
    this_figure.append_trace(traces, row=1, col=2)