# Métricas para comparar modelos

Para entender o desempenho de modelos de classificação, a matriz de confusão é o ponto de partida, pois ela mapeia os erros e acertos do modelo. A partir dela, derivamos métricas como acurácia, precisão, recall e F1-score.
A escolha da métrica ideal depende inteiramente do cenário do seu problema, especialmente se a sua base de dados for desbalanceada (ou seja, se houver muito mais exemplos de uma classe do que de outra).

## 1. O Ponto de Partida: Matriz de Confusão
A matriz de confusão é uma tabela que cruza os valores reais da base de dados com as predições do modelo. Para uma classificação binária (Positivo/Negativo), ela se divide em quatro quadrantes:

| | Predito como Positivo | Predito como Negativo |
|---|---|---|
| Realidade: Positivo | Verdadeiro Positivo (VP) (Acertou o positivo) | Falso Negativo (FN) (Errou: era positivo, disse que era negativo) |
| Realidade: Negativo | Falso Positivo (FP) (Errou: era negativo, disse que era positivo) | Verdadeiro Negativo (VN) (Acertou o negativo) |


## 2. Comparativo Direto das Métricas

| Métrica | O que ela mede? | Quando usar? | O perigo de usar erradamente |
|---|---|---|---|
| Acurácia | O percentual geral de acertos do modelo (positivos e negativos). | Quando as classes estão muito bem balanceadas na base de dados. | Se 99% da base for da classe A, um modelo burro que só chuta "classe A" terá 99% de acurácia, ocultando que ele não detecta a classe B. |
| Precisão | De tudo o que o modelo disse que era positivo, quanto ele realmente acertou. | Quando o custo de um Falso Positivo é muito alto. (Ex: Filtro de Spam — você não quer um e-mail importante na caixa de spam). | Se o modelo for ultra-conservador e classificar apenas 1 caso como positivo (e acertar), a precisão será de 100%, mas ele ignorou todos os outros positivos. |
| Recall (Sensibilidade) | De todos os positivos reais que existiam, quanto o modelo conseguiu encontrar. | Quando o custo de um Falso Negativo é intolerável. (Ex: Diagnóstico de doenças — deixar um paciente doente sem tratamento é perigoso). | Se o modelo chutar que todo mundo está doente, o Recall será 100%, mas o modelo será inútil porque gerará alarmes falsos para toda a base. |
| F1-Score | A média harmônica entre Precisão e Recall. Busca o equilíbrio entre ambas. | Excelente para bases desbalanceadas. Dá uma visão única quando você precisa de boa precisão e bom recall ao mesmo tempo. | Pode mascarar se o modelo é ligeiramente melhor em uma ponta do que na outra, caso você tenha preferência estrita por precisão ou recall. |


## Como aplicar nos seus modelos comparativos?
Ao treinar seus modelos com amostras, siga esta linha de raciocínio para a comparação:

   1. Olhe para a Acurácia apenas para ter um panorama global inicial.
   2. Analise a Matriz de Confusão para entender onde o modelo está errando (ele está gerando mais alarmes falsos ou deixando passar os alvos?).
   3. Use o F1-Score como critério de desempate principal se as suas classes forem desproporcionais na amostra.

