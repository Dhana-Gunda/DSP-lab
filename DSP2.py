import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
d,s=sf.read("/home/rguktrkvaleey/Television.wav")
def upsampling(x1, a):
    if a > 1:
    
        y = np.zeros((len(x1) * a, x1.shape[1]))
        y[::a] = x1
        sf.write("aout.wav",y,s)
        print("upsampled output audio saved")
def downsampling(x1, b):
    if b > 1:
        y=x1[::b]
        sf.write("bout.wav",y,s)
        print("downsampled output audio saved")
a = int(input("Enter upsampling factor: "))
b=int(input("Enter downsampling factor"))
upsampling(d, a)
downsampling(d,b)
