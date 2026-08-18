
## Substitutos para LogisticRegression (Modelos de Classificação)

### 1. **Decision Tree Classifier**

```python
from sklearn.tree import DecisionTreeClassifier
modelo = DecisionTreeClassifier()
```

* Baseado em regras tipo "if... else..."
* Interpretação fácil
* ⚠Pode sofrer com overfitting


### 2. **Random Forest Classifier**

```python
from sklearn.ensemble import RandomForestClassifier
modelo = RandomForestClassifier()
```

* Conjunto de várias árvores de decisão
* Mais robusto que Decision Tree
* Usa média das previsões das árvores
* Boa performance geral


### 3. **K-Nearest Neighbors (KNN)**

```python
from sklearn.neighbors import KNeighborsClassifier
modelo = KNeighborsClassifier(n_neighbors=5)
```

* Classifica com base nos vizinhos mais próximos
* Simples e eficaz para dados pequenos
* ⚠Lento para grandes volumes de dados


### 4. **Support Vector Machine (SVM)**

```python
from sklearn.svm import SVC
modelo = SVC()
```

* Tenta encontrar o melhor "limite" entre classes
* Eficiente em espaços de alta dimensão
* ⚠Pode ser lento e difícil de ajustar


### 5. **Naive Bayes**

```python
from sklearn.naive_bayes import GaussianNB
modelo = GaussianNB()
```

* Baseado em probabilidade (Teorema de Bayes)
* Rápido e eficiente
* Supõe independência entre variáveis (nem sempre é o caso)


### 6. **Gradient Boosting Classifier**

```python
from sklearn.ensemble import GradientBoostingClassifier
modelo = GradientBoostingClassifier()
```

* Método de boosting (modelo aprende com os erros anteriores)
* Alta acurácia
* ⚠Mais lento para treinar, mas muito eficaz


### 7. **XGBoost / LightGBM / CatBoost** (Modelos externos)

* Requerem instalação extra:

```bash
pip install xgboost lightgbm catboost
```

* Exemplo com XGBoost:

```python
from xgboost import XGBClassifier
modelo = XGBClassifier()
```

* Muito usados em competições de machine learning (Kaggle)
* Altíssima performance e controle
* Mais complexos, mas muito poderosos


## Como trocar?

Basta mudar a linha do modelo:

```python
# De:
modelo = LogisticRegression()

# Para, por exemplo:
modelo = RandomForestClassifier()
```

E manter o restante igual:

```python
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
```

## Comparações

Você pode comparar vários modelos com:

* `accuracy_score`
* `classification_report`
* `confusion_matrix`
* `cross_val_score`

