# -*- coding: utf-8 -*-
"""
    * author: Elias D. Peraza M. @tes1oner
    * created: 03/06/2016
    * licence: GPL3
"""
from sys import exit

from utils.write import Writer

from presenter import Presenter

from models.task_model import Task
from models.user_model import User
from models.config_model import Config

w = Writer()
class TasksPresenter(Presenter):
    """ * ...TaskPresenter * """
    helpText = """ ayuda para 'tareas'"""
    commandsList = """ Lista de comandos """
    def __init__(self, argq):
        super(TasksPresenter, self).__init__(self.helpText, self.commandsList)
        self.argq = argq
    def run(self):
        arg = ''
        if len(self.argq) > 0:
            arg = self.argq.popleft()
        if arg == '' or arg == 'all':
            tasks = Task.all()
            for task in tasks:
                w.task(task)
        elif arg == '+' or arg == 'add':
            if len(self.argq) > 0:
                # Si se pasaron los datos de manera directa
                pass
            title = raw_input('Ingrese título >>> ')
            details = raw_input('Ingrese detalles\n>>> ')
            task = Task()
            task.title = title
            task.details = details
            task.status = 0
            users = User.all()
            for user in users:
                print '\t'+str(user)
            assignedUser = raw_input('Ingrese ID del usuario asignado (Por defecto, su usuario)\n#')
            if assignedUser == '':
                task.assignedUser = User.find(Config.getUser().username, False)._id
            else:
                task.assignedUser = int(assignedUser)
            # Pendiente el manejo de errores de ingreso
            if task.save():
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
                task = Task.find(_id)
                if task == None:
                    w.error('No existe el elemento: '+str(arg))
                    exit()
                if task.delete():
                    w.success(' '+task.title, True, ' eliminado')

        elif arg == 'me' or arg == '-m':
            #tareas asignadas a mí
            user = User.find(Config.getUser().username, False)
            tasks = user.tasks()
            for task in tasks:
                w.task(task)
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
                task = Task.find(int(arg[1:]))
                w.task(task, True)
            elif arg.find('@')  > -1:
                # Las tareas de un usuario en especifico
                user = User.find(arg[1:], False)
                if user == None:
                    w.error('No existe el usuario: '+str(arg))
                    exit()
                tasks = user.tasks()
                if len(tasks) < 1:
                    w.success(arg+' no tiene elementos "task" asignados')
                    exit()
                for task in tasks:
                    w.task(task, True)
            else:
                print 'Parámetro desconocido. Puede probar los siguientes:'
                print '\ttracker tasks [-t] list [-l]\tLista de comandos'
                print '\ttracker tasks [-t] help [-h]\tAyuda'
                print 'Si se omite el parámetro, se listan todos los elementos'
