from nsf_mcp.api import search_awards


def test_api_call():

    results = search_awards("machine learning", 1)

    assert len(results) > 0
