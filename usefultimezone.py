import datetime, time, pytz
Epoch_DATETIME = datetime.datetime(1970, 1, 1)
SECONDS_PER_DAY = 86400

def utc_to_local_datetime(utc_datetime):
    delta = utc_datetime - Epoch_DATETIME
    utc_Epoch = SECONDS_PER_DAY * delta.days + delta.seconds
    time_struct = time.localtime(utc_Epoch)
    dt_args = time_struct[:6] + (delta.microseconds,)
    return (datetime.datetime)(*dt_args)


def local_datetime_to_utc(local_datetime):
    local = pytz.timezone('America/Mexico_City')
    utc = pytz.timezone('UTC')
    local_dt = local.localize(local_datetime, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt


def run_example1():
    origin = datetime.datetime(2020, 2, 20, 12, 0, 0, 730000)
    print('original : ' + str(origin))
    result = utc_to_local_datetime(origin)
    print('to_local : ' + str(result))
    print('to_utc   : ' + str(local_datetime_to_utc(result).strftime('%Y-%m-%d %H:%M:%S.%f')))


def run_example2():
    origin = datetime.datetime(2020, 2, 20, 12, 0, 0, 730000)
    print('original : ' + origin.strftime('%Y-%m-%d %H:%M:%S.%f'))
    result = local_datetime_to_utc(origin)
    print('to_utc   : ' + str(result.strftime('%Y-%m-%d %H:%M:%S.%f')))
    result = result.replace(tzinfo=None)
    print('to_local : ' + str(utc_to_local_datetime(result)))