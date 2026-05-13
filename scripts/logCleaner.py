import pandas as pd
import re

# Função auxiliar testável
def limpar_log(msg):
    msg_limpa = re.sub(r'[\x00-\x1F]+', ' ', str(msg))
    return re.sub(r'\s+', ' ', msg_limpa).strip()

def Criar_Vetor():
    # 1. Carregamento
    data = pd.read_json("resources/logs.jsonl", lines=True)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data = data.set_index('timestamp')

    # 2. Limpeza
    data['message'] = data['message'].apply(limpar_log)

    # 3. Agrupamento
    organizador = data.groupby([pd.Grouper(freq="5min"), 'source_ip'])
    vetor = organizador.agg(
        prompt_contexto=('message', lambda m: ' | '.join(m)),
        portas_acessadas=('target_port', lambda p: list(set(p))),
        linhas=('http_method', 'count')
    ).reset_index()

    # 4. Criação da String para o Banco Vetorial
    def vetorizador(row):
        return (
            f"Na janela de tempo começando em {row['timestamp']}, "
            f"O ip {row['source_ip']} fez {row['linhas']} requisições. "
            f"Portas alvo: {row['portas_acessadas']}. "
            f"Detalhes do log: {row['prompt_contexto']}."
        )

    vetor['texto_para_embedding'] = vetor.apply(vetorizador, axis=1)

    return vetor
