from this import d
import sounddevice as sd
import librosa
import IPython.display as ipd
from scipy.io.wavfile import write
# import soundfile as sf
import numpy as np
from scipy import stats
duration = 5  # seconds

# fs = 48000


data, fs = librosa.load('C:/Users/Abdelouahab/Documents/M&M/sample-000000.mp3')
# data, fs = sf.read('sounds/w.wav')

sd.play(data[:], fs)

sd.wait()
ipd.Audio(data,fs)
# print(data[np.argmax(data[:, 1])])

print(data)

def SaveRecord(recording:np.ndarray,fs: int):
    write('sounds/recording.wav', fs, recording)

def spectral_properties(y: np.ndarray, fs: int) -> dict:
    spec = np.abs(np.fft.rfft(y))
    freq = np.fft.rfftfreq(len(y), d=1/fs)
    spec = np.abs(spec)
    amp = spec / spec.sum()
    mean = (freq * amp).sum()
    sd = np.sqrt(np.sum(amp * ((freq - mean) ** 2)))
    amp_cumsum = np.cumsum(amp)
    median = freq[len(amp_cumsum[amp_cumsum <= 0.5]) + 1]
    mode = freq[amp.argmax()]
    Q25 = freq[len(amp_cumsum[amp_cumsum <= 0.25]) + 1]
    Q75 = freq[len(amp_cumsum[amp_cumsum <= 0.75]) + 1]
    IQR = Q75 - Q25
    z = amp - amp.mean()
    w = amp.std()
    skew = ((z ** 3).sum() / (len(spec) - 1)) / w ** 3
    kurt = ((z ** 4).sum() / (len(spec) - 1)) / w ** 4
    result_d = {
        'mean': mean,
        'sd': sd,
        'median': median,
        'mode': mode,
        'Q25': Q25,
        'Q75': Q75,
        'IQR': IQR,
        'skew': skew,
        'kurt': kurt,
    }

    return result_d

print(spectral_properties(data,fs))
# SaveRecord(fs, myvoice)