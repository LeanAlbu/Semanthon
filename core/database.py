import chromadb
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

RAIZ_DO_PROJETO = os.path.dirname(DIRETORIO_ATUAL)
DB_PATH = os.path.join(RAIZ_DO_PROJETO, "banco_vetorial")

chroma_client = chromadb.PersistentClient(path=DB_PATH)
collection = chroma_client.get_or_create_collection(name="log_collection")
