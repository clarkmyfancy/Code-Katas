from ToyMachine import ToyMachine
from Elf import Elf
from Sleigh import Sleigh

# link to kata
# https://codingdojo.org/kata/christmas-delivery/

def main():
    tm = ToyMachine()
    # elf =  Elf()
    elf = Elf(gift={}, status="I'm busy.")
    sleigh = Sleigh()
    elf.pack_gift_onto(sleigh)
    # tm.give_gift_to(elf)
    # sleigh = Sleigh()


if __name__ == '__main__':
    main()