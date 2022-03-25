import tkinter as tk
import sounddevice as sd
from sqlalchemy import false
import wavio as wv
import numpy as np
import librosa
import pandas as pd
import pickle
import time
import threading

class window_tk(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        tk.Frame.grid(self,row=0,column=0,sticky="NW")
        tk.Frame.update(self)
        self.root = parent
        # self.y_pred=predict_value().predict_value()
        self.Model = pickle.load(open("finalized_model.sav", 'rb'))
        self.recording = False
        self.thread = False
        self.root.geometry("300x300")
        self.root.title("vocal prediction")
        self.root.resizable(0,0)
        # self.root.config(bg="#000042")
        self.warning=tk.Label(self.root, text="Start Recording Your Voice")#,bg="#000042")
        # self.checktime=tk.Entry(self.root, textvariable = "number_of_duration", width = 8)
        self.photo_image = tk.PhotoImage(file="mic.png")
        self.voice=tk.Button(self.root,image=self.photo_image ,command=self.recorder_State, height = 50, width = 70)
        
        self.gender=tk.Label(self.root, text="Gender :")#,bg="#000042")
        self.gender_predict=tk.Label(self.root, text="{}".format(self._predict('women.wav')))#,bg="#000042")
        self.designe()

    def designe(self):
        # designe my GUI
        self.warning.configure(foreground="red")
        self.gender.configure(foreground="green")
        self.gender_predict.configure(foreground="green")
        self.warning.place(x=20,y=20)
        self.voice.place(x=110,y=130)
        # self.checktime.place(x=120,y=90)
        self.gender.place(x=130,y=200)
        self.gender_predict.place(x=130,y=230)
        
    def recorder_State(self):
        self.recording = not self.recording
        if self.thread : 
            self.thread.start()
            return
        self.thread = threading.Thread(target=self.recorder(), args=[])
        self.thread.start()
        
    def recorder(self):
        if not self.recording:
            return
        freq = 44100
        duration = 3
        recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
        sd.wait()
        name_ = '../recorded/Snap__' + str(int(time.time()))+".wav"
        wv.write(name_, recording, freq, sampwidth=2)
        self.gender_predict.config(text="{}".format(self._predict(name_)))
        self.gender_predict.after(1000, self.recorder)


    def _predict(self,audioFilename):
        prp = self.extract_feature(audioFilename)
        Xpred = pd.DataFrame([prp])
        return self.Model.predict(Xpred)[0][1:-1]


    def extract_feature(self,_file_name, **kwargs):
        mel = kwargs.get("mel")
        _file_name.replace('\\','/')
        X, sample_rate = librosa.core.load(_file_name)
        result = np.array([])
        mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
        result = np.hstack((result, mel))
        return result

if __name__ == "__main__":
    root = tk.Tk()
    window_tk(root)
    root.mainloop()