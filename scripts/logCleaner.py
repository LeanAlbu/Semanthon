import pandas as pd
import re

data = pd.read_json("resources/logs.jsonl", lines=True)

data['timestamp'] = pd.to_datetime(data['timestamp'])
data = data.set_index('timestamp')

#Limpar tudo que não for alfanumérico
def clean_data(msg):
    msg_limpa = re.sub(r'[\x00-\x1F]+', ' ', str(msg))
    return re.sub(r'\s+', ' ',  msg_limpa).strip()

#Criar função que agrupe os logs em blocos de tempo (5 min) e por IP
organizador = data.groupby([pd.Grouper(freq="5min"), 'source_ip'])

vetor = organizador.agg(
    prompt_contexto =('message', lambda m: ' | '.join(m)),
    portas_acessadas=('target_ports', lambda p: list(set(p))),
    linhas=('http_method', 'count')
).reset_index()


