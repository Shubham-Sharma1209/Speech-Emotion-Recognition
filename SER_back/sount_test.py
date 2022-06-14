# import pyaudio
# import wave
# import pickle
# # import librosa
# # import sklearn
# # from main import *
# import soundfile,librosa,numpy
# from sklearn.neural_network import MLPClassifier
# from main import extract_feature


# chunk = 1024  
# sample_format = pyaudio.paInt16  
# channels = 1
# fs = 44100 
# seconds = 10
# filename='/home/sharmaji/Programs linux/git/Speech-Emotion-Recognition/SER_back/sound(6).wav'
# # with open('count.txt','r') as count:
# #     temp=count.read()
# #     filename = "sound("+str(int(temp)+1)+").wav"
# # count =open('count.txt','w')
# # count.write(str(int(temp)+1))
# # count.close()

# # p = pyaudio.PyAudio() 

# # print('Recording')

# # stream = p.open(format=sample_format,
# #                 channels=channels,
# #                 rate=fs,
# #                 frames_per_buffer=chunk,
# #                 input=True)

# # frames = []  

# # for i in range(0, int(fs / chunk * seconds)):
# #     data = stream.read(chunk)
# #     frames.append(data)

# # stream.stop_stream()
# # stream.close()
# # p.terminate()

# # print('Finished recording')
# # # print(len(frames),len(frames[0]))
# # wf = wave.open(filename, 'wb')
# # wf.setnchannels(channels)
# # wf.setsampwidth(p.get_sample_size(sample_format))
# # wf.setframerate(fs)
# # wf.writeframes(b''.join(frames))
# # wf.close()

# # with open('count.txt','r') as cnt:
# feature=extract_feature(filename,True,True,True,True,True)
# s_model=pickle.load('/home/sharmaji/Programs linux/git/Speech-Emotion-Recognition/SER_back/Saved_model.model')
# pred=s_model.predict(feature)
# print(pred)



import pickle  # to save model after training
import wave
from array import array
from struct import pack
from sys import byteorder

import librosa
import numpy as np
import pyaudio
import soundfile  # to read audio file
# import speech_recognition as sr


def extract_feature(file_name, **kwargs):
    """
    Extract feature from audio file `file_name`
        Features supported:
            - MFCC (mfcc)
            - Chroma (chroma)
            - MEL Spectrogram Frequency (mel)
            - Contrast (contrast)
            - Tonnetz (tonnetz)
        e.g:
        `features = extract_feature(path, mel=True, mfcc=True)`
    """

    mfcc = kwargs.get("mfcc")
    chroma = kwargs.get("chroma")
    mel = kwargs.get("mel")
    contrast = kwargs.get("contrast")
    tonnetz = kwargs.get("tonnetz")
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate
        if chroma:
            stft = np.abs(librosa.stft(X))
        result = np.array([])
        if mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result = np.hstack((result, mfccs))
        if chroma:
            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
            result = np.hstack((result, chroma))
        if mel:
            mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T, axis=0)
            result = np.hstack((result, mel))
        # if contrast:
        #     contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T, axis=0)
        #     result = np.hstack((result, contrast))
        # if tonnetz:
        #     tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T, axis=0)
        #     result = np.hstack((result, tonnetz))
    return result


THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 16000

SILENCE = 30

def is_silent(snd_data):
    return max(snd_data) < THRESHOLD


def normalize(snd_data):
    MAXIMUM = 16384
    times = float(MAXIMUM) / max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i * times))
    return r


def trim(snd_data):
    def _trim(snd_data):
        snd_started = False
        r = array('h')
        for i in snd_data:
            if not snd_started and abs(i) > THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    snd_data = _trim(snd_data)

    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    r = array('h', [0 for i in range(int(seconds * RATE))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds * RATE))])
    return r


def record(seconds=10):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
                    input=True, output=True,
                    frames_per_buffer=CHUNK_SIZE)
    num_silent = 0
    snd_started = False
    r = array('h')
    for i in range(int(RATE/CHUNK_SIZE*seconds)):
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > SILENCE:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r


def record_to_file(path):
# "Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record(10)
    data = pack('<' + ('h' * len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()


#if __name__ == "__main__":
#def int():
    # load the saved model (after training)
loaded_model = pickle.load(open("Saved_model.model", 'rb'))

print("Please talk")
filename = "sound(7).wav"
a = filename
record_to_file(filename)

features = extract_feature(filename, mfcc=True, chroma=True, mel=True).reshape(1, -1)
# predict
result = loaded_model.predict(features)[0]
# show the result !
Emotion= ("Predicted Emotion is : ", result)
print(Emotion)
# recognize (convert from speech to text)
# text = mic.recognize_google(audio_data)
# print(text)
