'''
    O código ilustra a aplicação da predição e da previsão
    
    Predição: modelo estima se um paciente tem risco de desenvolver hipertensão com base nos dados coletados (IMC, idade, histórico familiar). Pode ser sobre um paciente atual ou de um exame passado — não precisa ser futuro. Contexto: Risco de hipertensão - classifica em alto, baixo risco.
    
    Previsão: modelo prevê o número de internações nos próximos meses com base no histórico de internações mensais. Sempre sobre o futuro, usando padrão temporal. Contexto: Demanda hospitalar - estima número de internações futuras usando histórico mensal.    
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# =========================================
# 1. PREDIÇÃO: risco de hipertensão
# =========================================

# Dados fictícios: IMC, idade, histórico familiar (1=sim, 0=não)
dados_pacientes = pd.DataFrame({
    'IMC': [22, 28, 31, 26, 35, 29, 40],
    'idade': [25, 45, 50, 35, 60, 55, 48],
    'historico_familiar': [0, 1, 1, 0, 1, 1, 1],
    'risco_hipertensao': [0, 1, 1, 0, 1, 1, 1]  # 1=alto risco, 0=baixo risco
})

X = dados_pacientes[['IMC', 'idade', 'historico_familiar']]
y = dados_pacientes['risco_hipertensao']

# Treinar modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
modelo_predicao = LogisticRegression()
modelo_predicao.fit(X_train, y_train)

# Predição para um novo paciente (pode ser consulta de hoje)
novo_paciente = [[30, 52, 1]]  # IMC=30, idade=52, histórico familiar=sim
print("Predição de risco de hipertensão (1=alto, 0=baixo):",
      modelo_predicao.predict(novo_paciente)[0])

# =========================================
# 2. PREVISÃO: demanda hospitalar
# =========================================

# Dados fictícios de internações mensais em um hospital
meses = np.arange(1, 13)  # de janeiro (1) a dezembro (12)
internacoes = np.array([120, 135, 150, 160, 155, 170, 180, 190, 200, 210, 220, 230])

# Treinar modelo de regressão para série temporal
meses = meses.reshape(-1, 1)
modelo_previsao = LinearRegression()
modelo_previsao.fit(meses, internacoes)

# Previsão para os próximos 3 meses
meses_futuros = np.array([13, 14, 15]).reshape(-1, 1)
internacoes_previstas = modelo_previsao.predict(meses_futuros)

print("Previsão de internações para os próximos meses:", internacoes_previstas)

# Visualizar tendência
plt.plot(np.arange(1, 16),
         modelo_previsao.predict(np.arange(1, 16).reshape(-1, 1)),
         label="Tendência prevista")
plt.scatter(np.arange(1, 13), internacoes, color='blue', label="Dados reais")
plt.scatter([13, 14, 15], internacoes_previstas, color='red', label="Previsão futura")
plt.xlabel("Mês")
plt.ylabel("Número de internações")
plt.legend()
plt.show()


