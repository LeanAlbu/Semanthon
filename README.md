# Semanthon
### Agente RAG para Triagem Semântica de Logs

O **Semanthon** é um assistente inteligente projetado para auxiliar analistas de um *Security Operations Center* (SOC) na triagem e análise de logs de sistema. Utilizando a arquitetura RAG (*Retrieval-Augmented Generation*), o sistema processa grandes volumes de dados não estruturados, armazena-os em um banco vetorial e permite consultas em linguagem natural com alta precisão e baixíssima latência.

---

## 🚀 Funcionalidades

- **Pipeline de ETL Automatizado**: Limpeza, normalização e vetorização de logs brutos em formato JSONL.
- **Busca Semântica**: Recuperação de contexto relevante utilizando ChromaDB.
- **Inferência de Alta Performance**: Integração com a API Groq (modelo Llama 3.1 8b) para respostas rápidas e técnicas.
- **Foco em Segurança**: Prompt system-level rigoroso e temperatura zero para mitigar alucinações e garantir respostas baseadas exclusivamente em evidências.
- **Pronto para Produção**: Ambiente totalmente conteinerizado com Docker.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.11
- **LLM**: Groq (Llama 3.1 8b Instant)
- **Banco Vetorial**: ChromaDB
- **Processamento de Dados**: Pandas
- **Containerização**: Docker & Docker Compose

## 📋 Arquitetura do Sistema

1. **Ingestão**: O script lê logs do diretório `resources/`, limpa caracteres especiais e agrupa eventos em janelas temporais de 5 minutos.
2. **Vetorização**: O contexto é convertido em embeddings e armazenado no ChromaDB.
3. **Consulta (RAG)**: O analista insere uma pergunta na CLI; o sistema busca os logs mais similares no banco vetorial.
4. **Resposta**: O LLM recebe a pergunta do usuário enriquecida com o contexto recuperado e gera uma análise técnica.

## ⚙️ Configuração e Instalação

### Pré-requisitos
- Python 3.11 ou superior
- Docker e Docker Compose (opcional para execução local)
- Chave de API do [Groq](https://console.groq.com/)

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
GROQ_API_KEY=sua_chave_aqui
```

### Execução via Docker (Recomendado)
O Docker iniciará automaticamente o pipeline de ingestão caso o banco vetorial esteja vazio.
```bash
docker-compose up --build
```

### Execução Local
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Realize a ingestão inicial dos dados:
   ```bash
   python -m scripts.ingestion
   ```
3. Inicie o assistente:
   ```bash
   python main.py
   ```

## 📂 Estrutura do Projeto

```text
├── core/             # Lógica central (LLM, Configuração do DB)
├── crud/             # Operações de persistência e busca
├── resources/        # Logs e dados brutos
├── scripts/          # Scripts de ETL e ingestão
├── banco_vetorial/   # Persistência do ChromaDB (gerado automaticamente)
├── main.py           # Ponto de entrada da CLI
└── start.sh          # Script de inicialização da infraestrutura
```

---
*Este projeto foi desenvolvido com foco em eficiência operacional e precisão técnica para ambientes de cibersegurança.*
