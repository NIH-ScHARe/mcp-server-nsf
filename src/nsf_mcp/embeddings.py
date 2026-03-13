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

model = SentenceTransformer(EMBEDDING_MODEL)


def embed_text(text: str):
    """
    Convert text into a numeric embedding vector.
    """
    return model.encode(text)
