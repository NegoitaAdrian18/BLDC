from stator_subassembly.stator import Stator


class AirGap(Stator):

    def __init__(self):
        """
            Calculul diametrului mediu al intrefierului.
        """
        super().__init__()

        d_delta_med = (self.d_stator_int + self.d_stator_ext)/2
        yield d_delta_med


