import numpy as np
import matplotlib.pyplot as plt
t=2
f=200
fs=900
n=np.arange(0,t*fs)
x=np.sin((2*f*np.pi*n)/fs)
X=[]
l=len(x)
N=l
K=np.arange(0,N)
for k in range(0,N):
	y=[]
	for n in range(0,N):
		a=x[n]*(np.exp((-1j*2*np.pi*k*n/N)))
		y.append(a)
	X.append(sum(y))
#print(list(X))
magnitude=np.abs(X)
phase=np.angle(X)
plt.subplot(1,2,1)
plt.title("Magnitude Spectrum")
plt.stem(K,magnitude)
plt.subplot(1,2,2)
plt.title("Phase Spectrum")
plt.stem(K,phase)
plt.show()
