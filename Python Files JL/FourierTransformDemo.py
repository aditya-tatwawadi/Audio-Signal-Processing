#Computes a Fast Fourier Transform using Numpy - Turns Time domain signal into Frequency domain signal
#Plots the frequency spectrum using matplotlib

#Import dependencies
import numpy as np
import matplotlib.pyplot as plt

def compute():
    #Construct a time signal from sine wave:

    #Sampling Frequency (Hz):
    frequency_sample = 2000 
    #Sample time interval:
    tstep = 1 / frequency_sample 
    #Signal Frequency:
    signal_frequency = 100 

    #Number of samples:
    N = int(10 * frequency_sample/ signal_frequency) 

    #Time steps:
    t = np.linspace(0, (N-1)*tstep, N) 
    #Frequency interval:
    fstep = frequency_sample / N
    #Frequency steps:
    f = np.linspace(0,(N-1)*fstep, N) 

    #Create a chaotic wave - new one added is 2 times the original input frequency and has a magnitude of 4
    y = 1 * np.sin(2 * np.pi * signal_frequency * t) + 3 * np.sin(2 * np.pi * 2 * signal_frequency * t)

    #Perform FFT:
    X = np.fft.fft(y)
    X_mag = np.abs(X) / N

    f_plot = f[0:int(N/2+1)]
    X_mag_plot = 2 * X_mag[0:int(N/2+1)]
    X_mag_plot[0] = X_mag_plot[0] / 2

    #Plot
    fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
    ax1.plot(t, y, ".-")
    ax2.plot(f_plot, X_mag_plot, ".-")
    ax1.set_xlabel("Time (s)")
    ax2.set_xlabel("Frequency (Hz)")
    ax1.grid()
    ax2.grid()

    ax1.set_xlim(0, t[-1])
    ax2.set_xlim(0, f_plot[-1])
    plt.tight_layout()
    plt.show()
compute()