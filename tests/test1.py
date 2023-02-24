from context import audio
import time
import sys

a = audio.AudioFile("snap.wav")
for i in range(1000):
    a.play()
    print(i)
    time.sleep(0.1)
a.close()