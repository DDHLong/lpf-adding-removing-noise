import soundfile

#convert wav file to 16-bit PCM type
data, sr = soundfile.read('input_with_noise.wav')
soundfile.write('input_with_noise2.wav', data, sr , subtype='PCM_16')