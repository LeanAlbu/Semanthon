#!/bin/bash

set -e

echo "Verificando integridade da infraestrutura..."

if [ ! -d "banco_vetorial" ] || [ -z "$(ls -A banco_vetorial 2>/dev/null)" ]; then
    echo " Banco vetorial não encontrado ou vazio. Iniciando pipeline de ETL e Ingestão..."
    python -m scripts.ingestion
    echo "Ingestão concluída com sucesso."
else
    echo "Banco vetorial detectado. Pulando etapa de ingestão."
fi

echo "Iniciando o Terminal SOC..."

exec "$@"
