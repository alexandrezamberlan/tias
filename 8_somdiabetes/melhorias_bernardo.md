Sinônimos: Modelo pronto de sinônimo do Hugging Face:
https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

Schema: Ajustar e deixar claro as chaves estrangeiras, limpar campos inúteis(economia de token e evita confusão e sql estranho)
	Trocar tipo do dado para descrição economiza token e melhora entendimento
	Colocar os tipos de campos que tem choices
	deixar as chaves estrangeiras explicitas, explicar bem para a ia n adivinhar
	remover campos lixos: slug, senha,....

regras de negocio, estão sendo mandadas? ou a ia adivinha?


baixar modelo:
pip install sentence-transformers
