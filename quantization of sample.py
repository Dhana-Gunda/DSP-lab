import numpy as np
import matplotlib.pyplot as plt
import struct
A = 1.0  
f = 1.0 
Fs = 20 
T = 2    
q_l = 16

t = np.linspace(0, T, 1000, endpoint=False)
y = A * np.sin(2 * np.pi * f * t)
t_s = np.linspace(0, T, int(Fs * T), endpoint=False)
n = []
tn=[]
for i in range(len(t_s) // 5):  
    n.append(t_s[5*i])

t_red=t_s[::5]

y_s= A * np.sin(2 * np.pi * f * t_s)
y_sn = (y_s - y_s.min()) / (y_s.max() - y_s.min())
y_q= np.round(y_sn * (q_l- 1)) / (q_l - 1)
y_q= y_q* (y_s.max() - y_s.min()) + y_s.min()

fi=open("binaryfile.bin","wb+")
fi.write(y_s.tobytes())


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))
ax1.plot(t, y, label='Continuous Signal')
ax1.set_title('Continuous Sine Wave')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
ax1.legend()
ax1.grid(True)


ax2.stem(t_s, y_s, linefmt='b', markerfmt='g*', basefmt='r', label='Sampled Signal')
ax2.set_title('Sampled Sine Wave')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Amplitude')
ax2.legend()
ax2.grid(True)


ax3.plot(t, y, label='Continuous Signal')
ax3.step(t_s, y_q, where='mid',label='Quantized Signal')
ax3.set_title('Quantized Sine Wave')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Amplitude')
ax3.legend()
ax3.grid(True)

# ax4.stem(t_red, n, linefmt='b', markerfmt='g*', basefmt='r', label='Sampled Signal')
# ax4.set_title('Resampled Sine Wave')
# ax4.set_xlabel('Time (s)')
# ax4.set_ylabel('Amplitude')
# ax4.legend()
# ax4.grid(True)

plt.tight_layout()
plt.show()
