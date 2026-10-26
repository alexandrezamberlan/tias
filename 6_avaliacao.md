# Avaliação

## Considere a frase: “A Maria contou para a Ana que ela foi promovida.”

Qual componente do Transformer é diretamente usado para aplicar pesos e decidir se “ela” tende a se referir mais a “Maria” ou “Ana”, a partir do contexto?

O componente do Transformer diretamente responsável por isso é o Mecanismo de Auto-Atenção (Self-Attention Mechanism). Mais especificamente, dentro desse mecanismo, o cálculo que define se "ela" se refere a "Maria" ou a "Ana" é o produto escalar das matrizes de Query (Consulta) e Key (Chave), que resulta nos chamados Pesos de Atenção (Attention Weights).

Veja como o Transformer processa isso de forma simplificada:

    1. A Consulta (Query): Quando o modelo está processando a palavra "ela", ele gera um vetor de consulta para essa palavra, perguntando ao restante da frase: "Quem é o sujeito feminino que realizou ou sofreu a ação aqui?"

    2. As Chaves (Keys): Todas as outras palavras da frase (incluindo "Maria" e "Ana") possuem vetores de chave que dizem o que elas representam no contexto.

    3. O Cálculo do Peso: O modelo multiplica a Query de "ela" pela Key de "Maria" e pela Key de "Ana". O resultado que tiver maior valor numérico (após passar por uma função chamada Softmax) recebe o maior peso.

    4. O Contexto (Value): Graças ao restante da frase ("contou para a Ana que..."), a palavra "Maria" geralmente ganha um peso de atenção muito maior nesse cálculo, permitindo que o modelo decida textualmente que "ela" se refere à Maria.

    Em modelos modernos, esse processo ocorre em múltiplos caminhos paralelos chamados de Multi-Head Attention (Atenção de Múltiplas Cabeças), onde uma "cabeça" pode focar em relações gramaticais, outra em proximidade física das palavras e outra na resolução desse tipo de ambiguidade (chamada de correferência).

## Analise as duas afirmações:

I. “Embeddings colocam tokens num espaço numérico com semântica aproximada.”
II. “O Transformer transforma esses vetores em representações contextualizadas, reduzindo ambiguidades.”

Qual alternativa está mais correta?

Ambas as afirmações estão totalmente corretas, tornando a alternativa que valida I e II como verdadeiras a correta.

A relação complementar entre as duas afirmações define perfeitamente como funciona o pipeline de Processamento de Linguagem Natural moderno:

    - Afirmação I está correta: O Static Embedding (como as camadas iniciais de projeção de tokens) mapeia cada palavra/token para um vetor denso em um espaço geométrico multibidimensional. Nesse espaço, tokens com significados ou usos semelhantes ficam geometricamente próximos (proximidade semântica por cosseno ou distância euclidiana). No entanto, de forma isolada, esse mapeamento é estático (a palavra "banco" teria inicialmente o mesmo vetor, seja o estabelecimento financeiro ou o assento da praça).

    - Afirmação II está correta: É aí que entra o Transformer. Ao receber esses embeddings estáticos combinados com os Positional Encodings, o mecanismo de Auto-Atenção do Transformer analisa o contexto completo da frase. Ele recalcula os vetores misturando as informações dos tokens vizinhos. Esse processo transforma o vetor estático original em um embedding contextualizado, resolvendo ambiguidades e distanciando o "banco" (assento) do "banco" (dinheiro) baseado nas palavras ao redor.

## Um servidor MCP expõe três tipos de componentes. Quais são?

No Model Context Protocol (MCP), desenvolvido para padronizar a comunicação entre inteligências artificiais e fontes externas de dados, um servidor expõe três componentes/primitivas principais: 

    1. Tools (Ferramentas): São funções executáveis que o modelo de IA pode invocar para realizar ações dinâmicas no mundo real ou em sistemas de software. O uso das tools é controlado pelo próprio modelo de IA, que decide o momento exato de chamá-las com base na pergunta do usuário.
	
        - Exemplos: Executar um script em Python, fazer uma chamada de API REST, pesquisar na web ou realizar uma consulta de escrita em um banco de dados.

    2. Resources (Recursos): São fontes de dados de apenas leitura (read-only) que fornecem informações de contexto bruto para a IA. Eles são identificados por URIs padronizadas e seu carregamento costuma ser controlado pelo aplicativo hospedeiro (host) ou injetado de forma fixa no contexto.
	
        - Exemplos: O conteúdo textual de um arquivo local, esquemas de bancos de dados, logs de sistema ou documentações de referência. 

    3. Prompts (Instruções): São templates reutilizáveis, parametrizáveis e pré-configurados de mensagens e instruções que ajudam a estruturar e guiar as interações com o modelo. Eles são controlados diretamente pelo usuário humano, servindo como atalhos para fluxos complexos.
	
        - Exemplos: Modelos de comandos (como os comandos de barra /), templates estruturados para revisão de código de programação ou fluxos guiados para análise de negócios. 


