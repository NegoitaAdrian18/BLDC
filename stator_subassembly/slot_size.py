from stator_subassembly.stator import Stator
from stator_subassembly.stator_tooth import Slot
import math

class SlotSize(Slot, Stator):

    so = 1e-3
    histm = 0.8
    hcon = 0.5

    def slot_width_one(self):
        """
        Calculul deschiderii crestaturii (la nivelul intrefierului)
        :return:
        """
        lcr_1 = (math.pi/self.slot)*(self.d_stator_int+2*self.histm+2*self.hcon)-self.tooth_width()
        return lcr_1

    def slot_width_two(self):
        """
        Calculul latimii crestturii la nivelul jugului stator
        :return:
        """
        lcr_2 = (math.pi*self.slot)*(self.d_stator_int+2*self.tooth_height())-self.tooth_width()
        return lcr_2

    def slot_surface(self):
        pass
    




