import unittest

from ExceptionTypes.ElfExceptions import Elf_Is_Currently_Busy
from Elf import Elf
from Sleigh import Sleigh

class Elf_and_Sleigh_Test(unittest.TestCase):

    def setUp(self) -> None:
        gift = {}
        self.elf = Elf(gift)
        self.sleigh = Sleigh()

    def tearDown(self) -> None:
        del self.elf
        del self.sleigh

    def test_sleigh_should_contain_more_gifts_after_being_given_one(self):
        starting_gift_count = self.sleigh.num_presents()
        self.elf.pack_gift_onto(self.sleigh)
        self.assertGreater(self.sleigh.num_presents(), starting_gift_count, "Sleigh's gift-count didn't increase after being given one")

    def test_elf_should_have_one_less_gift_after_loading_it_onto_sleigh(self):
        number_of_gifts_elf_was_carrying = len(self.elf.carried_gifts)
        self.elf.pack_gift_onto(self.sleigh)
        self.assertLess(len(self.elf.carried_gifts), number_of_gifts_elf_was_carrying, "Number of gifts elf was carrying didn't decrease after loading gift")

    def test_elf_should_notify_when_he_finishes_loading_gift(self):
        elfs_response = self.elf.pack_gift_onto(self.sleigh)
        self.assertEqual("I'm available!", elfs_response, "Elf didn't let anyone know he was finished loading gift")
        
    def test_elf_should_throw_exception_if_given_a_job_when_he_is_busy(self):
        elf = Elf(gift={}, status="I'm busy.")
        self.assertRaises(Elf_Is_Currently_Busy, elf.pack_gift_onto, self.sleigh)
    
    def test_elf_should_be_available_after_loading_gift_onto_sleign(self):
        self.elf.pack_gift_onto(self.sleigh)
        self.assertEqual("I'm available!", self.elf.status, "Elf was not available after loading gift")
        

if __name__ == '__main__':
    unittest.main()