# O texto fornecido pelo usuário
texto_usuario = """
sou diabetico tipo um, usuário de insulina lantus e insulina novorapid. Minha relação de insulina é de 15g por uma unidade. Para baixar a glicemia, uma unidade de insulina para 60 mg/dL. hoje de manhã comi um pão frances com uma fatia de queijo prato mais um ovo cozido. Também tomei um café com leite, mais café do que leite. me retorna em json a quantidade de quilo caloria (kcal), a quantidade de carboidrato (carb) e quantas unidades de insulina eu preciso tomar.
"""

# Função para calcular os tokens
palavras = texto_usuario.split()
num_palavras = len(palavras)

# Estimativa: 1 palavra ≈ 1.33 tokens (média comum)
tokens_estimados = int(num_palavras * 1.33)

print(f"Tokens estimados: {tokens_estimados}")


#1.000.000 de tokens de entrada por $1.25
#$10 por 1.000.000 tokens de saída
