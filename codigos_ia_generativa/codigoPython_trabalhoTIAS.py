
from google import genai

client = genai.Client(api_key="COLOQUE_SUA_API_KEY_AQUI")

# O texto fornecido pelo usuário
contexto = """
sou diabetico tipo um, usuário de insulina lantus e insulina novorapid. Minha relação de insulina é de 15g por uma unidade. Para baixar a glicemia, uma unidade de insulina para 60 mg/dL.
"""

pergunta = """
hoje de manhã comi um pão frances com uma fatia de queijo prato mais um ovo cozido. Também tomei um café com leite, mais café do que leite. MInha glicemia em jejum foi de 129 mg/dL.
"""

prompt = f"""
voce é uma nutricionista especializada em contar carboidratos, calorias e calcular a necessidade de insulina a partir da alimentação informada e pela quantidade de glicose também informada.

voce deve retornar SOMENTE um JSON contendo nome do alimento, quantidade de carboidrato, quantidade de caloria, quantidade de glicemia enviada e a quantidade de insulina necessária.

Contexto:
{contexto}

Pergunta:
{pergunta}
"""

response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
)

json = response.candidates[0].content.parts[0].text.strip()

# Função para calcular os tokens
palavras = pergunta.split()
palavras += contexto.split()
palavras += json.split()
palavras += str(response).split()

num_palavras = len(palavras)

# Estimativa: 1 palavra ≈ 1.33 tokens (média comum)
tokens_estimados = int(num_palavras * 1.33)

print(f"Tokens estimados: {tokens_estimados}")

print(json)