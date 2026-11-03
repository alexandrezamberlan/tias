# 1. Standard Library (Bibliotecas nativas do Python)
import datetime
import json
import os

# 2. Third-Party Libraries (Bibliotecas de terceiros)
from decouple import config
import google.generativeai as genai

# 3. Django Components (Componentes específicos do Django)
from django.db import connection, connections
from django.db.migrations.executor import MigrationExecutor
from django.template import Context, Template


class Conecta:
    todos_tokens = 0

    @staticmethod
    def testar_conexao(model):
        try:
            resposta = model.generate_content("ping")
            print("Status OK — respondeu ao ping.")
            return True
        except Exception as e:
            print("Erro ao testar conexão:", e)
            return False

    @staticmethod
    def conectar_api():  # conecta com api gemini
        # Configura o Gemini API
        try:
            # Configura a chave da API do Gemini
            try:
                api_key = config('GEMINI_API_KEY')
            except:
                api_key = os.getenv('GEMINI_API_KEY')

            if not api_key:
                raise Exception(
                    "Chave API do Google não encontrada. Configure GOOGLE_API_KEY nas variáveis de ambiente ou no .env")

            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            # model = genai.Client()
            tokens_lista = str(model.count_tokens(contents="Conexão inicial Gemini 2.5 Flash")).split(' ')
            Conecta.todos_tokens += int(tokens_lista[1])
            # print("Conectado ao Gemini 2.5 Flash com sucesso.", f"Total tokens usados: {Conecta.todos_tokens}")

            print('Testando conexão com API.......')
            if model and not isinstance(model, str):
                Conecta.testar_conexao(model)
            else:
                print('Nenhum modelo foi carregado após conexão com API')
            return model
        except genai.types.BlockedPromptException:
            return "Erro: Prompt bloqueado pela API."
        except genai.types.RateLimitException:
            return "Erro: Limite de requisições atingido (quota)."
        except genai.types.APIConnectionException:
            return "Erro: Falha de conexão com a API."
        except Exception as e:
            return f"Erro inesperado: {e}"


    ####### PARTE DO ESPECIALISTA EM SQL #######
    @staticmethod
    def houve_alteracao_banco():
        try:
            connection = connections['default']
            executor = MigrationExecutor(connection)

            # Pega as migrações aplicadas e as pendentes
            applied_migrations = executor.loader.applied_migrations
            all_migrations = executor.loader.graph.nodes.keys()

            # Diferença indica migrações pendentes
            pending = set(all_migrations) - set(applied_migrations)

            if pending:
                print("Há migrações pendentes:")
                for mig in pending:
                    print(mig)
                return True
            else:
                print("Todas as migrações estão aplicadas.")
                return False
        except Exception as e:
            print('Erro', e)
            return False

    @staticmethod
    def atualizar_contexto_json():
        # Lê o arquivo schema.json para entender o banco de dados
        try:
            schema_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'schema.json')

            with open(schema_path, "r", encoding='utf-8') as file:
                schema_data = json.load(file)
                return f"Contexto atualizado com sucesso. Schema carregado com {len(schema_data.get('models', {}))} modelos."
        except Exception as e:
            return f"Erro ao atualizar contexto. Exceção: {str(e)}"

    @staticmethod
    def atualizar_contexto_toon():
        # Lê o arquivo schema.json para entender o banco de dados
        try:
            schema_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'schema.toon')

            with open(schema_path, "r", encoding='utf-8') as file:
                schema_data = file.read()
                return f"Contexto atualizado com sucesso. Schema carregado com {len(schema_data.get('models', {}))} modelos."
        except Exception as e:
            return f"Erro ao atualizar contexto. Exceção: {str(e)}"

    @staticmethod
    def carregar_schema_json():
        # Carrega o esquema do banco de dados do arquivo schema.json
        try:
            schema_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'schema.json')

            with open(schema_path, "r", encoding='utf-8') as file:
                schema_data = json.load(file)
                return schema_data
        except Exception as e:
            print(f"Erro ao carregar schema: {str(e)}")
            return None

    @staticmethod
    def carregar_schema_toon():
        # Carrega o esquema do banco de dados do arquivo schema.toon
        try:
            schema_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'schema.toon')

            with open(schema_path, "r", encoding='utf-8') as file:
                schema_string = file.read()
                return schema_string
        except Exception as e:
            print(f"Erro ao carregar schema: {str(e)}")
            return None

    @staticmethod
    def gerar_sql(pergunta):
        try:
            model = Conecta.conectar_api()  # conecta com gemini api
            if isinstance(model, str):  # Se retornou erro
                return model

            # # Verifica se houve alteração pelo migrations
            # if Conecta.houve_alteracao_banco():
            #     Conecta.atualizar_contexto()

            # Carrega o schema do banco de dados
            schema_data = Conecta.carregar_schema_toon()
            if not schema_data:
                return "Erro ao carregar o esquema do banco de dados."

            # Constrói o prompt com o contexto do schema
            context_prompt = f"""
            Você é um especialista em SQL para Django. Gere UMA consulta SQL válida baseada nas tabelas disponíveis.

            O Schema é:
            {schema_data}

            REGRAS CRÍTICAS:
            1. Retorne APENAS UMA instrução SELECT válida
            2. NÃO use ponto e vírgula (;)
            3. FAÇA SOMENTE SELEÇÃO de dados (SELECT). NÃO use INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, EXEC, MERGE ou TRUNCATE
            4. Para buscar por nome ou campos descritivos use: WHERE campo LIKE '%parte_do_texto%'
            5. SEMPRE selecione campos completos (ex: u.nome, não SUBSTRING ou similar)
            6. NÃO use funções que dividem strings em caracteres
            7. Máximo 5 colunas no SELECT
            8. Ignore campos padroes do django
            9. Trate dados com letras maiusculas e minusculas igualmente (case insensitive)
            10. Sinônimos comuns: usuario = participante = estudante = aluno; participação = frequência = presença;

            PERGUNTA: {pergunta}

            SQL:
            """

            # total_tokens: 53
            response = model.generate_content(context_prompt)
            tokens_lista = str(model.count_tokens(contents=context_prompt + response.text)).split(' ')
            Conecta.todos_tokens += int(tokens_lista[1])
            print("Conectado ao Gemini 2.5 Flash para aplicar consulta.",
                  f"Total tokens usados: {Conecta.todos_tokens}")
            sql_resposta = response.text.strip()

            # Remove possíveis marcadores de código markdown
            if sql_resposta.startswith('```sql'):
                sql_resposta = sql_resposta[6:]
            if sql_resposta.startswith('```'):
                sql_resposta = sql_resposta[3:]
            if sql_resposta.endswith('```'):
                sql_resposta = sql_resposta[:-3]

            # Remove ponto e vírgula no final e quebras de linha extras
            sql_limpo = sql_resposta.strip()
            if sql_limpo.endswith(';'):
                sql_limpo = sql_limpo[:-1]

            # Se houver múltiplas instruções separadas por ';', pega apenas a primeira
            if ';' in sql_limpo:
                sql_limpo = sql_limpo.split(';')[0].strip()

            return sql_limpo
        except Exception as e:
            erro = f"Não foi possível conectar no servidor para gerar a consulta. Por favor, tente novamente mais tarde. Erro: {str(e)}"
            return erro

    @staticmethod
    def checar_consulta_segura(sql):  # NAO ALTERAR, REUTILIZAR
        sql = sql.strip().lower()

        # Primeiro, verifica se a consulta começa com SELECT ou WITH
        if not sql.startswith("select") and not sql.startswith("with"):
            return False

        # Segundo, verifica se há ponto e vírgula no meio da consulta
        if ';' in sql:
            parts = [p.strip() for p in sql.split(';') if p.strip()]
            for part in parts:
                if not part.startswith('select') and not part.startswith('with'):
                    return False

        # Por fim, verifica se há palavras-chave potencialmente perigosas
        forbidden = ['insert', 'update', 'delete', 'drop', 'alter', 'create', 'exec', 'merge', 'truncate']
        if any(word in sql for word in forbidden):
            return False

        return True

    @staticmethod
    def executar_sql(sql):  # NAO ALTERAR, REUTILIZAR
        try:
            # Verifica se a consulta é segura
            if not Conecta.checar_consulta_segura(sql):
                return "Uma consulta potencialmente insegura foi detectada. Por favor, tente novamente."

            # Conecta no banco com cursor e obtém os resultados
            with connection.cursor() as cursor:
                cursor.execute(sql)
                resultados = cursor.fetchall()

                # Se não houver resultados, retorna a mensagem
                if not resultados:
                    return "Nenhum resultado relevante foi encontrado."

                # Obtém os nomes dos campos
                nomes_campos = [i[0].upper() for i in cursor.description]

            # Verifica se resultados é string (mensagem de erro)
            if isinstance(resultados, str):
                return resultados

            # Se não houver "order by" na consulta, ordena a lista de listas (com proteção)
            if "order by" not in sql.lower() and resultados:
                try:
                    # Verifica se os resultados têm pelo menos um elemento para ordenar
                    if len(resultados) > 0 and len(resultados[0]) > 0:
                        lista_dados = sorted(resultados, key=lambda x: x[0] if x and len(x) > 0 else '')
                    else:
                        lista_dados = resultados
                except (IndexError, TypeError, AttributeError):
                    lista_dados = resultados
            else:
                lista_dados = resultados

            # Filtra os resultados
            lista_filtrada = Conecta.filtrar_resultados(lista_dados, nomes_campos)

            if lista_filtrada == 'Erro':
                raise Exception("Mais de 5 colunas retornadas. Por favor, refine sua consulta.")

            # Gera a tabela HTML com os resultados filtrados
            return Conecta.gerar_tabela_html(nomes_campos, lista_filtrada)

        except Exception as e:
            return f"Erro na execução da consulta. Erro: {str(e)}. Dúvida, contate o administrador!"

    @staticmethod
    def filtrar_resultados(resultados, nomes_campos):
        # Filtra campos indesejados
        campos_indesejados = {'SLUG', 'PASSWORD', 'ARQUIVO_PROJETO'}
        indices_validos = [i for i, nome in enumerate(nomes_campos) if nome not in campos_indesejados]
        nomes_campos = [nomes_campos[i] for i in indices_validos]

        # Se houver mais de 5 colunas, retorna a mensagem
        if len(nomes_campos) > 5:
            return 'Erro'

        # Converte os resultados (tuplas) em uma lista de listas, filtrando os campos indesejados
        lista_dados = [[linha[i] for i in indices_validos] for linha in resultados]

        # Formata os objetos datetime.date/datetime para o formato brasileiro
        for linha in lista_dados:
            for i, valor in enumerate(linha):
                if isinstance(valor, datetime.date):
                    linha[i] = valor.strftime('%d/%m/%Y')
                if isinstance(valor, datetime.datetime):
                    linha[i] = valor.strftime('%d/%m/%Y %H:%M:%S')

        return lista_dados

    @staticmethod
    def gerar_tabela_html(nomes_campos, lista_dados):
        template_str = """
                        <h2 style="text-align:center;">Tabela de Resposta</h2>
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    {% for campo in nomes_campos %}
                                        <th>{{ campo }}</th>
                                    {% endfor %}
                                </tr>
                            </thead>
                            <tbody>
                                {% for item in lista_dados %}
                                    <tr>
                                        {% for valor in item %}
                                            <td>{{ valor }}</td>
                                        {% endfor %}
                                    <tr>
                                {% endfor %}
                            </tbody>
                        </table>
                        <p><b>Total de registros:</b> {{ lista_dados|length }}</p>
                        """
        template = Template(template_str)
        context = Context({
            'nomes_campos': nomes_campos,
            'lista_dados': lista_dados
        })
        return template.render(context)
