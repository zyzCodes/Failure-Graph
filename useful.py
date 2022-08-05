<<<<<<< HEAD
IDs={
    '.':'data/sampledata.csv',
    'submit-val-01.n_clicks':'data/sampledata.csv',
    'submit-val-02.n_clicks':'data/sampledata2.csv',
}




=======
import json
import datetime, time as utz
from datetime import datetime as dt



def getComponentType(changed_id):
    with open("data/components.json", "r") as read_file:
        components = json.load(read_file)
    component_type=components[changed_id]
    return component_type

def getFile(changed_id):
    with open("data/filenames.json", "r") as read_file:
        files = json.load(read_file)  
    file=files[changed_id]
    return file
>>>>>>> 28dda889068749bd6689b3b45df95bcc680f3984

def getProyectId(changed_id):
    with open("data/proyectsid.json", "r") as read_file:
        proyectsids = json.load(read_file)
    project_id=proyectsids[changed_id]
    return project_id
    



def days_between(d1, d2):
    return abs((d2 - d1).days)

def GetDatesToQuery(start_date, end_date, dropdown1, dropdown2, dropdown3, dropdown4):
    if end_date is None:
        now_mex_end = datetime.datetime.now()
        now_mex_start = now_mex_end - datetime.timedelta(hours=8)
        start_local_s = format(now_mex_start, '%Y-%m-%d %H:%M')
        end_local_s = format(now_mex_end, '%Y-%m-%d %H:%M')
        start = utz.local_datetime_to_utc(now_mex_start)
        end = utz.local_datetime_to_utc(now_mex_end)
        start = start.strftime('%Y-%m-%d %H:%M')
        end = end.strftime('%Y-%m-%d %H:%M')
    else:
        start_local_s = str(start_date)[0:10]
        start_local_s = start_local_s + ' ' + dropdown1 + ':' + dropdown2
        end_local_s = end_date + ' ' + dropdown3 + ':' + dropdown4
        start_local = dt.strptime(start_local_s, '%Y-%m-%d %H:%M')
        end_local = dt.strptime(end_local_s, '%Y-%m-%d %H:%M')
        if days_between(start_local, end_local) > 32:
            return 'The date interval is it very large. Please insert a interval less that a month.'
        start = utz.local_datetime_to_utc(start_local)
        end = utz.local_datetime_to_utc(end_local)
        start = start.strftime('%Y-%m-%d %H:%M')
        end = end.strftime('%Y-%m-%d %H:%M')
    return (start, end, start_local_s, end_local_s)

    
    
