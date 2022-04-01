from src.magic.client import Client

def make_client(wizard: str) -> Client:
    client = Client(wizard=wizard)
    print(f"ID of `Client` in `make_client` is {id(client)}")
    return client