Essas três primitivas cobrem todas as frentes necessárias para que um agente de IA trabalhe com autonomia: ações em tempo real (Tools), dados contextuais (Resources) e guias de comportamento (Prompts). 

## Quando você transforma “cor = azul/vermelho/verde” em colunas com 0 e 1 (ex.: [1,0,0]), isso é:

Isso é chamado de One-Hot Encoding (ou codificação One-Hot).

Em ferramentas de análise de dados e Machine Learning em Python, esse processo também é conhecido como criação de variáveis dummy (ou dummy encoding).

Veja como funciona na prática com o exemplo:

• azul vira [1, 0, 0]
• vermelho vira [0, 1, 0]
• verde vira [0, 0, 1]

Por que isso é usado?

Os algoritmos de Machine Learning operam com equações matemáticas e não conseguem entender categorias em formato de texto (como "azul" ou "verde"). Transformar essas categorias em colunas binárias de 0 e 1 permite que o modelo calcule pesos para cada cor sem criar uma falsa ordem de grandeza entre elas (o que aconteceria se você usasse apenas números sequenciais como azul=1, vermelho=2, verde=3).

## Você indexou uma transcrição em chunks no Neo4j e quer que, para cada pergunta, o banco retorne apenas os trechos mais relevantes, sem trazer “muita coisa”. Qual ajuste conversa mais diretamente com isso?

O ajuste que conversa mais diretamente com isso é a redução do top_k (número de vizinhos mais próximos retornados) na busca vetorial, combinado com o ajuste de um limiar de similaridade (similarity score threshold).

Como você já transformou a transcrição em chunks e os indexou no Neo4j, o banco de dados calcula a proximidade matemática entre o vetor da pergunta e o vetor de cada trecho. Para limitar a quantidade de informação e trazer apenas o que é estritamente relevante, você deve atuar em dois pontos principais:

    1. Limitar a quantidade (top_k)

    O parâmetro top_k determina o número máximo de nós/chunks que a busca vetorial vai retornar. Se ele estiver configurado como 10 ou 5, o Neo4j sempre trará essa quantidade, mesmo que os últimos itens tenham pouca relação com a pergunta.
        
        - Ação: Reduza o top_k para um valor baixo (ex: top_k: 2 ou top_k: 3).

    2. Filtrar pela qualidade (Limiar de Similaridade)

    Para garantir que o banco não retorne lixo caso a pergunta não tenha nada a ver com a transcrição, você deve aplicar um filtro no score de similaridade (como a similaridade de cosseno).

        - Ação: Filtre os resultados para retornar apenas nós onde o score seja maior que um valor estipulado (ex: WHERE score > 0.75).


### Exemplo Prático em Cypher (Neo4j)

Se você estiver usando o procedimento de busca vetorial do Neo4j, o ajuste no código fica assim:

```cypher
CALL db.index.vector.queryNodes('transcricao_embeddings', $top_k, $pergunta_embedding)
YIELD node, score
// AJUSTE: Filtra para trazer apenas o que é muito relevante
WHERE score > 0.78  
RETURN node.text AS trecho, score
LIMIT $top_k // AJUSTE: Defina $top_k como 2 ou 3 no seu backend
```

Outro ajuste arquitetural importante: O tamanho do Chunk

Se mesmo trazendo apenas 1 ou 2 chunks a resposta ainda parecer "muita coisa", o problema pode estar no tamanho do chunk (Chunk Size) definido no momento da indexação. Chunks de 1000 tokens trazem muito texto de uma vez; se o seu objetivo é precisão cirúrgica, reindexar o documento com chunks menores (ex: 200 a 300 tokens) com alguma sobreposição (chunk overlap) fará o Neo4j retornar trechos bem mais específicos.


### Neo4j e Chunk

