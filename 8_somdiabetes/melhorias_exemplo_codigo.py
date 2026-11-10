# por Bernardo Paz

import warnings
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Ignora avisos no terminal
warnings.filterwarnings("ignore")

print("Carregando o modelo de Inteligência Artificial...")
modelo = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# O seu JSON com o contexto e esquema do banco de dados
json_contexto = """
{
    "esquema_banco_dados": {
        "alimento_alimento": {
            "descricao": {"significado": "Descrição ou nome identificador do alimento cadastrado na plataforma."},
            "calorias": {"significado": "Quantidade de calorias associada ao alimento."},
            "carboidratos": {"significado": "Quantidade de carboidratos, em gramas, associada ao alimento."}
        },
        "dado_clinico_dadoclinico": {
            "cliente": {"significado": "Referência ao usuário ou paciente proprietário dos dados clínicos."},
            "tipo_diabetes": {"significado": "Tipo de diabetes identificado para o paciente."},
            "glicemia_meta": {"significado": "Valor-alvo de glicemia definido para o paciente."},
            "altura": {"significado": "Altura do paciente em centímetros."},
            "peso": {"significado": "Peso do paciente em quilogramas."}
        },
        "exercicio_exercicio": {
            "nome": {"significado": "Nome do exercício físico cadastrado na plataforma."},
            "descricao": {"significado": "Descrição detalhada das características e orientações do exercício."}
        },
        "medicamento_medicamento": {
            "nome_comercial": {"significado": "Nome comercial do medicamento."},
            "principio_ativo": {"significado": "Nome do princípio ativo do medicamento."},
            "classe_terapeutica": {"significado": "Classe terapêutica à qual o medicamento pertence."}
        },
        "registro_atividade_registroatividade": {
            "duracao": {"significado": "Duração da atividade física em minutos."},
            "esforco": {"significado": "Nível de esforço percebido durante a atividade."},
            "frequencia_cardiaca_media": {"significado": "Frequência cardíaca média durante a atividade física."},
            "total_calorias": {"significado": "Total de calorias gastas durante a atividade física."}
        },
        "registro_refeicao_registrorefeicao": {
            "registro_alimentacao": {"significado": "Descrição textual detalhada dos alimentos consumidos pelo paciente na refeição. Pode conter nomes de pratos, ingredientes."},
            "glicemia_vigente": {"significado": "Valor de glicemia medido antes da refeição."},
            "quantidade_insulina_recomendada": {"significado": "Quantidade de insulina recomendada após a análise da alimentação."}
        },
        "relatorio_relatorio": {
            "titulo": {"significado": "Título identificador do relatório."},
            "script_sql": {"significado": "Campo que armazena o script SQL associado ao relatório."}
        },
        "usuario_usuario": {
            "tipo": {"significado": "Categoria do usuário na plataforma: cliente, médico, nutricionista ou educador físico."},
            "nome": {"significado": "Nome completo do usuário, paciente ou profissional."},
            "cpf": {"significado": "CPF do usuário."}
        }
    }
}
"""

# Carrega o JSON
dados = json.loads(json_contexto)
esquema = dados["esquema_banco_dados"]

tabelas = {}

# Monta o contexto de cada tabela juntando os significados das colunas
for nome_tabela, colunas in esquema.items():
    contexto_tabela = f"Tabela {nome_tabela}. "
    for nome_coluna, detalhes in colunas.items():
        if "significado" in detalhes:
            contexto_tabela += f"{detalhes['significado']} "
    tabelas[nome_tabela] = contexto_tabela.strip()

nomes_tabelas = list(tabelas.keys())
descricoes = list(tabelas.values())

# Transforma as descrições ricas em vetores matemáticos
vetores_tabelas = modelo.encode(descricoes)

print("="*50)
print(" SISTEMA PRONTO! TESTE DE CONTEXTO COM JSON ")
print(" Digite 'sair' para encerrar o programa.")
print("="*50)

while True:
    pergunta = input("\nDigite uma frase (ex: 'qual a minha meta de glicemia?' ou 'corri por 30 minutos'): ")
    
    if pergunta.lower().strip() == 'sair':
        print("Encerrando o teste...")
        break
        
    if not pergunta.strip():
        continue

    vetor_pergunta = modelo.encode([pergunta])
    similaridades = cosine_similarity(vetor_pergunta, vetores_tabelas)[0]
    
    indice_maior = np.argmax(similaridades)
    tabela_vencedora = nomes_tabelas[indice_maior]
    confianca = similaridades[indice_maior] * 100
    
    print("-" * 50)
    print(f"🤖 Entendi, Bernardo! Com base no esquema do banco, o contexto é:")
    print(f"✅ Tabela: {tabela_vencedora}")
    print(f"📊 Nível de confiança: {confianca:.1f}%")
    print("-" * 50)
