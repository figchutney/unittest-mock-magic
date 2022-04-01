from . import potions, spells


class Client:
    def __init__(self, wizard):
        self.wizard = wizard
    
    @property
    def spells(self) -> spells.Spell:
        return spells.Spell()

    @property
    def potions(self) -> potions.Potion:
        return potions.Potion()
