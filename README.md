# Semanthon
### Agente RAG para Triagem Semântica de Logs e Inteligência de Ameaças

O **Semanthon** é um assistente inteligente projetado para auxiliar analistas de um *Security Operations Center* (SOC) na triagem e análise de logs de rede e sistema. Utilizando a arquitetura RAG (*Retrieval-Augmented Generation*), o sistema processa grandes volumes de dados não estruturados, armazena-os em um banco de dados vetorial local e permite consultas em linguagem natural com alta precisão e baixíssima latência.

---

## Funcionalidades Principais

- **Pipeline de ETL Automatizado**: Higienização, normalização e vetorização de logs brutos (formato JSONL) agregados por janelas temporais para otimização de contexto.
- **Busca Semântica**: Recuperação de dados estruturados e não estruturados utilizando ChromaDB como motor vetorial persistente.
- **Inferência de Alta Performance**: Integração com o modelo Llama-3.1-8b via API da Groq para respostas rápidas e estritamente técnicas.
- **Engenharia de Prompt Segura**: Diretrizes de sistema rigorosas e temperatura zero configuradas para mitigar alucinações, garantindo respostas baseadas exclusivamente nas evidências contidas nos logs.
- **Infraestrutura Resiliente**: Ambiente totalmente conteinerizado, incluindo rotinas de *cold-start* para ingestão automática de dados sem intervenção manual.

## Stack Tecnológico

- **Linguagem**: Python 3.11
- **Inteligência Artificial**: Groq API (Llama-3.1-8b-Instant)
- **Banco de Dados Vetorial**: ChromaDB
- **Engenharia de Dados**: Pandas
- **Infraestrutura e DevOps**: Docker e Docker Compose

## Arquitetura do Sistema

1. **Ingestão (ETL)**: O script processa os logs do diretório `resources/`, limpa anomalias e agrupa eventos em janelas temporais de 5 minutos.
2. **Vetorização**: O contexto processado é convertido em *embeddings* e persistido no banco vetorial.
3. **Recuperação (Retrieval)**: O analista insere uma query na CLI; o sistema realiza uma busca semântica de alta precisão no ChromaDB.
4. **Geração (Generation)**: O LLM recebe a instrução estrita juntamente com os logs recuperados, gerando uma análise técnica, determinística e livre de viés.

## Configuração e Instalação

### Pré-requisitos
- Python 3.11 ou superior
- Docker e Docker Compose (Recomendado)
- Chave de API da [Groq](https://console.groq.com/)

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto contendo a sua credencial:
```env
GROQ_API_KEY=sua_chave_aqui
```

### Execução via Docker (Recomendado)
O ambiente Docker foi projetado para inicializar automaticamente o pipeline de ingestão caso o banco vetorial esteja vazio. Para iniciar o terminal interativo, execute:

```bash
docker compose build
docker compose run --rm soc-assistant
```

### Execução Local (Sem Docker)
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Realize a ingestão inicial dos dados:
   ```bash
   python -m scripts.ingestion
   ```
3. Inicie a interface do assistente:
   ```bash
   python main.py
   ```

## Estrutura do Projeto

```text
├── core/             # Lógica central (Motor RAG, LLM e Configuração do DB)
├── crud/             # Operações de persistência e busca vetorial
├── resources/        # Logs e dados brutos em formato JSONL
├── scripts/          # Scripts de ETL e ingestão automatizada
├── banco_vetorial/   # Persistência local do ChromaDB (gerado dinamicamente)
├── main.py           # Ponto de entrada do loop interativo da CLI
└── start.sh          # Script de entrypoint para orquestração da infraestrutura
```

---
*Este projeto foi desenvolvido com foco em eficiência operacional, reprodutibilidade de infraestrutura e precisão técnica para ambientes avançados de cibersegurança.*
