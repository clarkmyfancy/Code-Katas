from Elf import Elf

class ToyMachine:

    gift = {}

    def __init__(self):
        pass

    def produce_gift(self):
        return self.gift

    def give_gift_to(self, elf):
        elf.carried_gifts.append(self.gift)