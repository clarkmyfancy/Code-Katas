import unittest

from ToyMachine import ToyMachine
from Elf import Elf

class ToyMachine_Test(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_should_output_gift(self):
        tm = ToyMachine()
        gift = tm.produce_gift()
        self.assertIsNotNone(gift, "Toy Machine produced gift that was NONE")


if __name__ == '__main__':
    unittest.main()




    