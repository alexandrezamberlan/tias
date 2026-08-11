import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score

# Modelos de classificação
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# 1. Carregar os dados
url = 'https://raw.githubusercontent.com/alexandrezamberlan/tias/refs/heads/main/predicao_previsao_codigos_exemplos/glicose_data.csv'
df = pd.read_csv(url)

# 2. Definir as variaveis de interesse em novo dataframe
df_com_variaveis_interesse = df[['GLICEMIA', 'INSULINA','KCAL','CARB', 'SONO', 'padel']]

# 3. Apagar linhas com colunas em branco ou nulas
df_com_variaveis_interesse = df_com_variaveis_interesse.dropna()

# 4. Substituir strings por inteiros
df_com_variaveis_interesse["GLICEMIA"] = df_com_variaveis_interesse["GLICEMIA"].replace({
    "Acima": 2,
    "Normal": 1,
    "Abaixo": 0
})

df_com_variaveis_interesse["KCAL"] = df_com_variaveis_interesse["KCAL"].replace({
    "Acima": 2,
    "Recomendado": 1,
    "Abaixo": 0
})

df_com_variaveis_interesse["CARB"] = df_com_variaveis_interesse["CARB"].replace({
    "Acima": 2,
    "Recomendado": 1,
    "Abaixo": 0
})

# 5. Features e variável alvo
features = ['INSULINA', 'KCAL', 'CARB', 'SONO', 'padel']
target = 'GLICEMIA'

X = df_com_variaveis_interesse[features]
y = df_com_variaveis_interesse[target]

# 6. Divisão treino/teste com estratificação
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

# 7. Padronizar (necessário para SVM e KNN)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 8. Modelos de classificação
modelos = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'KNN': KNeighborsClassifier(),
    'Naive Bayes': GaussianNB(),
    'SVM': SVC(),
    'Gradient Boosting': GradientBoostingClassifier()
}

# 9. Avaliar cada modelo
resultados = []

print("Avaliação dos Modelos:\n")

for nome, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro', zero_division=0)
    
    resultados.append((nome, acc, f1))

    print(f"Modelo: {nome}")
    print(f"Acurácia: {acc:.4f}")
    print(f"F1-Score (Macro): {f1:.4f}")
    print("Relatório de Classificação:")
    print(classification_report(y_test, y_pred, zero_division=0))
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
    print("-" * 60)

# 10. Mostrar ranking final por F1-Score Macro
resultados.sort(key=lambda x: x[2], reverse=True)

print("\nRanking Final dos Modelos:")
print(f"{'Modelo':<25} {'Acurácia':<10} {'F1-Score (Macro)':<15}")
print("-" * 50)
for nome, acc, f1 in resultados:

    print(f"{nome:<25} {acc:<10.4f} {f1:<15.4f}")
