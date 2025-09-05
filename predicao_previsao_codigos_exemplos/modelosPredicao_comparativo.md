# Comparativo entre os modelos de predição

1. Treina **vários modelos de classificação**
2. Usa seus dados `X` e `y` (carregar isso antes).
3. Mostra a **acurácia de cada modelo** de forma comparativa.


```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Modelos de classificação
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# (Opcional) Modelos mais avançados
# !pip install xgboost lightgbm catboost
# from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier
# from catboost import CatBoostClassifier

# ---------------------
# 1. Substitua X e y pelos seus dados
# ---------------------
# Exemplo fictício se você não tiver dados ainda:
# from sklearn.datasets import load_breast_cancer
# data = load_breast_cancer()
# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = pd.Series(data.target)

# 2. Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Padronização (importante para modelos como SVM e KNN)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Definir os modelos
modelos = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'KNN': KNeighborsClassifier(),
    'Naive Bayes': GaussianNB(),
    'SVM': SVC(),
    'Gradient Boosting': GradientBoostingClassifier(),
    # 'XGBoost': XGBClassifier(),
    # 'LightGBM': LGBMClassifier(),
    # 'CatBoost': CatBoostClassifier(verbose=0)
}

# 5. Treinar e testar os modelos
resultados = []

for nome, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    resultados.append((nome, acc))

# 6. Exibir os resultados
resultados.sort(key=lambda x: x[1], reverse=True)
print("Acurácia dos modelos:")
for nome, acc in resultados:
    print(f"{nome:<20} -> Acurácia: {acc:.4f}")
```



## O que esse código faz?

* Testa 7 modelos clássicos de classificação.
* Padroniza os dados (essencial para modelos como SVM, KNN).
* Compara todos com base na **acurácia**.
* Permite fácil substituição ou adição de modelos como XGBoost e LightGBM (comentados ali).


## Exemplo de saída:

```
Acurácia dos modelos:
Random Forest        -> Acurácia: 0.9650
Gradient Boosting    -> Acurácia: 0.9561
Logistic Regression  -> Acurácia: 0.9474
SVM                  -> Acurácia: 0.9386
KNN                  -> Acurácia: 0.9211
Naive Bayes          -> Acurácia: 0.9123
Decision Tree        -> Acurácia: 0.9035
```

