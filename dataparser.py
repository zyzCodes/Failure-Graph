#EXAMPLE DATA QUERY

# SELECT TOP (100) [SeqNo], [Date], [UTC Time], [FALLA], [ESTADO], [CODIGO], [FECHAMASTIEMPO], [DIF], [TIPO] FROM [EuroDigSysDB].[dbo].[FallasED40]
# where FECHAMASTIEMPO BETWEEN '2022-04-08 13:00:00' and '2022-04-08 14:00:00' and TIPO like 'EST'