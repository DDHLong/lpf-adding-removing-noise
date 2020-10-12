import math
import librosa
import matplotlib.pyplot as plt

signal_file = 'sound/output.wav'
signal, sr = librosa.load(signal_file)

plt.plot(signal)
plt.show()