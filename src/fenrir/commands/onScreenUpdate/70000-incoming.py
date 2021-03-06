#!/bin/python
# -*- coding: utf-8 -*-

# Fenrir TTY screen reader
# By Chrys, Storm Dragon, and contributers.

from core import debug

class command():
    def __init__(self):
        pass
    def initialize(self, environment):
        self.env = environment
    def shutdown(self):
        pass
    def getDescription(self):
        return 'No Description found'      

    def run(self):
        if not self.env['runtime']['settingsManager'].getSettingAsBool('speech', 'autoReadIncoming'):
            return
        # is there something to read?
        if not self.env['runtime']['screenManager'].isDelta(ignoreSpace=True):
            return      
        # this must be a keyecho or something      
        #if len(self.env['screen']['newDelta'].strip(' \n\t')) <= 1:
        xMove = abs(self.env['screen']['newCursor']['x'] - self.env['screen']['oldCursor']['x'])
        yMove = abs(self.env['screen']['newCursor']['y'] - self.env['screen']['oldCursor']['y'])
        if (xMove >= 1) and xMove == len(self.env['screen']['newDelta']):
        # if len(self.env['screen']['newDelta'].strip(' \n\t0123456789')) <= 2:
            return          
        #if yMove == 1:
        #   if len(self.env['screen']['newDelta'].strip(' \n\t0123456789')) <= 2:
        #    return                        
        self.env['runtime']['outputManager'].presentText(self.env['screen']['newDelta'], interrupt=False, flush=False)

    def setCallback(self, callback):
        pass

