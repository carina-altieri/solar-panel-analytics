import pandas as pd
import numpy as np
from datetime import datetime, timedelta 
from db import get_connection

# Gerando histórico de dados dos últimos 30 dias, a cada 15 min

data_recente = datetime.now() 
dias_para_subtrair = timedelta(days=29) 
data_antiga = data_recente - dias_para_subtrair 

datas_e_horarios = pd.date_range(start=data_antiga, end=data_recente, freq='15min') 

df = pd.DataFrame({'DataHora': datas_e_horarios})


df['Hora'] = df['DataHora'].dt.time
hora = df['Hora']

df['Data'] = df['DataHora'].dt.date
datas = df['Data'] 

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

df['IrradiacaoSolar'] = l_irradiacao_solar
df['TempPainel'] = l_temperatura_painel
df['TempAmbiente'] = l_temperatura_ambiente
df['StatusPainel'] = l_status_painel


# inserindo dados no MySQL

cnx = get_connection()
cur = cnx.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS monitoramento_solar (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    data DATE NOT NULL, 
    hora TIME NOT NULL,
    irradiacao_solar FLOAT, 
    temp_painel FLOAT, 
    temp_ambiente FLOAT, 
    status_painel VARCHAR(50)
)
"""
cur.execute(create_table)

for i, df_coluna in df.iterrows():
    cur.execute(
        ''' 
        INSERT INTO upx.monitoramento_solar(
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
            df_coluna['Data'],
            df_coluna['Hora'],
            df_coluna['IrradiacaoSolar'],
            df_coluna['TempPainel'],
            df_coluna['TempAmbiente'],
            df_coluna['StatusPainel']
        )
    ) 

cnx.commit()

cur.close()
cnx.close()