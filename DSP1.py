import numpy as np
import matplotlib.pyplot as plt
t0=np.arange(0,0.5,0.01)
t=0.5
f=200
x1=np.sin(2*np.pi*f*t0)
fs1=500
Ts=(1/fs1)
N=int(t*fs1)
n1=np.arange(N)
x2=np.sin(2*np.pi*n1*Ts)
fs2=100
down=int(fs1/fs2)
x3=x2[::down]
n2=n1[::down]
m1=np.max(x3)
m2=np.min(x3)
levels=16
step_size=((m1-m2)/(levels-1))
x4 = np.round((x3 - m2) /step_size) * step_size + m2
plt.subplot(2,2,1)
plt.plot(t0,x1)
plt.title("Original Signal")
plt.subplot(2,2,2)
plt.stem(n1,x2)
plt.title("Sampled Signal")
plt.subplot(2,2,3)
plt.stem(n2,x3)
plt.title("Resampled Signal")
plt.subplot(2,2,4)
plt.plot(n2,x4)
plt.title("Quantized Signal")
plt.show()
