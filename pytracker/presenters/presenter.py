# -*- coding: utf-8 -*-
"""
    * author: Elias D. Peraza M. @tes1oner
    * created: 03/06/2016
    * licence: GPL3
"""

from utils.write import Writer
from models.task_model import Task
from models.user_model import User
from sys import exit
w = Writer()

class Presenter(object):
    """ * docstring for Presenter * """
    def __init__(self, helpText, commandsList):
        self.helpText = helpText
        self.commandsList = commandsList
        pass
    def showHelp(self):
        print self.helpText
        exit()
    def showCommandsList(self):
        print self.commandsList
        exit()
    def run(self):
        """ docstring for run """
        pass
