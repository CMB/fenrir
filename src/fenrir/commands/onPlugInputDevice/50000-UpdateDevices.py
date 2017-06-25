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
        return 'No description found'         
    def run(self):
        if not self.env['runtime']['screenManager'].isSuspendingScreen(): # remove if all works
            self.env['runtime']['inputManager'].updateInputDevices() 
    def setCallback(self, callback):
        pass
