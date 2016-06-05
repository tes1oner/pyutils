# -*- coding: utf-8 -*-
"""
    * author: Elias D. Peraza M. @tes1oner
    * created: 04/06/2016
    * licence: GPL3
"""
from connections import QueryB
class Task(object):
    """ * docstring for Task * """
    table = 'tasks'
    fields = ('id', 'title', 'details', 'status','id_user',)
    statusAvailables = ('created', 'working','ready')
    def __init__(self, _id = None, title = None, details = None, status = None, id_user = None):
        self.fillable = {'id': _id, 'title': title, 'details': details, 'status': status, 'id_user': id_user}
        self.queryB = QueryB(self.table, self.fields)
    def __str__(self):
        return "#"+str(self._id)+" .:"+self.title+":."
    def setId(self, _id):
        self.fillable['id'] = _id
    def getId(self):
        return self.fillable['id']
    _id = property(getId, setId)
    def getTitle(self):
        return self.fillable['title']
    def setTitle(self,  title):
        self.fillable['title'] = title
    title = property(getTitle, setTitle)
    def setDetails(self, details):
        self.fillable['details'] = details
    def getDetails(self):
        return self.fillable['details']
    details = property(getDetails, setDetails)

    def getStatus(self, name = False):
        if name:
            return self.statusAvailables[self.fillable['status']]
        return self.fillable['status']
    def setStatus(self, status):
        self.fillable['status'] = status
    status = property(getStatus, setStatus)
    def getUser(self):
        return self.fillable['id_user']
    def setUser(self, id_user):
        self.fillable['id_user'] = id_user
    assignedUser = property(getUser, setUser)

    def save(self):
        """ * Guardar el objeo actual en la BD, o actualizarlo si existe *
            params: None
            return: ???
            note: Aún no se ha implementado las sentencias de actualización cuando el obj ya existe
        """
        values = []
        values.append(self._id)
        values.append(self.title)
        values.append(self.details)
        values.append(self.getStatus(False))
        values.append(self.getUser())
        self.queryB.insert(values)
        #Pendiente el manejo de error al guardar
        return True
    def fillFromList(self, data):
        """ * Llenar(setear) los datos del objeto a partir de una lista o tupla *
            params: (list, tuple)data: lista que contiene los datos en el orden del array fields perteneciente a este modelo
        """
        self._id = data[0]
        self.title = data[1]
        self.details = data[2]
        self.status = data[3]
        self.assignedUser = data[4]
    def delete(self):
        """ * Elimina el elemento de la BD *
            params:
            return: True | False
        """
        if self._id != None:
            if self.queryB.delete('id = '+str(self._id)):
                return True
        return False
    #Metodos estaticos
    @classmethod
    def all(self):
        """ * Buscar en la BD todos los registros de este modelo *
            params: no
            return: todos los registros en la tabla perteneciente a este modelo
        """
        query = QueryB(self.table, self.fields)
        elements = query.select().where().get()
        tasks = []
        for element in elements:
            tasks.append(Task.createFromList(element))
        return tasks
    @classmethod
    def where(self, rules = []):
        """ * Buscar en la BD los registros que coincidan con rules *
            params: [(list, tuple) rules: reglas de busqueda. Ej: ['id = 1', 'status = 2']
            return: retorna los elementos que coinciden con la busqueda
            Por defecto el valor es una lista vacía, lo que se traducirá al SQL como WHERE 1 = 1
        """
        query = QueryB(self.table, self.fields)
        elements = query.select().where(rules).get()
        tasks = []
        for element in elements:
            tasks.append(Task.createFromList(element))
        return tasks
    @classmethod
    def find(self, value, byId = True):
        """ * Buscar un único registro en la BD *
            params: value [, byId]
                (int)_id: id del elemento a encontrar
                (bool)byId: si la busqueda se realizará por ID o por clave candidata. por df True
            return: retorna el elemento cuyo id o clave candidata coincida con value. None si ninguna lo hizo
        """
        query = QueryB(self.table, self.fields)
        if byId:
            rule = ['id = '+str(value)]
        else:
            rule = ['title = '+str(value)]
        result = query.select().where(rule).get()
        if len(result) < 1:
            return None
        task = Task()
        for row in result:
            task.fillFromList(row)
        return task
    @classmethod
    def createFromList(self, data):
        """ * Crear un objeto a partir de una lista o tupla *
            params: (list, tuple)data: lista o tupla de datos en el orden del campo fields de este modelo
            return: instancia de Task
        """
        task = Task(data[0], data[1], data[2], data[3], data[4])
        return task
