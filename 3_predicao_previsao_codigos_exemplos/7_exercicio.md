# Exercício de fixação de comparativo na PREDIÇÃO

Tendo como base os códigos comparativos de predição, refaça usando a seguinte fonte de dados... https://github.com/alexandrezamberlan/tias/blob/main/3_predicao_previsao_codigos_exemplos/dados_predicao_modelos.csv

Esta base de dados sintética contém 250 linhas e foi estruturada especificamente para problemas de classificação binária, ideal para testar e comparar os algoritmos estudados.

## Estrutura do arquivo dados_predicao_modelos.csv 

  - X (Features): 
    - Idade: Valores inteiros simulando a idade do cliente (18 a 65 anos).
    - Renda_Anual_K: Renda anual simulada em milhares de unidades monetárias.
    - Score_Credito: Pontuação de crédito padrão (300 a 850).
    - Pontuacao_Engajamento: Nota de engajamento do cliente com a marca (1 a 10).
  
  - y (Target):
    - Compro_Produto: Variável binária (0 para não comprou, 1 para comprou) gerada a partir de uma combinação logística das features com ruído estatístico, garantindo que os modelos encontrem padrões reais sem overfitting perfeito.
