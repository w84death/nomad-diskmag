#
# Nomad Diskmag - MIDI
# Playing MIDI files
#
# E-zine on a 1.44 floppy tailored made on Raspberry Pi computer.
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/nomad-diskmag
#

import sys
import pygame
from pygame.locals import *

class Midi:
    midi_directory = "assets"
    freq = 44100    # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 1024   # number of samples
    volume = 0.8
    
    def __init__(self):
        pygame.mixer.init(self.freq, self.bitsize, self.channels, self.buffer)
        pygame.mixer.music.set_volume(self.volume)

    def play_track(self, track):
        file_path = "{base}/{sub}/{file}.mid".format(base=getattr(sys, '_MEIPASS', '.'), sub=self.midi_directory, file=track)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    def stop_track(self):
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()