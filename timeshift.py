import numpy as np
import matplotlib.pyplot as pt

# Define the sequences
x1 = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5, 0, 0, 0]
y1 = np.roll(y, 3)  # Time-shifted version of y
n = len(y1)

# Function to compute the DTFT
def dtft(x, n):
    w = np.arange(-np.pi, np.pi, 0.01)
    X = np.zeros(len(w), dtype=complex)
    for k in range(len(w)):
        X[k] = sum(x[i] * np.exp(-1j * w[k] * i) for i in range(n))
    return w, X

# Compute DTFT of the time-shifted sequence
w, Y1 = dtft(y1, n)

# Plot DTFT of the time-shifted sequence
pt.figure(figsize=(8, 4))
pt.title("DTFT of x[n-3]")
pt.plot(w, np.abs(Y1))
pt.xlabel("Frequency (rad/s)")
pt.ylabel("|Y1(w)|")

# Compute DTFT of the original sequence and apply time shift in the frequency domain
w, X1 = dtft(x1, len(x1))
X1_shifted = np.exp(-1j * w * 3) * X1

# Plot DTFT of the frequency-shifted sequence
pt.figure(figsize=(8, 4))
pt.title("DTFT of e^(-jw3) * X(w)")
pt.plot(w, np.abs(X1_shifted))
pt.xlabel("Frequency (rad/s)")
pt.ylabel("|X1_shifted(w)|")

# Check if the time-shift property is verified by comparing the magnitude of the DTFTs
if np.allclose(np.abs(X1_shifted), np.abs(Y1)):
    print("Time shift verified")
else:
    print("Time shift not verified")

pt.show()

