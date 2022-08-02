import pyodbc, pandas as pd


class SQLConexion:

    def __init__(self, env):
        self.server = env.Server()
        self.database = env.Database()
        self.username = env.Username()
        self.password = env.Password()
        if env.Environment() == 'production':
            self.cnxn = pyodbc.connect(DRIVER='{ODBC Driver 17 for SQL Server}', SERVER=(self.server),
              DATABASE=(self.database),
              UID=(self.username),
              PWD=(self.password))
        else:
            if env.Environment() == 'development':
                self.cnxn = pyodbc.connect(TRUSTED_CONNECTION='Yes', DRIVER='{ODBC Driver 17 for SQL Server}',
                  SERVER=(self.server),
                  DATABASE=(self.database))
        self.df = pd.DataFrame()

    def ExecuteQueryDataFrame(self, tagID, startTime, endTime):
        cursor = self.cnxn.cursor()
        startTime = startTime
        endTime = endTime
        if startTime is None or endTime is None:
            startTime = "'2022-05-20'"
            endTime = "'2022-05-31'"
        startTime = "'{}'".format(startTime)
        endTime = "'{}'".format(endTime)
        query = 'SELECT TOP (40000) * FROM [PPADB].[dbo].[View_Read_FLOATArchive] WHERE TagID = {0} AND RowUpdated > {1} AND RowUpdated < {2} ORDER BY RowUpdated'.format(tagID, startTime, endTime)
        self.df = pd.read_sql_query(query, self.cnxn)
        cursor.close()
        return self.df

    def RemoveColumns(self):
        lista = [
         'TagID', 'Time', 'Msec', 'Status']
        for col in self.df.columns:
            if col in lista:
                del self.df[col]

    def PrintQueryResult(self):
        pass

    def GetDF(self):
        return self.df

    def ExecuteQueryDataFrame2(self, semana, dia, turno, equipmentID):
        cursor = self.cnxn.cursor()
        semana = semana
        dia = dia
        turno = turno
        equipmentID = equipmentID
        if startTime is None or endTime is None:
            startTime = '2022-05-20'
            endTime = '2022-05-31'
        startTime = "'{}'".format(startTime)
        endTime = "'{}'".format(endTime)
        query = ' SELECT [Project],[EquipmentName] FROM [VisualPlant].[dbo].[WCRatesPlan] where Week = {0} and Day = {1} and Shift = {2} and EquipmentId = {3}'.format(semana, dia, turno, equipmentID)
        self.df = pd.read_sql_query(query, self.cnxn)
        cursor.close()
        return self.df

    def RemoveColumns2(self):
        lista = [
         'Project']
        for col in self.df.columns:
            if col in lista:
                del self.df[col]

    def PrintQueryResult2(self):
        pass

    def GetDF2(self):
        return self.df