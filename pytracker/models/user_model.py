# -*- coding: utf-8 -*-
"""
    * author: Elias D. Peraza M. @tes1oner
    * date: 03/06/2016
    * updated: 03/06/2016
    * licence: GPL3
"""
from connections import QueryB
from task_model import Task
from bug_model import Bug
class User(object):
    """ * docstring for User * """
    table = 'users'
    fields = ('id', 'name', 'email', 'username',)
    def __init__(self, _id = None, name = None, email = None, username = None):
        self.fillable = {'id': _id, 'name': name, 'email': email, 'username': username}
        self.queryB = QueryB(self.table, self.fields)
    def __str__(self):
        return "#"+str(self._id)+" @"+self.username+'   '+self.name

    def setId(self, _id):
        self.fillable['id'] = _id
    def getId(self):
        return self.fillable['id']
    _id = property(getId, setId)

    def getName(self):
        return self.fillable['name']
    def setName(self,  name):
        self.fillable['name'] = name
    name = property(getName, setName)

    def setEmail(self, email):
        self.fillable['email'] = email
    def getEmail(self):
        return self.fillable['email']
    email = property(getEmail, setEmail)

    def getUsername(self):
        return self.fillable['username']
    def setUsername(self, username):
        self.fillable['username'] = username
    username = property(getUsername, setUsername)

    def save(self):
        """ * Guardar el objeo actual en la BD, o actualizarlo si existe *
            params: None
            return: ???
            note: Aún no se ha implementado las sentencias de actualización cuando el obj ya existe
        """
        values = []
        values.append(self._id)
        values.append(self.name)
        values.append(self.email)
        values.append(self.username)
        self.queryB.insert(values)
        #Pendiente el manejo de error al guardar
        return True
    def fillFromList(self, data):
        """ * Llenar(setear) los datos del objeto a partir de una lista o tupla *
            params: (list, tuple)data: lista que contiene los datos en el orden del array fields perteneciente a este modelo
        """
        self._id = data[0]
        self.name = data[1]
        self.email = data[2]
        self.username = data[3]
    def delete(self):
        """ * Elimina el elemento de la BD *
            params:
            return: True | False
        """
        if self._id != None:
            if self.queryB.delete('id = '+str(self._id)):
                return True
        return False
    def tasks(self):
        myTasks = Task.where(['id_user = '+str(self._id)])
        return myTasks
    def bugs(self):
        myBugs = Bug.where(['id_user = '+str(self._id)])
        return myBugs
    #Metodos estaticos
    @classmethod
    def all(self):
        """ * Buscar en la BD todos los registros de este modelo *
            params: no
            return: todos los registros en la tabla perteneciente a este modelo
        """
        query = QueryB(self.table, self.fields)
        elements = query.select().where().get()
        users = []
        for element in elements:
            users.append(User.createFromList(element))
        return users
    @classmethod
    def where(self, rules = []):
        """ * Buscar en la BD los registros que coincidan con rules *
            params: [(list, tuple) rules: reglas de busqueda. Ej: ['id = 1', 'username = jvk']
            return: retorna los elementos que coinciden con la busqueda
            Por defecto el valor es una lista vacía, lo que se traducirá al SQL como WHERE 1 = 1
        """
        query = QueryB(self.table, self.fields)
        elements = query.select().where(rules).get()
        users = []
        for element in elements:
            users.append(User.createFromList(element))
        return users
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
            rule = ['username = '+str(value)]
        result = query.select().where(rule).get()
        if len(result) < 1:
            return None
        user = User()
        for row in result:
            user.fillFromList(row)
        return user
    @classmethod
    def createFromList(self, data):
        """ * Crear un objeto a partir de una lista o tupla *
            params: (list, tuple)data: lista o tupla de datos en el orden del campo fields de este modelo
            return: instancia de User
        """
        user = User(data[0], data[1], data[2], data[3])
        return user
