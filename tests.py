#Write your tests here
import datetime 
import useful as usf
import db
import logging, numpy as np, pandas as pd, statistics as stats, db, datetime, time, environment,useful as usf
from datetime import date, datetime as dt



#def queryTest(start_date, end_date, start_hour, start_minute, end_hour, end_minute, env, changed_id):
    
    #component_type=usf.getComponentType(changed_id)
    #proyect_id=usf.getProyectId(changed_id)
    
    #hour = datetime.datetime.now().hour
    #date = datetime.datetime.now()
    #week = (dt.isocalendar(date)[1])
    #day = (dt.today().isoweekday())
    #shift= usf.GetShift(hour)
    
    #dates_to_query=usf.GetDatesToQuery(start_date, end_date, start_hour, start_minute, end_hour, end_minute)
    
    #start = dates_to_query[0]
    #end = dates_to_query[1]
    #start_local=dates_to_query[2]
    #end_local=dates_to_query[3]
    
    #return()
    
    
def parse_data(proyect_id, component_type, start, end):
    envi=environment.Environment('production')
    print(envi.Environment())
    conx=db.SQLConnection(envi)
    conx.ExecuteQueryDataFrame(proyect_id, component_type, start, end)
    return conx.GetDF()

df=parse_data('FALLASED40', 'EST', '2022-04-08 13:00:00', '2022-04-08 14:00:00')

sampledata=df

sampledata['DIF']=sampledata['DIF'].astype(str)

sampledata['DIF']=sampledata['DIF'].str.slice(10,19)

sampledata['DIF']=pd.to_timedelta(sampledata['DIF'])

sampledata.insert(6, 'MINUTES', sampledata['DIF'].dt.total_seconds().div(60).astype(int))

print(sampledata)

    