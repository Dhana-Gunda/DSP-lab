import numpy as np
from matplotlib import pyplot as plt
sampling_frequency=8000
f=200
duration=0.5
t=np.linspace(0,duration,int(sampling_frequency*duration))
x=np.sin(2*np.pi*f*t)
t1=np.arange(0,int(duration*sampling_frequency),2)
y=x[t1]
levels=10
quantization_step=2/levels
quantization_signal=np.round(y/quantization_step)*quantization_step
plt.stem(t1,y,label='analog signal')
plt.step(t1,quantization_signal,where='mid',label='quantized signal',color='red')
plt.title("sinwave")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid("True")
plt.show()