O Neo4j é um banco de dados orientado a grafos.
Diferente dos bancos de dados tradicionais (como MySQL ou Excel, que organizam os dados em tabelas, linhas e colunas), o Neo4j organiza as informações como uma rede de conexões humanas ou nós interligados. Ele armazena os dados em duas estruturas principais:
    
    - Nós (Nodes): São as entidades (ex: uma Pessoa, uma Empresa, ou um Trecho de Texto).
    - Relacionamentos (Edges/Relationships): São as linhas que conectam esses nós, mostrando como eles se relacionam (ex: Maria TRABALHA_NA Empresa X).

Por que ele é tão usado em IA? Porque além de mapear essas conexões complexas com muita rapidez, o Neo4j possui suporte nativo para Busca Vetorial. Isso significa que ele consegue guardar textos, transformá-los em números (vetores/embeddings) e encontrar quais textos são parecidos entre si de forma matemática.

#### Chunk

Em computação e Inteligência Artificial, Chunk significa simplesmente um "pedaço" ou "fragmento" de um texto maior.
Modelos de linguagem (como o ChatGPT ou o Claude) possuem um limite de texto que conseguem ler e processar de uma só vez (chamado de janela de contexto). Se você der um livro de 500 páginas ou uma transcrição de uma reunião de 3 horas para a IA ler a cada pergunta do usuário, o processo fica muito lento, caro e ineficiente.

A solução é o Chunking (fatiamento):
    1. Você pega essa transcrição gigante de 3 horas.
    2. Corta o texto em pedacinhos menores (ex: blocos de 3 parágrafos ou 200 palavras cada).
    3. Cada um desses pedacinhos é um Chunk.

No cenário da sua pergunta anterior, você fez exatamente isto:

    1. Pegou uma transcrição longa e cortou em vários Chunks (pedaços de texto).
    2. Salvou cada um desses pedaços como um Nó dentro do Neo4j.
    3. Quando o usuário faz uma pergunta, o sistema não lê o documento inteiro. Ele vai no Neo4j, faz uma busca rápida e diz: "Olha, de todos os 500 chunks que eu tenho guardados aqui, estes 2 chunks (nós) são os únicos que respondem à pergunta do usuário".

## Um agente em um editor usa MCP para chamar uma ferramenta que: (1) transforma a pergunta em embedding, (2) busca top-K chunks num índice vetorial, (3) aplica filtro por serviço/ambiente e reranking, e (4) injeta os trechos no prompt antes da resposta. Qual alternativa descreve melhor o papel de RAG e MCP nesse fluxo?

A alternativa que descreve perfeitamente esse fluxo é: 

    RAG é o padrão de arquitetura do pipeline de busca e recuperação de dados, enquanto o MCP é o protocolo de comunicação que permite ao agente invocar e executar essa capacidade externa.

Para detalhar o papel de cada um nesse cenário:
    - O papel do RAG (Retrieval-Augmented Generation): Todo o pipeline descrito do passo (1) ao (4) — transformar em embedding, buscar os top-K chunks no índice vetorial, aplicar filtros/reranking e injetar o contexto no prompt — é a definição clássica e completa de uma arquitetura RAG Avançado. O RAG é o conceito/padrão de projeto que resolve o problema de falta de conhecimento específico ou desatualização do modelo de IA.

    - O papel do MCP (Model Context Protocol): O modelo de IA rodando no editor não sabe, por padrão, como acessar seu banco de dados ou como rodar esse pipeline de busca. O MCP entra como a infraestrutura de comunicação (o canal padronizado). Ele expõe esse pipeline RAG sob a forma de uma Tool (Ferramenta). Quando o agente percebe que precisa de dados do documento, ele usa o protocolo MCP para disparar essa ferramenta, delegando a computação pesada (busca vetorial, filtragem e reranking) para o servidor MCP correspondente e recebendo de volta apenas o texto limpo para injetar no prompt.

O MCP viabiliza a execução, e o RAG define a estratégia de recuperação dos dados.

## No contexto do TensorFlow.js, o que é um tensor?

No TensorFlow.js (e em machine learning no geral), um tensor é a estrutura de dados fundamental. 

Ele é essencialmente uma generalização de matrizes e vetores para dimensões maiores:

    - Um tensor de 0 dimensões é um único número (escalar).
    - Um tensor de 1 dimensão é uma lista de números (vetor).
    - Um tensor de 2 dimensões é uma tabela de números (matriz).
    - Um tensor de 3 ou mais dimensões é uma matriz multidimensional (ex.: uma imagem colorida digitalizada, que possui largura, altura e 3 canais de cor).

Os modelos e algoritmos usam essas estruturas numéricas para realizar os cálculos matemáticos pesados e aprender os padrões dos dados.