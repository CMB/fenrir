#!/bin/python
# -*- coding: utf-8 -*-

# Fenrir TTY screen reader
# By Chrys, Storm Dragon, and contributers.

from core import debug
from utils import word_utils
from utils import char_utils

class command():
    def __init__(self):
        pass
    def initialize(self, environment):
        self.env = environment
    def shutdown(self):
        pass 
    def getDescription(self):
        return 'phonetically spells the current word and set review to it'        
    
    def run(self):
        self.env['runtime']['cursorManager'].enterReviewModeCurrTextCursor()
        self.env['screenData']['newCursorReview']['x'], self.env['screenData']['newCursorReview']['y'], nextWord = \
          word_utils.getNextWord(self.env['screenData']['newCursorReview']['x'], self.env['screenData']['newCursorReview']['y'], self.env['screenData']['newContentText'])
        
        if nextWord.isspace():
            self.env['runtime']['outputManager'].presentText("blank", interrupt=True)
        else:
            firstSequence = True
            for c in nextWord:
                currChar = char_utils.getPhonetic(c) 
                self.env['runtime']['outputManager'].presentText(currChar, interrupt=firstSequence, announceCapital=True)
                firstSequence = False
   
    def setCallback(self, callback):
        pass