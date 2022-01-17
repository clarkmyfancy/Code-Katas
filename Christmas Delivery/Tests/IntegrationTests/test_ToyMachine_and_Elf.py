import unittest

from ToyMachine import ToyMachine
from Elf import Elf

class ToyMachine_and_Elf_Test(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_should_give_gift_to_elf(self):
        tm = ToyMachine()
        elf = Elf()
        tm.give_gift_to(elf)
        self.assertIsNotNone(elf.carried_gifts, "gift was not given to elf")

if __name__ == '__main__':
    unittest.main()