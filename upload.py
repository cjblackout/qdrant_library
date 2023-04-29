import numpy as np
import qdrant_client

from sentence_transformers import SentenceTransformer
from datasets import load_dataset
from qdrant_client.http import models
from dotenv import dotenv_values

config = dotenv_values(".env")

DIMENSION = 384
COLLECTION_NAME = "books_library"
API_KEY = config["API_KEY"]
SERVER_URL = config["SERVER_URL"]

# Load the BERT tokenizer and model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Define a function to extract sentences from the 'text' field of the bookcorpus dataset
def extract_sentences(text):
    # Split the text into sentences
    sentences = text.split('.')
    
    # Remove any leading or trailing whitespaces from each sentence
    sentences = [s.strip() for s in sentences]

    #remove all newlines
    sentences = [s.replace('\n', '') for s in sentences]

    # Remove any empty sentences
    sentences = [s for s in sentences if s]

    #only take sentences with more than 5 words
    sentences = [s for s in sentences if len(s.split()) > 5]
    
    return sentences


# Load the bookcorpus/open dataset from Hugging Face
dataset = load_dataset("bookcorpusopen", split="train")

# Initialize the Qdrant client
client = qdrant_client.QdrantClient(
    url=SERVER_URL, 
    prefer_grpc=True,
    api_key=API_KEY,
)

# Loop over each book in the dataset
for i, book in enumerate(dataset):
    print(f"Processing book {i+1} of {len(dataset)}")
    
    # Extract the author name and book title from the metadata
    book_title = book["title"].split('.')[0]
    
    # Extract sentences from the 'text' field of the book
    sentences = extract_sentences(book["text"])
    
    vectors = []
    # Encode each sentence into a 768-dimensional vector using the BERT model and upsert it into Qdrant
    for j, sentence in enumerate(sentences):
        # Encode the sentence into a vector and append it to the vectors list
        vector = model.encode(sentence)
        vector = np.reshape(vector, DIMENSION).tolist()
        vectors.append(
                    models.PointStruct(
                        id=(i+1)*(j+1),
                        payload={
                            "book_title": book_title
                        },
                        vector=vector,
                        )
                    )
        
    # Upsert the vector into Qdrant with the author name and book title as the payload
    status = client.upsert(
        collection_name=COLLECTION_NAME,
        points=vectors
    )
    print(status.status + " for book " + str(i+1) + " of " + str(len(sentences)))
