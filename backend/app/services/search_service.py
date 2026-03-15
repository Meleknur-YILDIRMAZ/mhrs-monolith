from app.extensions import get_es

INDEX_NAME = "hospitals"


def search_hospitals(keyword):
    es = get_es()

    if es is None:
        return []

    query = {
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": ["city", "hospital", "department", "doctor"]
            }
        }
    }

    response = es.search(index=INDEX_NAME, body=query)
    hits = response["hits"]["hits"]

    return [hit["_source"] for hit in hits]