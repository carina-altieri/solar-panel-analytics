import pandas as pd
import numpy as np
from datetime import datetime, timedelta 
from db_connection import get_connection
import criar_banco


criar_banco.criar_bd()

# Gerando histórico de dados dos últimos 90 dias, a cada 15 min

data_recente = datetime.now() 
dias_para_subtrair = timedelta(days=90) 
data_antiga = data_recente - dias_para_subtrair 

datas_e_horarios = pd.date_range(start=data_antiga, end=data_recente, freq='15min') 

df = pd.DataFrame({'DataHora': datas_e_horarios})

df['hora'] = df['DataHora'].dt.floor('s').dt.time
hora = df['hora']

df['data'] = df['DataHora'].dt.date
datas = df['data'] 

l_irradiacao_solar = []
l_temperatura_painel = []
l_temperatura_ambiente = []
l_status_painel = []

amanhecer = 6
anoitecer = 18

for h in hora:
    if h.hour < anoitecer and h.hour >= amanhecer:
        irradiacao = np.random.randint(100, 1000)
    else:
        irradiacao = 0
    l_irradiacao_solar.append(irradiacao)

    if irradiacao > 0:
        l_temperatura_painel.append(np.random.randint(40, 70))
        l_temperatura_ambiente.append(np.random.randint(24, 35))
        l_status_painel.append(np.random.choice(["Operando...", "Falha"], p=[0.9, 0.1]))
    else:
        l_temperatura_painel.append(np.random.randint(20, 30))
        l_temperatura_ambiente.append(np.random.randint(13, 24))
        l_status_painel.append("Em espera...")

df.drop('DataHora', axis=1, inplace=True)

df['irradiacao_solar'] = l_irradiacao_solar
df['temp_painel'] = l_temperatura_painel
df['temp_ambiente'] = l_temperatura_ambiente
df['status_painel'] = l_status_painel

# exportando os dados para .csv

df.to_csv('dados_3_meses', index=False, sep=";")

#  inserindo dados no MySQL

cnx = get_connection(database='upx')
cursor = cnx.cursor()

for i, df_coluna in df.iterrows():
    cursor.execute(
        ''' 
        INSERT INTO monitoramento_solar(
        data,
        hora,
        irradiacao_solar,
        temp_painel,
        temp_ambiente,
        status_painel
    ) 
        values (%s,%s,%s,%s,%s,%s)  
        ''',
        (
            df_coluna['data'],
            df_coluna['hora'],
            df_coluna['irradiacao_solar'],
            df_coluna['temp_painel'],
            df_coluna['temp_ambiente'],
            df_coluna['status_painel']
        )
    ) 

cnx.commit()

cursor.close()
cnx.close()
