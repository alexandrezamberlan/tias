
# Guia rápido: Criando e usando sua API Key da OpenAI

## 1. Criando sua conta

1. Acesse: [https://platform.openai.com](https://platform.openai.com)
2. Clique em **Sign up**.
3. Faça cadastro com:

   * **E-mail acadêmico** (recomendado), ou
   * Conta **Google** ou **Microsoft**.


## 2. Gerando sua API Key

1. Depois de logado, acesse: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Clique em **Create new secret key**.
3. Dê um nome para a chave (ex.: `meu_teste_api`).
4. Copie a chave gerada (formato `sk-xxxxx...`).
   Guarde-a, pois não será exibida novamente.


## 3. Usando sua chave com Python

### Instale a biblioteca

```bash
pip install openai
```

### Código exemplo

```python
import os
from openai import OpenAI

# Defina sua chave de API (melhor em variável de ambiente)
os.environ["OPENAI_API_KEY"] = "sua_chave_aqui"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",  # ou outro disponível
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Explique o que é banco de dados relacional em 3 linhas."}
    ]
)

print(response.choices[0].message.content)
```

## 4. Boas práticas

- Nunca compartilhe sua chave publicamente (GitHub, fóruns, etc).
- Prefira salvar em **variáveis de ambiente**, não diretamente no código.
- Acompanhe o uso e custos em: [https://platform.openai.com/usage](https://platform.openai.com/usage).


## 5. Observações

* O uso da API é **pago conforme consumo** (tokens).
* Pode haver **créditos iniciais gratuitos** para novas contas.


Quer que eu prepare também um **PDF resumido** desse guia, que você possa entregar diretamente aos seus alunos?
