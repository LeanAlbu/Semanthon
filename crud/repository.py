
from core.database import collection



#add 1 por 1
def Database_add(log:str, timestamp: str, source_ip: str):
    collection.add(
        ids=[f"{timestamp}_{source_ip}"],
        documents = [log]
    )



#search
def Database_search(question: str):
    results = collection.query(
        query_texts=[question],
        n_results=3
    )
    return results
