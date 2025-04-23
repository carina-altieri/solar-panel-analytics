import pandas as pd
import numpy as np
from datetime import datetime, timedelta 

# Gerando histórico de dados dos últimos 30 dias, a cada 15 min

data_recente = datetime.now() 
dias_para_subtrair = timedelta(days=29) 
data_antiga = data_recente - dias_para_subtrair 

datas_e_horarios = pd.date_range(start=data_antiga, end=data_recente, freq='15min') 

df = pd.DataFrame({'DataHora': datas_e_horarios})


df['Hora'] = df['DataHora'].dt.hour
horas = df['Hora']

hora_formatada = datetime.now().strftime('%H:%M:%S')

df['Data'] = df['DataHora'].dt.date
datas = df['Data'] 

l_irradiacao_solar = []
l_temperatura_painel = []
l_temperatura_ambiente = []
l_status_painel = []

amanhecer = 6
anoitecer = 18

for hora in horas:
    if hora < anoitecer and hora >= amanhecer:
        irradiacao = np.random.randint(100, 1000)
    else:
        irradiacao = 0
    l_irradiacao_solar.append(irradiacao)

    if irradiacao < 0 or irradiacao > 1000:
        raise ValueError("Erro")

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
