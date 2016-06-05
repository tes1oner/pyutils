# -*- coding: utf-8 -*-
"""
    * author: Elias D. Peraza M. @tes1oner
    * created: 04/06/2016
    * licence: GPL3
"""
from sys import exit

from utils.write import Writer

from presenter import Presenter

from models.user_model import User
from models.user_model import User
from models.config_model import Config

w = Writer()
class UsersPresenter(Presenter):
    """ * ...UserPresenter * """
    helpText = """ ayuda para 'tareas'"""
    commandsList = """ Lista de comandos """
    def __init__(self, argq):
        super(UsersPresenter, self).__init__(self.helpText, self.commandsList)
        self.argq = argq
    def run(self):
        arg = ''
        if len(self.argq) > 0:
            arg = self.argq.popleft()
        if arg == '' or arg == 'all':
            users = User.all()
            for user in users:
                w.user(user)
        elif arg == '+' or arg == 'add':
            if len(self.argq) > 0:
                # Si se pasaron los datos de manera directa
                pass
            name = raw_input('Ingrese nombre>>> ')
            username = raw_input('Ingrese nombre de usuario>>> ')
            email = raw_input('Ingrese email>>> ')
            user = User()
            user.name = name
            user.username = username
            user.email = email
            if user.save():
                #w.success('')
                pass
            else:
                w.error("Error al guardar")
        elif arg == 'del' or arg == '-d':
            if len(self.argq) < 1:
                w.error('No eligió ningun elemento para borrar. Pruebe alguno de los siguientes comandos')
                w.warning('  track -u -d \#1', True, '\t#1 para el elemento cuyo id es 1')
                w.warning('  track -u -d @username', True, '\t@username para borrar a @username')
            else:
                arg = self.argq.popleft()
                if arg.find('#') > -1:
                    user = User.find(int(arg[1:]))
                    if user == None:
                        w.error('No existe el usuario: '+str(arg))
                        exit()
                elif arg.find('@')  > -1:
                    user = User.find(arg[1:], False)
                    if user == None:
                        w.error('No existe el usuario: '+str(arg))
                        exit()
                if user.delete():
                    w.success('@'+user.username, True, ' eliminado')

        elif arg == 'me' or arg == '-m':
            #tareas asignadas a mí
            user = User.find(Config.getUser().username, False)
            if user != None:
                w.user(user, True)
        elif arg == 'list' or arg == '-l':
            # Mostrar lista de comandos con ejemplo
            self.showCommandsList()
        elif arg == '-h' or arg == 'help':
            # Mostrar ayuda
            self.showHelp()
        else:
            if arg.find('#') > -1:
                #Si se quiere ver una tarea en especifico
                user = User.find(int(arg[1:]))
                if user != None:
                    w.user(user, True)
                    exit()
            elif arg.find('@')  > -1:
                # Las tareas de un usuario en especifico
                user = User.find(arg[1:], False)
                if user == None:
                    w.error('No existe el usuario: '+str(arg))
                    exit()
                w.user(user, True)
            else:
                print 'Parámetro desconocido. Puede probar los siguientes:'
                print '\ttracker users [-u] list [-l]\tLista de comandos'
                print '\ttracker users [-u] help [-h]\tAyuda'
                print 'Si se omite el parámetro, se listan todos los elementos'
