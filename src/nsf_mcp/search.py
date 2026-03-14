# """
# Semantic search utilities.

# This module performs similarity comparisons between
# query embeddings and NSF award embeddings.
# """

# import numpy as np
# from .embeddings import embed_text


# def cosine_similarity(a, b):
#     """
#     Compute cosine similarity between two vectors.
#     """

#     return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# def semantic_search(query, awards):
#     """
#     Perform semantic search across a list of awards.

#     Steps
#     -----

#     1. Embed the query text
#     2. Embed each award abstract
#     3. Compute similarity scores
#     4. Return the most similar awards
#     """

#     query_vec = embed_text(query)

#     scored = []

#     for award in awards:
#         text = award.title + " " + award.abstract

#         vec = embed_text(text)

#         score = cosine_similarity(query_vec, vec)

#         scored.append((score, award))

#     scored.sort(reverse=True)

#     return [a for _, a in scored]
