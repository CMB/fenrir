#!/bin/python
# -*- coding: utf-8 -*-

# Fenrir TTY screen reader
# By Chrys, Storm Dragon, and contributers.

from core import debug
from utils import char_utils

class command():
    def __init__(self):
        pass
    def initialize(self, environment):
        self.env = environment
    def shutdown(self):
        pass
    def getDescription(self):
        return ''           
    
    def run(self):
        if not self.env['runtime']['settingsManager'].getSettingAsBool('focus', 'cursor'):
            return        
        if self.env['runtime']['screenManager'].isScreenChange():
            return                 
        # detect an change on the screen, we just want to cursor arround, so no change should appear
        if self.env['runtime']['screenManager'].isDelta():
            return
        if self.env['runtime']['screenManager'].isNegativeDelta():
            return
        # is a vertical change?
        if self.env['runtime']['cursorManager'].isCursorVerticalMove():
            return                        
        # is it a horizontal change?
        if not self.env['runtime']['cursorManager'].isCursorHorizontalMove():
            return
        x, y, currChar = char_utils.getCurrentChar(self.env['screen']['newCursor']['x'], self.env['screen']['newCursor']['y'], self.env['screen']['newContentText'])
        if not currChar.isspace():
            self.env['runtime']['outputManager'].presentText(currChar, interrupt=True, ignorePunctuation=True, announceCapital=True, flush=False)
    def setCallback(self, callback):
        pass
