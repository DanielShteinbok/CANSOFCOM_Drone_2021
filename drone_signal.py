import math
import numpy

def sinc(x) :
    if x == 0: 
        return 1
    return math.sin(x)/x

def return_signal_array(Ar, L1, L2, N, R, Vrad, lam, theta, fc, frot, t):
    ''' (num, num, num, num, num, num, num, num, num, num, numpy.ndarray) -> numpy.ndarray

    A NOTE ABOUT INPUTS: "num" means integer or float, and there are 11 parameters in total.

    returns the amplitudes of the received signal from a monitored drone
    as in return_signal(), except this one takes and returns an ndarray
    with the complete time-series dataset to:
        a) make the STFT easier to perform in one go, since scipi already has
            a compatible funtion
        b) make computing a big set of these data a lot faster.

    t is all the intervals at which the return signal is measured, for n measurements
    t.shape = (n,).
    I.e. if the measurements are taken regularly, all the values of t
    could just be equally spaced increasing numbers.

    the returned ndarray time-series data related to the value of t at the
    corresponding index, so e.g. plotting a graph should be done using both.
    e.g. if r = what is returned, then:
    r.shape = t.shape
    r[n] = return_signal(... t[n])

    NOTE: the ellipses above are simply used to represent all the other parameters
    that must be passed, in order to improve readability.
    '''
 
    sigma = numpy.zeros(t.shape, dtype=complex)
    for n in range(N) :
        sigma += numpy.exp( \
            -1j * 4 * numpy.pi / lam * \
            ((L1+L2)/2) * \
                numpy.cos(theta) * \
                numpy.sin(2 * numpy.pi * frot * t + (2*numpy.pi*n)/N) 
        ) * numpy.sinc( \
            (numpy.pi*4/lam) * \
            ((L2-L1)/2) * \
            numpy.cos(theta) * \
            numpy.sin( ( (2*numpy.pi) * (frot * t + n/N) ) ) \
        )
       
    return Ar*numpy.exp(1j*(2*numpy.pi*fc*t - 4*numpy.pi/lam * (R + Vrad * t)) ) * sigma   

def return_noisey_signal_array(inputSignal, SNR, Ar ) :
    """ (ndarray, int, int) --> ndarray 
        SNR(signal to noise ratio) in dB
        Ar or ScaleFactor from equation
    """  
    sigma = math.sqrt(Ar**2/(10**(SNR/10)))
    return inputSignal + numpy.random.normal(0, sigma, len(inputSignal))

# SCRIPT FOR TESTING THE ABOVE

# import matplotlib.pyplot as plt

# example values to use
# Ar = 1
# L1 = 1
# L2 = 0
# N = 4
# R = 0
# Vrad = 1

# theta = numpy.pi/2 #depression angle say 30deg
# fc = 60e9 #Frequency, open question to find best frequency
# lam = 299792458/fc #wavelength wavelength = c / frequency
# fs = 1 #sampling frequency
# frot = 500 #frequency of drone prop rotation

# testing the new numpy-using function:


# time_array = numpy.arange(100)
# signal_array = return_signal_array(Ar, L1, L2, N, R, Vrad, lam, theta, fc, frot, time_array)
# noisySignal = return_noisey_signal_array(signal_array, 10, Ar)


# plt.plot(time_array, noisySignal)
# plt.show()


