#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Elias Peraza @tes1oner
# licence: GPL v3
# web: https://github.com/tes1oner/pyutils

import sys
import os
import commands
from collections import deque
from presenters.tasks_presenter import TasksPresenter
from presenters.bugs_presenter import BugsPresenter
from presenters.users_presenter import UsersPresenter
from presenters.configs_presenter import ConfigsPresenter

from models.config_model import Config
unix = False
try:
    unix = {'linux': True, 'linux2': True, 'darwin': True}[sys.platform]
except KeyError:
    if sys.platform != 'win32' and sys.platform != 'cygwin':
        print 'Plataforma no soportada'
        sys.exit()
if unix:
    separator = '/'
    appPath = '/opt/pytracker'
else:
    separator = '\\'
    appPath = 'C:\\\\apps\\pytracker'
class App(object):
    """
        docstring for App
    """
    appDescription = """    \033[1m\033[3mPyTracker\033[0m
  An local simple issue tracker for software projects
     Rastreo de bugs
     Administración de tareas
     CLI Interfaz
     Software Libre. licencia: GNU GPL 3
     plataformas soportadas:
       Linux
       Windows[cygwin] (funciona con error en los mensajes unicode)
       Mac OS (no ha sido probado)
  Version: 0.3.1 pre-alpha
  Repositorio: https://gitgub.com/tes1oner/pyutils/pytracker
  Desarrollador: Elias Peraza @tes1oner """


    def __init__(self, argl):
        self.argl = argl
    def showHelp(self):
        print 'Ayuda'
    def showArgList(self):
        print 'Lista de argumentos'
    def showAppDescription(self):
        print self.appDescription
    def run(self):
        if len(self.argl) <= 1:
            self.showAppDescription()
            sys.exit()
        argq = deque(self.argl)
        callPath = argq.popleft()
        mod = argq.popleft()
        if mod == 'tasks' or mod == '-t':
            presenter = TasksPresenter(argq)
            presenter.run()
        elif mod == 'bugs' or mod == '-b':
            presenter = BugsPresenter(argq)
            presenter.run()
        elif mod == 'users' or mod == '-u':
            presenter = UsersPresenter(argq)
            presenter.run()
        elif mod == 'config' or mod == '-c':
            presenter = ConfigPresenter(argq)
            presenter.run()
        elif mod == 'help' or mod == '-h':
            self.showHelp()
        elif mod == 'list' or mod == '-l':
            self.showArgList()
        elif mod == 'start' or mod == 'init':
            self.init_track()
        else:
            print 'Parámetro desconocido. Puede probar los siguientes:'
            print '\ttracker list [-l]\tLista de comandos'
            print '\ttracker help [-h]\tAyuda'

    def init_track(self):
        if os.path.exists('track.db'):
            print "El rastreo de incidencias se ha iniciado anteriormente"
        else:
            command = 'cp '+appPath + separator + 'db'+separator+'track.sqlite track.db'
            commandResult = commands.getoutput(command)
            if(commandResult != '\n' and commandResult != ''):
                print commandResult
                sys.exit()
            user = Config.getUser()
            if user != None:
                user.save()

def main(argv):
    app = App(argv)
    app.run()


if __name__ == "__main__":
    main(sys.argv)
