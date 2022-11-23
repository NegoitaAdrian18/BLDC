import numpy as np
import matplotlib.pyplot as plt


    # Construc a time signal
Fs = 2000 # sampling freq  [numar de puncte din semnal [ din fereastra]]
tstep = 1/Fs # sample time interval  {perioada dintre puncte ori daca consider consider esantioane, dintre esantioane}
f0 = 100 # signal freq

N = int(10 * Fs/f0) # 10 cycles  of samples of the signals

t = np.linspace(0, (N-1)*tstep, N) # time steps of the time domain signal

# compute fft, there is a frequency interval for each frequency "bin"
fstep = Fs/N # freq interval

f = np.linspace(0, (N-1)*fstep, N) # freq steps

    # create a sin wave signal

y = 1*np.sin(2*np.pi*f0*t)

    # FFT

X = np.fft.fft(y)  # series of complex numbers
X_mag = np.abs(X) / N

f_plot = f[0:int(N/2+1)]
X_mag_plot =  2 * X_mag[0:int(N/2+1)]
X_mag_plot[0] =   X_mag_plot[0] / 2  # DC component does not need to multiply by 2

    # PLOT

fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
ax1.plot(t, y, '.-')
ax2.plot(f_plot, X_mag_plot, '.-')
ax1.set_xlabel(" time [s]")
ax2.set_xlabel("frequncy [Hz]")
ax1.grid()
ax2.grid()
plt.tight_layout()
plt.show()