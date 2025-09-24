from openai import OpenAI

# inicializa o cliente com sua chave da OpenAI
client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

schema = """
Tabelas e colunas disponíveis:

Tabela: person
Colunas:
- id (bigint)
- first_name (varchar)
- last_name (varchar)
- address (varchar)
- gender (varchar)
- enabled (bit)
- wikipedia_profile_url (varchar)
- photo_url (varchar)

Tabela: book
Colunas:
- id (bigint)
- title (longtext)
- author (longtext)
- launch_date (date)
- price (decimal)

Tabela: person_books
Colunas:
- person_id (bigint)
- book_id (bigint)
"""

pergunta = "preciso o email e o número do celular do usuário que tenha no nome as palavras alexandre zamberlan"

prompt = f"""
Você é um gerador de SQL para MySQL.

Com base no esquema abaixo, gere apenas o SQL que responde a pergunta.

Esquema:
{schema}

Pergunta:
{pergunta}
"""

# chamada ao modelo GPT-5
response = client.chat.completions.create(
    model="gpt-5",   # pode usar "gpt-4o-mini" ou outro disponível
    messages=[
        {"role": "system", "content": "Você é um gerador de SQL para MySQL."},
        {"role": "user", "content": prompt}
    ]
)

sql_bruto = response.choices[0].message.content.strip()

# limpeza do markdown SQL
if sql_bruto.startswith('```sql'):
    sql_bruto = sql_bruto[6:]
if sql_bruto.startswith('```'):
    sql_bruto = sql_bruto[3:]
if sql_bruto.endswith('```'):
    sql_bruto = sql_bruto[:-3]

print(sql_bruto)
