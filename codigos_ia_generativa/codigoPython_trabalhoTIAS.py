
from google import genai

client = genai.Client(api_key="COLOQUE_SUA_API_KEY_AQUI")

#dados clinicos do cliente
medicamentos = ['novorapid', 'basaglar']
bolus_alimentar = 15 #15g de carboidrato por 1 unidade de insulina
bolus_correcao = 60 #60mg/dL por 1 unidade de insulina


#dados do registro da refeição
glicemia_atual = 132

descricao_alimentacao = """
hoje de manhã comi um pão frances com uma fatia de queijo prato mais um ovo cozido. Também tomei um café com leite, mais café do que leite. 
"""

contexto_json =  montar_json(medicamentos, bolus_alimentar, bolus_correcao, glicemia_atual, descricao_alimentacao)

papel_esperado_ia = """
Você é nutricionista especializada em contagem de carboidratos, calorias e cálculo da insulina necessária com base na alimentação e nos níveis de glicose informados.
"""

resposta = """
voce deve retornar SOMENTE um JSON contendo todos os alimentos com nome do alimento, quantidade de carboidrato, quantidade de caloria, quantidade de glicemia enviada e a quantidade de insulina necessária.
"""

prompt = f"""
Papel:
{papel_esperado_ia}

Contexto:
Utilize o JSON como fonte de entrada
{contexto_json}

Resposta:
{resposta}
"""

response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
)

resposta_json = response.candidates[0].content.parts[0].text.strip()

# Função para calcular os tokens
palavras = pergunta.split()
palavras += contexto.split()
palavras += json.split()
palavras += str(response).split()
num_palavras = len(palavras)
# Estimativa: 1 palavra ≈ 1.33 tokens (média comum)
tokens_estimados = int(num_palavras * 1.33)
print(f"Tokens estimados: {tokens_estimados}")

print(resposta_json)

lista_alimentos, calorias, carboidratos, qtd_insulina = desmontar_json(resposta_json)







x, y 
