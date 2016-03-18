# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 21:21:55 2016

@author: Dema
"""

import pyaudio
import wave
import subprocess
import datetime
import time


CHUNK = 1024 
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 2 
RATE = 16000 #sample rate

RECORD_SECONDS = 8

now = datetime.datetime.now()
sOutputFile = format(now.year)[-2:] + ('%02d' % now.month) + ('%02d' % now.day) + "_" + ('%02d' % now.hour) + ('%02d' % now.minute) + ('%02d' % now.second)
sOutputWAV = sOutputFile + ".wav"
sOutputMP3 = sOutputFile + ".mp3"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) #buffer

print("\n\nRecording " + sOutputWAV + " for " + format(RECORD_SECONDS) + " seconds")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data) # 2 bytes(16 bits) per channel
    if i % 5 == 0:
        print(">")
        
print("*")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(sOutputWAV, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
time.sleep(3)
print ("Converting: " + sOutputMP3)
sCommand = "ffmpeg -i " + format(sOutputWAV) + " -f mp3 " + sOutputMP3
print (sCommand)
subprocess.call(sCommand)

