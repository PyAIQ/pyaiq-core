from core import on_query


@on_query
def handle_query(data):
    print(f"Server received on_query with data: {data}")
    return {"status": "query completed"}
