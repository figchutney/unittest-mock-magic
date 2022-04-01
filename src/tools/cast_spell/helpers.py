from ...tools.helpers.general import make_client

def cast_spell(wizard: str) -> str:

    client = make_client(wizard=wizard)
    return client.spells.cast("wingardium leveosaaaa")
