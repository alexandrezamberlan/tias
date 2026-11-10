```python
import json
from openai import OpenAI

# 1. Inicializa o cliente da OpenAI
client = OpenAI()

# 2. Carrega o arquivo JSON
with open("prompt_text_to_sql.json", "r", encoding="utf-8") as arquivo:
    prompt_json = json.load(arquivo)

# 3. Recebe a pergunta
pergunta_usuario = input("Digite sua pergunta: ")

# 4. Atualiza a pergunta no JSON
prompt_json["entrada_usuario"]["pergunta"] = pergunta_usuario

# 5. Converte o JSON em texto
prompt_final = json.dumps(
    prompt_json,
    ensure_ascii=False,
    indent=4
)

# 6. Envia o prompt para a IA
resposta = client.responses.create(
    model="gpt-5.4",
    input=prompt_final
)

# 7. Recupera a resposta da IA
resultado = resposta.output_text

# 8. Exibe o resultado
print("\nResultado da IA:")
print(resultado)

```
