import pyaudio
import wave
import sys

"""
NOTES AND PLANNING

Going to have to make a multitasking system so time to play an audio file doesn't affect time functions

"""


class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """Initialize audio stream"""
        self.wf = wave.open(file, 'rb')                                         # open the wave file
        self.p = pyaudio.PyAudio()                                              # initialize a pyaudio.PyAudio object
        self.stream = self.p.open(                                              # initialize audio stream
            format = self.p.get_format_from_width(self.wf.getsampwidth()),      # get the format of the wave file (width = bytes per sample)
            channels = self.wf.getnchannels(),                                  # 1 = mono, 2 = stereo, etc
            rate = self.wf.getframerate(),                                      # frequency of samples
            output = True                                                       # used for output
        )

    def play(self):
        """Play the entire audio file"""
        data = self.wf.readframes(self.chunk)                                   # read data (one chunk) from the file
        while data != b'':                                                      # loop until the end of the file
            self.stream.write(data)                                             # write data to output stream 
            data = self.wf.readframes(self.chunk)                               # read more data again
        self.wf.setpos(0)

    def close(self):
        """Graceful shutdown"""
        self.stream.close()                                                     # close the stream
        self.p.terminate()                                                      # terminate the PyAudio object
        self.wf.close()                                                         # close wave file