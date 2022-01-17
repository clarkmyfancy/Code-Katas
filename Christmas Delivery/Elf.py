import time

from ExceptionTypes.ElfExceptions import Elf_Is_Currently_Busy

class Elf:

    carried_gifts = []
    status = ""

    def __init__(self, gift=None, status=None):
        self.carried_gifts.append(gift)
        self.status = status

    def pack_gift_onto(self, sleigh):
        try:
            if self.status == "I'm busy.":
                raise Elf_Is_Currently_Busy
            self.status = "I'm busy."
            # time.sleep(1)
            sleigh.add_gift(self.carried_gifts[0])
            del self.carried_gifts[0]
            self.status = "I'm available!"
            return self.status
        except Elf_Is_Currently_Busy as e:
            raise e


    # def notify_that_elf_is_ready_to_transport_another_gift(self):
    #     return "I'm available!"