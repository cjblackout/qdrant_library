import qdrant_client
from qdrant_client.http import models

DIMENSION = 384

# Initialize the Qdrant client
client = qdrant_client.QdrantClient(
    url="https://72392111-a4ed-486c-9334-596e82942ef4.us-east-1-0.aws.cloud.qdrant.io:6333", 
    prefer_grpc=True,
    api_key="LVWBlNWbz76iBgxzGBGqx12fgDivyhQp72l1Y3XglR_0f9TBSVGZXg",
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