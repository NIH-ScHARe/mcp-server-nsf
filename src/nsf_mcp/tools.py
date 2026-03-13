"""
MCP tools exposed to AI clients.

Tools are the core of the MCP server.

Each function decorated with @mcp.tool becomes
callable by AI models.

Example AI call:

"Find NSF awards related to climate AI"

The AI client can call:

search_awards_tool("climate ai")
"""

from fastmcp import FastMCP
from .api import search_awards
from .models import Award
from .search import semantic_search

mcp = FastMCP("NSF Research Explorer")


@mcp.tool()
def search_awards_tool(keyword: str):
    """
    Basic NSF keyword search.

    This tool performs a simple keyword search
    using the NSF API.

    Example
    -------

    search_awards_tool("machine learning")

    Returns
    -------
    List of award titles and institutions.
    """

    raw = search_awards(keyword)

    awards = [Award.from_api(x) for x in raw]

    return [
        {
            "title": a.title,
            "institution": a.institution,
            "funding": a.funding,
        }
        for a in awards
    ]


@mcp.tool()
def semantic_award_search(query: str):
    """
    Semantic search for NSF awards.

    Unlike keyword search, semantic search finds
    research that is conceptually related.

    Example
    -------

    Query:
        "AI for hospitals"

    Could return research about:

        "machine learning in healthcare"
        "predictive models for patient data"

    because embeddings capture meaning.
    """

    raw = search_awards(query)

    awards = [Award.from_api(x) for x in raw]

    ranked = semantic_search(query, awards)

    return [a.title for a in ranked[:5]]


@mcp.tool()
def analyze_institutions(keyword: str):
    """
    Analyze which institutions receive NSF funding
    for a given research area.

    This tool is useful for research analytics.

    Example
    -------

    analyze_institutions("machine learning")

    Returns
    -------

    A dictionary mapping institutions to
    total funding amounts.
    """

    raw = search_awards(keyword, 20)

    awards = [Award.from_api(x) for x in raw]

    totals = {}

    for a in awards:

        totals.setdefault(a.institution, 0)

        totals[a.institution] += a.funding

    return totals
