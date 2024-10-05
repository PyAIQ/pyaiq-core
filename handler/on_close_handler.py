from core import on_close


@on_close
def handle_close(data):
    print(f"Server received on_close with data: {data}")
    return {"status": "on close completed"}
