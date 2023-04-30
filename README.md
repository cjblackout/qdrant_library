# Qdrant Cloud-based Semantic Book Search
A semantic search engine for books on a toy book dataset. The dataset is preprocessed and uploaded to a Qdrant Cloud Database. The search engine uses a transformer model to encode the query and the documents into vectors and then uses the Qdrant API to search for the most similar documents. The search engine is hosted on [Render](https://qdrant-library.onrender.com).


## Installation

1. Clone the repository
2. Install requirements using `pip install -r requirements.txt`
3. Run `python app.py`
4. Access on `localhost:8080`

## Dataset

1. The Dataset is taken from [here](https://huggingface.co/datasets/bookcorpusopen)
2. The dataset is preprocessed and uploaded to a Qdrant Cloud Database. See [Docs](https://qdrant.tech/documentation/) for more details.

## Technical Details

1. Vector Dimension: 384
2. Model Used: [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
3. Payload: `dataset[title]` of the type `string`.

## Demo

1. The demo is hosted on [Render](https://qdrant-library.onrender.com). Please note: The server is free tier, hence it may take a few seconds to load.

## Credits

1. [Qdrant](https://qdrant.tech/) for providing the vector database.
2. Rishabh Saxena for development.

## Citation

---
    title : Aligning Books and Movies: Towards Story-Like Visual Explanations by Watching Movies and Reading Books
    author : Zhu, Yukun and Kiros, Ryan and Zemel, Rich and Salakhutdinov, Ruslan and Urtasun, Raquel and Torralba, Antonio and Fidler, Sanja
    booktitle : The IEEE International Conference on Computer Vision (ICCV)
    month : December
    year : 2015
---