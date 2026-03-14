"""
Embedding utilities.

Embeddings convert text into numeric vectors.

These vectors allow semantic similarity search.
Instead of matching keywords, we compare meaning.

Example:

"AI in medicine"
and
"machine learning for healthcare"

will produce similar embeddings.
"""

from sentence_transformers import SentenceTransformer
from .config import EMBEDDING_MODEL
import os

# model = SentenceTransformer(EMBEDDING_MODEL)

# Adding for databricks
DBFS_MODEL_PATH = "/dbfs/models/all-MiniLM-L6-v2"

try:
    # Try loading the model from DBFS
    if os.path.exists(DBFS_MODEL_PATH):
        model = SentenceTransformer(DBFS_MODEL_PATH)
    else:
        # If not saved yet, download and save it
        model = SentenceTransformer(EMBEDDING_MODEL)
        model.save(DBFS_MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    # Fallback: download directly from Hugging Face
    model = SentenceTransformer(EMBEDDING_MODEL)
    print("Model loaded from online source as fallback.")


def embed_text(text: str):
    """
    Convert text into a numeric embedding vector.
    """
    return model.encode(text)
