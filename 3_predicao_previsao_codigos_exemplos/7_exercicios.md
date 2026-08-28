# Exercício de fixação de comparativo na PREDIÇÃO

Tendo como base os códigos comparativos de predição, refaça usando a seguinte fonte de dados... 


## Problema 1

https://github.com/alexandrezamberlan/tias/blob/main/3_predicao_previsao_codigos_exemplos/dados_predicao_modelos.csv

Esta base de dados sintética contém 250 linhas e foi estruturada especificamente para problemas de classificação binária, ideal para testar e comparar os algoritmos estudados.

### Estrutura do arquivo dados_predicao_modelos.csv 

  - X (Features): 
    - Idade: Valores inteiros simulando a idade do cliente (18 a 65 anos).
    - Renda_Anual_K: Renda anual simulada em milhares de unidades monetárias.
    - Score_Credito: Pontuação de crédito padrão (300 a 850).
    - Pontuacao_Engajamento: Nota de engajamento do cliente com a marca (1 a 10).
  
  - y (Target):
    - Compro_Produto: Variável binária (0 para não comprou, 1 para comprou) gerada a partir de uma combinação logística das features com ruído estatístico, garantindo que os modelos encontrem padrões reais sem overfitting perfeito.

## Problema 2

https://github.com/alexandrezamberlan/tias/blob/main/3_predicao_previsao_codigos_exemplos/dados_saude_predicao.csv

### Estrutura do Arquivo

  - X (Features):
    - Idade: Idade do paciente (25 a 80 anos).
    - Pressao_Arterial: Pressão arterial sistólica em mmHg (100 a 170).
    - Colesterol_Total: Nível de colesterol total em mg/dL (150 a 310).
    - Frequencia_Cardiaca_Max: Frequência cardíaca máxima atingida em bpm (60 a 110).
  
  - y (Target):
    - Risco_Internacao: Variável alvo (0 para baixo risco / sem internação, 1 para alto risco / necessidade de internação)

## Análise de resultados

  1) Analisar a matriz de confusão para saber se os dados usados no treinamento foram adequados (com ou sem overfitting)
  2) Analisar as variáveis de métricas Acurácia e F1-Score (bem como explica-las)

## Apresentação ao professor

  Após os resultados gerados, é preciso defender (com justificativa) se os dados utilizados no treinamento são válidos, ou seja, se o treinamento de fato surtiu efeito nos modelos e se algum desses modelos podem ser utilizados em produção.
