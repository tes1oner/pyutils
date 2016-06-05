# -*- coding: utf-8 -*-
"""
    * author: Elias D. Peraza M. @tes1oner
    * created: 04/06/2016
    * licence: GPL3
"""
from sys import exit

from utils.write import Writer

from presenter import Presenter

from models.bug_model import Bug
from models.user_model import User
from models.config_model import Config

w = Writer()
class BugsPresenter(Presenter):
    """ * ...BugPresenter * """
    helpText = """ ayuda para 'tareas'"""
    commandsList = """ Lista de comandos """
    def __init__(self, argq):
        super(BugsPresenter, self).__init__(self.helpText, self.commandsList)
        self.argq = argq
    def run(self):
        arg = ''
        if len(self.argq) > 0:
            arg = self.argq.popleft()
        if arg == '' or arg == 'all':
            bugs = Bug.all()
            for bug in bugs:
                w.bug(bug)
        elif arg == '+' or arg == 'add':
            if len(self.argq) > 0:
                # Si se pasaron los datos de manera directa
                pass
            title = raw_input('Ingrese título >>> ')
            details = raw_input('Ingrese detalles\n>>> ')
            bug = Bug()
            bug.title = title
            bug.details = details
            bug.status = 0
            users = User.all()
            for user in users:
                #print '\t'+str(user)
                w.user(user)
            assignedUser = raw_input('Ingrese ID del usuario asignado (Por defecto, su usuario)\n#')
            if assignedUser == '':
                bug.assignedUser = User.find(Config.getUser().username, False)._id
            else:
                bug.assignedUser = assignedUser
            # Pendiente el manejo de errores de ingreso
            bug.AsignedUser = 2
            if bug.save():
                #w.success('')
                pass
            else:
                w.error("Error al guardar")
        elif arg == 'del' or arg == '-d':
            if len(self.argq) < 1:
                w.error('No eligió ningun elemento para borrar. Pruebe alguno de los siguientes comandos')
                w.warning('  track -t -d \#1', True, '\t#1 para el elemento cuyo id es 1')
            else:
                arg = self.argq.popleft()
                if arg.find('#') > -1:
                    _id = int(arg[1:])
                else:
                    _id = int(arg)
                bug = Bug.find(_id)
                if bug == None:
                    w.error('No existe el elemento: '+str(arg))
                    exit()
                if bug.delete():
                    w.success(' '+bug.title, True, ' eliminado')
        elif arg == 'me' or arg == '-m':
            #tareas asignadas a mí
            user = User.find(Config.getUser().username, False)
            bugs = user.bugs()
            for bug in bugs:
                w.bug(bug)
            pass
        elif arg == 'list' or arg == '-l':
            # Mostrar lista de comandos con ejemplo
            self.showCommandsList()
        elif arg == '-h' or arg == 'help':
            # Mostrar ayuda
            self.showHelp()
        else:
            if arg.find('#') > -1:
                #Si se quiere ver una tarea en especifico
                bug = Bug.find(int(arg[1:]))
                w.bug(bug, True)
            elif arg.find('@')  > -1:
                # Las tareas de un usuario en especifico
                user = User.find(arg[1:], False)
                if user == None:
                    w.error('No existe el usuario: '+str(arg))
                    exit()
                bugs = user.bugs()
                if len(bugs) < 1:
                    w.success(arg+' no tiene elementos "bug" asignados')
                    exit()
                for bug in bugs:
                    w.bug(bug, True)
            else:
                print 'Parámetro desconocido. Puede probar los siguientes:'
                print '\ttracker bugs [-b] list [-l]\tLista de comandos'
                print '\ttracker bugs [-b] help [-h]\tAyuda'
                print 'Si se omite el parámetro, se listan todos los elementos'
