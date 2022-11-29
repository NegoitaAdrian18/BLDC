from stator_subassembly.stator import Stator
import math


class Slot(Stator):
    B_tooth = 1.7

    def __init__(self):
        super(Slot, self).__init__()
        """
        t = slot step,
        bd = width of the stator tooth,
        
        """

    def tooth_width(self):
        """
            Calculul latimii dintelui statoric
        :return:
        """
        t = (math.pi * self.d_stator_int) / self.slot
        bd = (t * self.B_delta_med) / (self.k_fe * self.B_tooth)
        return bd

    def tooth_height(self):
        """
        Calculul inaltimii dintelui statoric
        :return:
        """
        hd = (self.bothom_tooth_diameter() - self.d_stator_int) / 2
        return hd
