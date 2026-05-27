from scripts import logCleaner
from crud import repository

def Database_ingestion():
    print(f"Iniciando ingestão dos logs")
    dataframe = logCleaner.Criar_Vetor()
    print(f"Encontrados:{len(dataframe)} logs...")

    for index, row in dataframe.iterrows():
        repository.Database_add(
            str(row['texto_para_embedding']),
            str(row['timestamp']),
            str(row['source_ip'])
        )

        print("Ingestão concluída")
