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

  1) Analisar os resultados obtidos nos dados de treinamento e de teste, utilizando a matriz de confusão e as métricas de avaliação, buscando identificar possíveis sinais de overfitting. Não considere a matriz de confusão isoladamente como evidência de overfitting. Compare o desempenho do modelo nos diferentes conjuntos de dados.
  2) Apresente e explique as métricas Accuracy (Acurácia) e F1-Score dos modelos avaliados. Explique o significado de cada métrica e justifique qual delas é mais adequada para comparar os modelos utilizados neste problema.

     
## Apresentação ao professor

  Após os resultados gerados, é preciso defender (com justificativa)  se os modelos foram adequadamente treinados e se apresentam capacidade de generalização para dados não utilizados no treinamento, ou seja, se o treinamento de fato surtiu efeito nos modelos e se algum desses modelos podem ser utilizados em produção.

# PyCaret

Reproduzir, utilizando o PyCaret, o processo de treinamento, comparação e avaliação dos modelos preditivos desenvolvidos nos desafios anteriores, analisando se os resultados obtidos são consistentes com aqueles encontrados anteriormente.

1) Entenda o papel do PyCaret.
2) Entenda como configura-lo no seu ambiente de desenvolvimento.
3) Reimplemente os dois problemas anteriores utilizando o PyCaret, substituindo, sempre que possível, a implementação manual dos modelos pelas funcionalidades disponibilizadas pela biblioteca.
4) Utilize os recursos do PyCaret para treinar e comparar diferentes modelos de classificação, identificando quais modelos apresentam melhor desempenho. Utilize a funcionalidade de comparação de modelos do PyCaret (compare_models) e apresente os resultados obtidos.

## Importante

O objetivo do exercício não é apenas executar os comandos do PyCaret. O aluno deverá compreender e explicar o processo realizado pela ferramenta, interpretando os resultados obtidos.

Compare os resultados obtidos anteriormente, utilizando a implementação tradicional dos modelos, com os resultados obtidos utilizando o PyCaret.

O que é preciso saber:
- Os melhores modelos foram os mesmos?
- As métricas foram semelhantes?
- Houve diferenças significativas?
- Por que os resultados podem ter sido diferentes?
- Qual abordagem você considera mais adequada para este tipo de problema: implementação manual ou PyCaret? Justifique.
