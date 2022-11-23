import numpy as np
import matplotlib.pyplot as plt


Fs = 2000
tstep= 1/Fs
fo = 100
N = int(10*Fs/fo)
t = np.linspace(0, (N-1)*tstep, N)

fstep = Fs/N
f = np.linspace(0, (N-1)*fstep, N)

y = 10*np.sin(2 * np.pi * fo * t)

# compute FFT

X = np.fft.fft(y)
X_magnit = np.abs(X) / N

f_plot = f[0:int(N/2+1)]
X_magnit_plot = 2 * X_magnit[0: int(N/2+1)]
X_magnit_plot[0] = X_magnit_plot[0] / 2

fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
ax1.plot(t, y, '.-')
ax2.plot(f_plot, X_magnit_plot, '.-')

ax1.set_xlabel(" time [s]")
ax2.set_xlabel(" frequency [Hz]")

ax1.set_ylabel(" Magnitude ")
ax2.set_ylabel(" Magnitude ")

ax1.grid()
ax2.grid()
plt.tight_layout()
plt.show()
