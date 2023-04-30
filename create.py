import qdrant_client
from qdrant_client.http import models
from dotenv import dotenv_values

DIMENSION = 384

config = dotenv_values(".env")

# Initialize the Qdrant client
API_KEY = config["API_KEY"]
SERVER_URL = config["SERVER_URL"]

client = qdrant_client.QdrantClient(
    url=SERVER_URL, 
    prefer_grpc=True,
    api_key=API_KEY,
)

# Recreate the collection with the appropriate vector size and distance metric
client.recreate_collection(
    collection_name="books_library",
    vectors_config=models.VectorParams(size=DIMENSION, distance=models.Distance.COSINE),
    quantization_config=models.ScalarQuantization(
        scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8,
            quantile=0.99,
            always_ram=True,
        ),
    ),
)