# Dados reais de internações hospitalares no Brasil
'''
1. SIH/SUS — Sistema de Informações Hospitalares

O SIH/SUS registra mensalmente as internações hospitalares realizadas em todo o Brasil. É uma fonte que permite montar séries temporais a partir de dados reais.

2. OpenDataSUS

A plataforma OpenDataSUS disponibiliza vários conjuntos de dados públicos, incluindo informações sobre internações (AIH — Autorizações de Internação Hospitalar) e ocupação hospitalar, geralmente em formatos CSV ou PDF.

3. bi-sus

O site bi-sus consolida e apresenta dados derivados do SIH/SUS de forma amigável e visual, com séries completas por ano, número de internações, custos, entre outros indicadores até dezembro de 2024.
'''

#Abaixo está um exemplo de script Python que simula como é possível:
#1. Carregar dados reais (supondo que foi baixado um CSV do OpenDataSUS ou SIH).
#2. Treinar um modelo de previsão (regressão linear simples) para estimar internações futuras.
#3. Comparar com o exemplo de predição (classificação clínica) no mesmo contexto da saúde.

import pandas as pd #dataframes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# ==================================================
# 1. PREPARAÇÃO DA PREVISÃO: DADOS REAIS DE INTERNAÇÕES
# ==================================================

# Exemplo fictício: meses de 1 a 36 (3 anos)
# Imagine que 'internacoes.csv' tenha colunas: 'ano', 'mes', 'internacoes'
# df = pd.read_csv('internacoes.csv')
# df['periodo'] = df['ano'] * 12 + df['mes']  # criar índice temporal

# Para demonstração, vamos criar dados semelhantes:
periodo = np.arange(1, 37)  # 36 meses
internacoes = np.array([
    11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000,
    15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 19500,
    20000, 20500, 21000, 21500, 22000, 22500, 23000, 23500, 24000,
    24500, 25000, 25500, 26000, 26500, 27000, 27500, 28000, 28500
])

df = pd.DataFrame({'periodo': periodo, 'internacoes': internacoes})

#  Treinar modelo de regressão linear
X = df['periodo'].values.reshape(-1, 1)
y = df['internacoes'].values
modelo_previsao = LinearRegression()
modelo_previsao.fit(X, y)

#  Prever os próximos 6 meses (mês 37 a 42)
futuros = np.arange(37, 43).reshape(-1, 1)
previstos = modelo_previsao.predict(futuros)

print("Previsão de internações para os próximos meses:", previstos)

#  Visualizar
plt.figure(figsize=(10, 5))
plt.plot(df['periodo'], y, label='Internações reais')
plt.plot(np.arange(1, 43), modelo_previsao.predict(np.arange(1, 43).reshape(-1, 1)), label='Tendência prevista')
plt.scatter(futuros, previstos, color='red', label='Previsão futura')
plt.xlabel("Período (meses)")
plt.ylabel("Internações")
plt.legend()
plt.title("Previsão de demanda hospitalar com dados reais simulados")
plt.show()

# ==================================================
# 2. PREDIÇÃO: CLASSIFICAÇÃO CLÍNICA (hipertensão)
# ==================================================

dados_pacientes = pd.DataFrame({
    'IMC': [24, 30, 28, 22, 35, 27, 40],
    'idade': [30, 50, 45, 28, 65, 55, 48],
    'historico_familiar': [0, 1, 1, 0, 1, 1, 1],
    'risco_hipertensao': [0, 1, 1, 0, 1, 1, 1]
})

Xc = dados_pacientes[['IMC', 'idade', 'historico_familiar']]
yc = dados_pacientes['risco_hipertensao']

X_train, X_test, y_train, y_test = train_test_split(Xc, yc, test_size=0.3, random_state=42)
modelo_predicao = LogisticRegression()
modelo_predicao.fit(X_train, y_train)

novo_paciente = [[29, 53, 1]]  # IMC=29, idade=53, histórico familiar
risco = modelo_predicao.predict(novo_paciente)[0]
print("Predição de risco de hipertensão (1=alto risco, 0=baixo risco):", risco)

'''
O que o código exemplifica

| Tipo     | Contexto Saúde           | O que faz                                        | Futuro obrigatório?                      |
| ---------| -------------------------| -------------------------------------------------| ---------------------------------------- |
| Previsão | Internações hospitalares | Estima próximas internações baseado em histórico | SIM - sempre estima o futuro             |
| Predição | Risco clínico individual | Classifica risco de hipertensão | dados clínicos | NÃO - pode ser paciente atual ou passado |


Como usar dados reais
1. Acesse plataformas como OpenDataSUS para baixar CSV com internações mensais por município, estado ou país.
2. Explore o bi-sus para verificar séries, tendências e valores agregados até 2024.
3. Prefira usar o SIH/SUS direto para mais granularidade — está disponível por meio do DATASUS.
'''