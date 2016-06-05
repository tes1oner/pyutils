# -*- coding: utf-8 -*-
"""
    * author: Elias D. Peraza M. @tes1oner
    * created: ?/06/2016
    * licence: GPL3
"""
from sys import exit

from utils.write import Writer

from presenter import Presenter

from models.config_model import Config
from models.user_model import User

w = Writer()
class ConfigsPresenter(Presenter):
    """ * ...ConfigPresenter * """
    helpText = """ ayuda para 'tareas'"""
    commandsList = """ Lista de comandos """
    def __init__(self, argq):
        super(ConfigsPresenter, self).__init__(self.helpText, self.commandsList)
        self.argq = argq
    def run(self):
        pass
