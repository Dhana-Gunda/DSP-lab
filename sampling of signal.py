import numpy as np
from matplotlib import pyplot as plt
fs1=8000
t=np.arange(0,1,0.02)
x=np.sin(2*np.pi*2*t)
plt.stem(t,x)
plt.show()

