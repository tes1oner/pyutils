# -*- coding: utf-8 -*-
"""
    * author: Elias D. Peraza M. @tes1oner
    * created: 01/06/2016
    * updated: 01/06/2016
    * licence: GPL3
"""
import sqlite3
from sys import exit
class Connection(object):
    """docstring for Connections"""
    def __init__(self):
        self.connection = sqlite3.connect('track.db')
        self.connection.text_factory = str
        self.cursor = self.connection.cursor()
class QueryB:
    """QueryBuilder o constructor de Queryes"""
    def __init__(self, table, fieldsList):
        """ params: (string)table, (list, tuple)fieldsList """
        self.connection = Connection()
        self.table = table
        self.sql = ""
        self.fieldsList = fieldsList
    def where(self, rules = []):
        """ * Agrega condiciones al queryBuilder *
            params: [rules]: Lista de reglas. por defecto [ '1 = 1']
            return: El objeto QueryBuilder con las condiciones dadas
            example:
        """
        if rules == []:
            self.sql += " WHERE 1 = 1"
        else:
            self.sql += " WHERE "
            for rule in rules:
                original = rule
                rList = rule.split(' ')
#                try:
#                    rList[2] = int(rList[0])
#                except:
#                    if rList[2] == 'true' or rList[2] == 'false':
#                        rList[2] = bool(rList[0])
#                    else:
                        #rList[2] = '"'+rList[2]+'"'
                rList[2] = '"'+rList[2]+'"'
                rule = ''
                for piece in rList:
                    rule += ' '+str(piece)
                self.sql += rule
                if original != rules[-1]:
                    self.sql += ' AND '
        return self
    def select(self, fields = ''):
        """ * *
            params:
            return:
        """
        if fields == '':
            for field in self.fieldsList:
                fields += '`'+field+'`, '
            limit = len(fields)-2
            fields = fields[:limit]
        self.sql = "SELECT "+fields+" FROM `"+self.table+'`'
        return self
    def get(self):
        """ * *
            params:
            return:
        """
        self.sql += ';'
        rows = self.connection.cursor.execute(self.sql)
        result = []
        for row in rows:
            result.append(row)
        self.connection.cursor.close()
        self.connection.connection.close()
        return result
    def insert(self, values):
        """ * *
            params: (list, tuple)values: valores para insertar en la tabla dada
            return: el resultado de la sentencia SQL
        """
        self.sql = "INSERT INTO "+self.table+" "+str(self.fieldsList) + " VALUES ("
        i = 0
        for field in self.fieldsList:
            self.sql += '?'
            if i < len(self.fieldsList)-1:
                self.sql += ','
            i+=1
        self.sql += ');'
        self.connection.cursor.execute(self.sql, values)
        result = self.connection.connection.commit()
        self.connection.cursor.close()
        self.connection.connection.close()
        return result
    def update(self, fields, values, condition = '1'):
        """ * *
            params: (list)fields, (list)values [,(string)condition]
            example: queryBuilder.update(['title', 'details'], ['new title', 'new details'], 'id = 3')
            return: resultado de la sentencia SQL
        """
        self.sql = "UPDATE "+self.table + " SET "
        i = 0
        for field in fields:
            self.sql += field + ' = ?'
            if i < len(fields)-1:   self.sql += ','
            else:   self.sql += ' '
            i+=1
        self.sql += " WHERE "+condition+";"
        self.connection.cursor.execute(self.sql, values)
        result = self.connection.connection.commit()
        self.connection.cursor.close()
        self.connection.connection.close()
        return result
    def delete(self, condition):
        """ * Eliminar de la bd el registro donde se cumplan las condiciones *
            params: (str)condition: condición para la eliminación
            return:
            example: queryBuilder.delete('id = 2')
        """
        self.sql = "DELETE FROM "+self.table+" WHERE "+condition+";"
        try:
            self.connection.cursor.execute(self.sql)
            result = self.connection.connection.commit()
            self.connection.cursor.close()
            self.connection.connection.close()
            return True
        except:
            return False
