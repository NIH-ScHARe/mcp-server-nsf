"""
Configuration settings for the NSF MCP server.

Keeping configuration centralized makes it easier to update
API endpoints or model choices without modifying the rest
of the codebase.
"""

NSF_API_URL = "https://api.nsf.gov/services/v1/awards.json"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

DEFAULT_RESULTS = 10
