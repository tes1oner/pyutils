# -*- coding: utf-8 -*-
"""
    * author: Elias D. Peraza M. @tes1oner
    * created: 04/06/2016
    * licence: GPL3
"""
from user_model import User
class Config(object):
    """ * Config * """
    def __init__(self, arg):
        super(Config, self).__init__()
        self.arg = arg
    @classmethod
    def getUser(self):
        user = User()
        user.username = 'your-username'
        user.email = 'your@email.com'
        user.name = "Your Name"
        return user
