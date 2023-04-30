import qdrant_client
from sentence_transformers import SentenceTransformer
from dotenv import dotenv_values

COLLECTION_NAME = "books_library"  #Name of the collection on the server
DIMENSION = 384  #Dimension of the vectors of the transformer
QUERY_SENTENCE = "What is thy name son"  #Sanity Check Sentence for testing

def retrieve(query_sentence):

    config = dotenv_values(".env")

    SERVER_URL = config["SERVER_URL"]
    API_KEY = config["API_KEY"]

    client = qdrant_client.QdrantClient(
        url=SERVER_URL, 
        api_key=API_KEY,
    )  #Connect to the server using secret keys

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')   #Load the transformer model
    query_vector = model.encode(query_sentence)  #Encode the query sentence
    query_vector = query_vector.tolist()  #Convert the query vector to a list

    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=3,
    )  #Search the collection for the query vector

    titles = {results[i].payload["book_title"].replace("-", " ").title(): results[i].score for i in range(len(results))}   #make a dictionary of titles and scores

    return list(set([title + " with a match of " + str(round(titles[title]*100)) + "%" for title in titles]))  #return the titles with their scores

if __name__ == "__main__":
    titles = retrieve(QUERY_SENTENCE)  #Sanity Check
    print(titles)  #Sanity Check