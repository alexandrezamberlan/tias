# Tecnologias Inteligentes Aplicadas à Saúde

Material de apoio da disciplina nos cursos de Computação UFN.

## Mapa mental: Computação X Saúde X Rotinas

<img width="2994" height="1396" alt="mapaMentalTIAS" src="https://github.com/user-attachments/assets/7b968f62-2d60-4965-bdca-c2e4c8fd4518" />


### Conceitos e fundamentos

Na mineração de dados e no reconhecimento de padrões, **predição** e **previsão** até parecem a mesma coisa no uso cotidiano, mas tecnicamente não são idênticas — e essa diferença é importante dependendo do contexto.

---

#### Predição

* **Sentido geral:** é o termo mais amplo. Refere-se ao ato de **estimar um valor, classe ou comportamento futuro, presente ou até passado desconhecido**, com base em dados e modelos.
* **Âmbito:** pode envolver **classificação** (prever rótulos/categorias) ou **regressão** (prever valores numéricos).
* **Exemplos:**

  * Identificar se um cliente **vai** cancelar a assinatura (classificação).
  * Descobrir a idade de uma pessoa a partir de uma foto (a idade já ocorreu, mas não era conhecida — logo, é predição).
* **Importante:** a predição não precisa ser, necessariamente, sobre o futuro. Pode ser sobre o presente ou passado, desde que o dado real não seja conhecido no momento.


#### Previsão

* **Sentido mais específico:** normalmente associada a **séries temporais** e eventos futuros.
* **Âmbito:** quase sempre lida com estimativas de **valores futuros** baseadas em padrões históricos.
* **Exemplos:**

  * Estimar a temperatura de amanhã com base nos dados climáticos dos últimos 10 anos.
  * Projetar o faturamento do próximo trimestre.
* **Importante:** a previsão implica **tempo** — está sempre ligada ao que ainda vai acontecer.



**Resumo**

| Termo        | Escopo                             | Pode ser sobre passado/presente desconhecido? | Sempre envolve futuro? | Exemplo                                            |
| ------------ | ---------------------------------- | --------------------------------------------- | ---------------------- | -------------------------------------------------- |
| **Predição** | Mais amplo                         | Sim                                           | Não                    | Rotular a classe de um cliente atual (“alto risco”) |
| **Previsão** | Mais específico (séries temporais) | Não                                           | Sim                    | Prever o faturamento do mês que vem                |



**Na mineração de dados**:

* Se o modelo **não depende diretamente do tempo** (ex.: classificação de imagens, detecção de fraude em transações), está se falando de **predição**.
* Se seu modelo **usa o histórico temporal** para estimar algo que ainda vai acontecer, está se  referindo a **previsão**.

