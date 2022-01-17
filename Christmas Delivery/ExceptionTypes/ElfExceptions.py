class Elf_Is_Currently_Busy(Exception):
    def __init__(self):
        self.message = "Elf is currently busy"

    def __str__(self):
        return self.message