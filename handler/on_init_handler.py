from core import on_init


@on_init
def handle_init(data):
    print(f"Server received on_init with data: {data}")
    return {"status": "init completed"}
