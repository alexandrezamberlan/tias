
##  Para geração de gráfico de comparação

rode tudo junto no Google Colab

```python
import matplotlib.pyplot as plt

# 8. Criar DataFrame com os resultados
df_resultados = pd.DataFrame(resultados, columns=['Modelo', 'Acuracia', 'F1_Score_Macro'])

# 9. Salvar em CSV
df_resultados.to_csv('resultados_modelos_classificacao.csv', index=False)
print("\nResultados exportados para 'resultados_modelos_classificacao.csv' com sucesso!")

# 10. Plotar gráfico comparativo
plt.figure(figsize=(12, 6))
bar_width = 0.35
index = np.arange(len(df_resultados))

# Barras de acurácia
plt.bar(index, df_resultados['Acuracia'], bar_width, label='Acurácia', color='skyblue')

# Barras de F1-score macro ao lado
plt.bar(index + bar_width, df_resultados['F1_Score_Macro'], bar_width, label='F1-Score (Macro)', color='orange')

plt.xlabel('Modelo')
plt.ylabel('Pontuação')
plt.title('Comparação de Modelos - Acurácia vs F1-Score (Macro)')
plt.xticks(index + bar_width / 2, df_resultados['Modelo'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()
```


### O que faz o código

1. **Cria um DataFrame** com os resultados
2. **Exporta os dados para CSV** (você poderá baixar no Colab clicando no arquivo gerado)
3. **Gera um gráfico de barras duplas** comparando acurácia e F1-score macro de todos os modelos

