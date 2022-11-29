import numpy as np


class Stator(object):
    k_fe = 0.95
    alfa_pol = 0.89
    B_delta_med = 0.65
    L_fe = 4e-3
    B_js = 1.55

    def __init__(self):
        """

        :param
        """
        self.d_stator_ext = float(input("Insert the exterior diameter of stator: "))
        self.d_stator_int = float(input("Insert the interior diameter of stator: "))
        self.slot = int(input("Insert numnber of slots: "))
        self.number_of_paire_poles = int(input(" Insert the number of pole paires: "))

        assert self.d_stator_int >= self.d_stator_ext, f"The interior diameter of stator can not be grater of equal " \
                                                       f"with the exterior diamter of the stator "

    def area_of_pole(self):
        """
        Calculul suprfetei ununi pol statoric
        :param L_fe:
        :return:
        """
        area_pole = (np.pi * self.d_stator_int * self.L_fe) / (2 * self.number_of_paire_poles)
        return area_pole

    def magnetic_flux_per_pole(self):
        """
        Calculul fluxului magnetic pe pol
        :param alfa_pol - factor de acoperire polara, valoarea aleasa:
        :param B_delta_med - Inductia magnetica in intrefier, valoare aleasa:
        :return:
        """
        flux_per_pole = self.alfa_pol * self.area_of_pole() * self.B_delta_med
        return flux_per_pole

    def armature_high(self):
        """
        Calculul inaltimii jugului statorului
        :return:
        """
        hjs = self.magnetic_flux_per_pole() / (2 * self.k_fe * self.L_fe * self.B_js)
        return hjs
