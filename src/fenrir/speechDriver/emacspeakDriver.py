#!/usr/bin/python
# -*- coding: utf-8 -*-

# Fenrir TTY screen reader
# By Chrys, Storm Dragon, and contributers.
# generic driver

from core import debug
from subprocess import Popen, PIPE
import pexpect
import sys

class driver():
    def __init__(self):
        pass
    def initialize(self, environment):
        self._isInitialized = False    
        try:
            self.server = pexpect.spawnu('tclsh /home/chrys/Projekte/emacspeak/servers/espeak')   
        except Exception as e:
            self.env['runtime']['debug'].writeDebugOut('speechDriver:initialize:' + str(e),debug.debugLevel.ERROR)                
        self._isInitialized = True
        self.env = environment
        
    def shutdown(self):
        if self.server:
            try:
                self.server.terminate()
            except Exception as e:
                self.env['runtime']['debug'].writeDebugOut('speechDriver:shutdown:self.server.terminate():' + str(e),debug.debugLevel.WARNING)    

    def speak(self,text, queueable=True):
        if not self._isInitialized:
            return
        if not queueable: 
            self.cancel()
        self.server.sendline('tts_say ' + '\"' + text +'\"')
        self.server.sendline('d')            

    def cancel(self):
        if not self._isInitialized:
            return
        self.server.sendline('s')   

    def setCallback(self, callback):
        print('SpeechDummyDriver: setCallback')    

    def clear_buffer(self):
        if not self._isInitialized:
            return
        print('SpeechDummyDriver: clear_buffer')    

    def setVoice(self, voice):
        if not self._isInitialized:
            return
        #self.server.sendline('s')

    def setPitch(self, pitch):
        if not self._isInitialized:
            return
        #self.server.sendline('tts_set_speech_rate')

    def setRate(self, rate):
        if not self._isInitialized:
            return
        self.server.sendline('tts_set_speech_rate' + str(rate))
    def setModule(self, module):
        if not self._isInitialized:
            return 

    def setLanguage(self, language):
        if not self._isInitialized:
            return
        #self.server.sendline('s')

    def setVolume(self, volume):
        if not self._isInitialized:
            return     
        #self.server.sendline('s')
