# Guia Rápido: Criando e Usando Sua API Key do Gemini

## 1. Criando Sua Conta no Google AI Studio

1. Acesse: [https://aistudio.google.com](https://aistudio.google.com)
2. Faça login com sua **Conta Google** (preferencialmente institucional).
3. Se for a primeira vez, você será guiado para configurar um projeto no Google Cloud.

## 2. Gerando Sua API Key

1. Após o login, clique em **"Obter chave de API"**.
2. Escolha entre:

   * **Novo projeto**: Cria um projeto do zero.
   * **Projeto existente**: Se já tiver um projeto no Google Cloud, selecione-o.
3. Clique em **"Criar chave de API"**.
4. Copie a chave gerada (formato: `AIza...`).

**Importante**: Guarde essa chave com segurança. Ela permite acesso à API e deve ser tratada como uma senha.


## 3. Usando Sua API Key com Python

1. Instale a biblioteca oficial:

   ```bash
   pip install google-genai
   ```
2. No seu código Python:

   ```python
   import os
   from google import genai

   # Defina sua chave de API como variável de ambiente
   os.environ["GEMINI_API_KEY"] = "sua_chave_aqui"

   client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

   prompt = "Explique a teoria da relatividade de forma simples."
   response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

   print(response.candidates[0].content.parts[0].text.strip())
   ```

**Dica**: Para maior segurança, defina a variável de ambiente `GEMINI_API_KEY` no seu sistema operacional ou em um arquivo `.env`.


## 4. Boas Práticas

* **Segurança**: Nunca compartilhe sua chave de API publicamente.
* **Limites**: A versão gratuita oferece até 1.500 requisições diárias com o modelo Gemini 1.5 Flash.
* **Gerenciamento**: Para visualizar e gerenciar suas chaves, acesse: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)


## 5. Observações Finais

* **Uso Educacional**: Incentive os alunos a criarem suas próprias chaves para evitar compartilhamento excessivo e possíveis custos inesperados.
* **Suporte**: Para dúvidas ou problemas, consulte a documentação oficial: [https://ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key)


Se desejar, posso preparar um **PDF resumido** deste guia para facilitar o compartilhamento com seus alunos. Gostaria que eu faça isso?
