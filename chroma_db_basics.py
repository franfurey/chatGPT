# export HNSWLIB_NO_NATIVE = 1
import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name = 'my_collection')

collection.add(
    document = ['My name is Francisco Furey','Soy Argentino y campeon del mundo'],
    metadatas= [{'source':'Francisco'},{'source':'Campeon'}],
    ids = ['1','2'],
)

results = collection.query(
    query_texts= ['What is my name?'],
    n_results=1
)

print(results)