import numpy as np
import matplotlib.pyplot as plt
def DTFT(x):
	X=[]
	N=len(x)
	w=np.arange(-1*np.pi,np.pi,0.001*np.pi)
	for i in range(0,len(x)):
	    X.append(x[i]*np.exp(-1j*w*i))
	return X
t=np.arange(0,50)
x=np.cos(2*np.pi*200*t)  #you can take any other input here
f=DTFT(x) #calling DTFT function
s=sum(f)
magnitude=np.abs(s) #taking absolute values
phase=np.angle(s)
plt.subplot(1,2,1)
plt.title("Magnitude Spectrum")
plt.plot(magnitude)
plt.subplot(1,2,2)
plt.title("Phase Spectrum")
plt.plot(phase)
plt.show()
