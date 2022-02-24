import os
import librosa
import numpy as np


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

my_list = os.listdir('C:/Users/Abdelouahab/Documents/M&M/M&M/1snoke-20120412-hge')
Dataset=[]
def getaudioprop(i, wavpath, my_wav,gender):
    # print(i," - ",len(my_wav),'-',len(my_list))
    data, fs = librosa.load(wavpath+"/"+my_wav[i])
    prop= spectral_properties(data,fs)
    prop["gender"]=gender
    return prop

for i in range(len(my_list)):
    valuefound=False
    wavpath = "C:/Users/Abdelouahab/Documents/M&M/M&M/1snoke-20120412-hge/"+str(my_list[i])+"/wav"
    my_wav = os.listdir(wavpath)
    listofwav = []
    with open("C:/Users/Abdelouahab/Documents/M&M/M&M/1snoke-20120412-hge/"+str(my_list[i])+"/etc/README", 'r') as my_readme:
        valuefound=False
        for line in my_readme:
            if 'Female' in line:
                listofwav= [list(getaudioprop(j, wavpath, my_wav,"Female").values()) for j in range(len(my_wav))]
                valuefound=True
                break
            elif 'Male' in line:
                listofwav= [list(getaudioprop(j, wavpath, my_wav,"Male").values())for j in range(len(my_wav))]
                valuefound=True
                break
        if valuefound:
            Dataset.append(listofwav)
Dataset = np.array(Dataset)
print(Dataset[0],Dataset.shape)
Dataset=Dataset.reshape(-1,10)
import pandas as pd
df = pd.DataFrame(Dataset,columns =['1','2','3','4','5','6','7','8','9','10'])
df.to_csv('out.csv')