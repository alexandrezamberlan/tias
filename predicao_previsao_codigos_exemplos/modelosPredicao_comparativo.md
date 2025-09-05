
# Comparativo entre modelos de predição sob a base Glicose

```python
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

# 2. Features e variável alvo
features = ['INSULINA', 'KCAL', 'CARB', 'SONO', 'padel']
target = 'GLICEMIA'

X = df[features]
y = df[target]

# 3. Divisão treino/teste com estratificação
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

# 4. Padronizar (necessário para SVM e KNN)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Modelos de classificação
modelos = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'KNN': KNeighborsClassifier(),
    'Naive Bayes': GaussianNB(),
    'SVM': SVC(),
    'Gradient Boosting': GradientBoostingClassifier()
}

# 6. Avaliar cada modelo
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

# 7. Mostrar ranking final por F1-Score Macro
resultados.sort(key=lambda x: x[2], reverse=True)

print("\nRanking Final dos Modelos:")
print(f"{'Modelo':<25} {'Acurácia':<10} {'F1-Score (Macro)':<15}")
print("-" * 50)
for nome, acc, f1 in resultados:
    print(f"{nome:<25} {acc:<10.4f} {f1:<15.4f}")
```



## 🧾 Exemplo da Saída Final (Ranking)

```
Ranking Final dos Modelos:
Modelo                   Acurácia   F1-Score (Macro)
--------------------------------------------------
Random Forest            0.9200     0.9133
Gradient Boosting        0.9100     0.9041
Logistic Regression      0.8900     0.8800
...
```



### Nesta comparação há:

* **Acurácia** (o quão certo o modelo está no geral)
* **F1-Score Macro** (o quão bem ele está equilibrando o desempenho entre todas as classes)
* **Matriz de confusão e classificação detalhada**
* **Ranking ordenado por F1 Macro**, que é ideal para problemas multiclasse

