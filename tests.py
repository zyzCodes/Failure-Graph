#Write your tests here
import datetime 
import useful as usf
import db
import environment as env
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
    
    
def parse_data(env, proyect_id, component_type, start, end):
    env=env
    conx=db.SQLConnection(env)
    conx.ExecuteQueryDataFrame(proyect_id, component_type, start, end)
    return conx.GetDF()

env=env.Environment('development')
df=parse_data(env, 'FALLASED40', 'EST', '2022-04-08 13:00:00', '2022-04-08 14:00:00')
     
print(df)
    