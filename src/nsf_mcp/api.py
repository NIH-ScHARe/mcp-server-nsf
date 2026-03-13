"""
NSF API client.

This module communicates with the public NSF Awards API.

The API allows searching research grants funded by the
U.S. National Science Foundation.

Documentation:
https://api.nsf.gov
"""

import requests
from .config import NSF_API_URL


def search_awards(keyword: str, limit: int = 10):
    """
    Search NSF awards using the NSF public API.

    Parameters
    ----------
    keyword : str
        Text query such as "machine learning" or "climate change".

    limit : int
        Number of results to return.

    Returns
    -------
    list[dict]

        Raw award records from the NSF API.

        Each record contains fields such as:
        - title
        - abstractText
        - awardeeName
        - fundsObligatedAmt
        - startDate
    """

    params = {
        "keyword": keyword,
        "printFields": "title,awardeeName,fundsObligatedAmt,startDate,abstractText",
        "rpp": limit,
    }

    response = requests.get(NSF_API_URL, params=params)

    response.raise_for_status()

    data = response.json()

    return data.get("response", {}).get("award", [])
