from stator_subassembly.stator import Stator

bldc_motor = Stator()
rez1 = bldc_motor.magnetic_flux_per_pole()
print(rez1)
