import matplotlib.pyplot as plt
import math

def sinc(x) :
    if x == 0: 
        return 1
    return math.sin(x)/x

def equation(Ar, L1, L2, N, R, Vrad, lam, theta, fc, frot, t) :
    # sigma is the variable that holds the result of the summation
    sigma = 0
    for n in range(N) :
        sigma += math.e**( \
            -1j * 4 * math.pi / lam * \
            ((L1+L2)/2) * \
                math.cos(theta) * \
                math.sin(2 * math.pi * frot * t + (2*math.pi*n)/N) 
        ) * sinc( \
            (math.pi*4/lam) * \
            ((L2-L1)/2) * \
            math.cos(theta) * \
            math.sin( ( (2*math.pi) * (frot * t + n/N) ) ) \
        )
       
    return Ar*math.e**(1j*(2*math.pi*fc*t - ( ( (4*math.pi)/lam) * (R+Vrad*t) )  ) ) * sigma

time = []
output = []

Ar = 1
L1 = 1
L2 = 0
N = 4
R = 0
Vrad = 1

theta = math.pi/2 #depression angle say 30deg
fc = 60*10**9 #Frequency, open question to find best frequency
lam = fc/299792458 #wavelength v=f/lambda
fs = 1 #sampling frequency
frot = 500 #frequency of drone prop rotation


for i in range(100000, 101000):
    time.append(i)
    output.append(equation(Ar, L1, L2, N, R, Vrad, lam, theta, fc, frot, fs*i))




plt.plot(time, output)
plt.show()
