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
    def load(self):
        print('--------------')
        print('agetty')    
        print('load new',self.env['screen']['newApplication'])        
        print('--------------')
        
    def unload(self):
        print('--------------')
        print('agetty')    
        print('unload old',self.env['screen']['oldApplication'])    
        print('--------------')
          
    def setCallback(self, callback):
        pass
