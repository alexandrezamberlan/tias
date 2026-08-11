

from google import genai

client = genai.Client(api_key="API_TOKEN AQUI")

# O texto fornecido pelo usuário
contexto = """
sou diabetico tipo um, usuário de insulina lantus e insulina novorapid. Minha relação de insulina é de 15g por uma unidade. Para baixar a glicemia, uma unidade de insulina para 60 mg/dL.
hoje é 24 de setembro de 2025
"""

pergunta = """
hoje de manhã comi um pão frances com uma fatia de queijo prato mais um ovo cozido. Também tomei um café com leite, mais café do que leite.
"""


prompt = f"""
Você é um nutricionista que tem habilidade de contar carboidratos e calorias; e recomendar a quantidade de insulinas necessárias.

Com base na pergunta, retorne apenas um JSON com a quantidade de calorias, carboidratos e a quantidade de insulina necessárias que responde a pergunta.

Contexto:
{contexto}

Pergunta:
{pergunta}
"""

response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
)

# Extrai o texto da resposta
json = response.candidates[0].content.parts[0].text.strip()


# Função para calcular os tokens
palavras = pergunta.split()
palavras += contexto.split()
palavras += json.split()

num_palavras = len(palavras)

# Estimativa: 1 palavra ≈ 1.33 tokens (média comum)
tokens_estimados = int(num_palavras * 1.33)

print(f"Tokens estimados: {tokens_estimados}")


#1.000.000 de tokens de entrada por $1.25
#$10 por 1.000.000 tokens de saída

print(json)