import qdrant_client
from sentence_transformers import SentenceTransformer
from dotenv import dotenv_values

COLLECTION_NAME = "books_library"
DIMENSION = 384
QUERY_SENTENCE = "A wolf and a cow become friends"

config = dotenv_values(".env")

def retrieve(query_sentence):

    API_KEY = config["API_KEY"]
    SERVER_URL = config["SERVER_URL"]

    client = qdrant_client.QdrantClient(
        url=SERVER_URL, 
        #prefer_grpc=True,
        api_key=API_KEY,
    )

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    query_vector = model.encode(query_sentence)
    query_vector = query_vector.tolist()

    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=3,
    )

    return results

print(retrieve(QUERY_SENTENCE))