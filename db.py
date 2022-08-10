import pyodbc, pandas as pd


class SQLConnection:

    def __init__(self, env):
        self.server = env.Server()
        self.database = env.Database()
        self.username = env.Username()
        self.password = env.Password()
        if env.Environment() == 'production':
            self.cnxn = pyodbc.connect(DRIVER='{SQL Server}', SERVER=(self.server),
              DATABASE=(self.database),
              UID=(self.username),
              PWD=(self.password))
        elif env.Environment() == 'development':
            self.cnxn = pyodbc.connect(TRUSTED_CONNECTION='Yes', DRIVER='{SQL Server}', SERVER=(self.server), DATABASE=(self.database))
        self.df = pd.DataFrame()

    def ExecuteQueryDataFrame(self, proyect_id, component_type, startTime, endTime):
        cursor = self.cnxn.cursor()
        db=self.database
        proyect_id=proyect_id
        component_type=component_type
        startTime = startTime
        endTime = endTime
        if startTime is None or endTime is None:
            startTime = "'2022-05-20'"
            endTime = "'2022-05-31'"
        startTime = "'{}'".format(startTime)
        endTime = "'{}'".format(endTime)
        # SELECT TOP (100) [SeqNo], [Date], [UTC Time], [FALLA], [ESTADO], [CODIGO], [FECHAMASTIEMPO], [DIF], [TIPO] FROM [EuroDigSysDB].[dbo].[FallasED40]
        # where FECHAMASTIEMPO BETWEEN '2022-04-08 13:00:00' and '2022-04-08 14:00:00' and TIPO like 'EST'
        query = "SELECT TOP (20) [Date], [UTC Time], [FALLA], [FECHAMASTIEMPO], [DIF], [TIPO], [ESTADO] FROM [{0}].[dbo].[{1}] WHERE FECHAMASTIEMPO BETWEEN {2} and {3} and TIPO like '{4}' and ESTADO like 'FALLA ACTIVA                                                                                                                                                                                                                                                  ' order by DIF desc".format(db, proyect_id, startTime, endTime, component_type)
        print(query)
        self.df = pd.read_sql_query(query, self.cnxn)
        cursor.close()
        return self.df

    def RemoveColumns(self):
        lista = [
         'Date', 'UTC Time', 'FECHAMASTIEMPO', 'TIPO', 'ESTADO']
        for col in self.df.columns:
            if col in lista:
                del self.df[col]

    def StripString(self, column):
        self.df[column]=self.df[column].str.strip()

    def GetDF(self):
        return self.df
 
    def GetDF2(self):
        return self.df