
import numpy as np
import matplotlib.pyplot as plt


n = np.arange(-5, 6)
x1 = np.sin(n)
x2 = 2 * np.cos(n)


X1 = np.fft.fft(x1)
X2 = np.fft.fft(x2)


a = 2
b = 3
x = a * x1 + b * x2
X = np.fft.fft(x)


print("Linearity check:", np.allclose(X, a * X1 + b * X2))

# Plot the results

plt.subplot(1, 2, 1)
plt.plot(n, x1, label='x1[n]')
plt.plot(n, x2, label='x2[n]')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(X)
plt.plot(a * X1 + b * X2)
plt.legend()
plt.show()



