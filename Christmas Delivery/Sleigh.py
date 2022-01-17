class Sleigh:

    num_presents = 0
    gifts = []

    def __init__(self):
        pass

    def num_presents(self):
        return len(self.gifts)

    def add_gift(self, gift):
        self.gifts.append(gift)
    