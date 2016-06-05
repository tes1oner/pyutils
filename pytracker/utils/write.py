# -*- coding: utf-8 -*-
from models.user_model import User
class Writer(object):
    """docstring for Writer"""
    END_FORMAT = '\033[0m'
    #colores
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    #Formatos
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESALT = '\033[7m'
    TACH = '\033[9m'
    def __init__(self):
        pass
    def tached(self, text):
        print self.TACH + self.GREEN + text + self.END_FORMAT

    def info(self, text):
        print text
    def error(self, text, bold = False, sub = ''):
        line = ''
        if bold:
            line += self.BOLD
        line += self.RED + text + self.END_FORMAT+sub
        print line
    def warning(self, text, bold = False,sub = ''):
        line = ''
        if bold:
            line += self.BOLD
        line += self.YELLOW + text + self.END_FORMAT+sub
        print line
    def success(self, text, bold = False,sub = ''):
        line = ''
        if bold:
            line += self.BOLD
        line += self.GREEN + text + self.END_FORMAT+sub
        print line

    def auto(self, text, status):
        cat = ''
        if status == 0:
            cat = self.RED
        elif status == 1:
            cat = self.YELLOW
        elif status == 2:
            cat = self.TACH+self.GREEN
        print cat+text+self.END_FORMAT
    #def item(self, item):
    #    print item
    def task(self, task, full = False):
        line = '  '
        username = str(User.find(task.assignedUser).username)
        if task.status == 0:
            line += self.RED+''
            color = self.RED
        elif task.status == 1:
            line += self.YELLOW+''
            color = self.YELLOW
        elif task.status == 2:
            line += self.GREEN+''
            color = self.GREEN
        line += ' #'+str(task._id) +'  '+str(task.title) +self.BOLD+'  @'+username+self.END_FORMAT
        if full:
            line += color+'\n   type: task\t   status: '+task.getStatus(True)+'\n  '
            line += str(task.details)+self.END_FORMAT+'\n'
        print line
    def bug(self, bug, full = False):
        line = '  '
        username = str(User.find(bug.assignedUser).username)
        if bug.status == 0:
            line += self.RED+''
            color = self.RED
        elif bug.status == 1:
            line += self.YELLOW+''
            color = self.YELLOW
        elif bug.status == 2:
            line += self.GREEN+''
            color = self.GREEN
        line += ' #'+str(bug._id) +'  '+str(bug.title) +self.BOLD+'  @'+username+self.END_FORMAT
        if full:
            line += color+'\n   type: bug\t   status: '+bug.getStatus(True)+'\n  '
            line += str(bug.details)+self.END_FORMAT+'\n'
        print line
    def user(self, user, full = False):
        line = self.CYAN+ '  #'+str(user._id)+'\t '+str(user.name)
        line += self.BOLD+'  @'+str(user.username)+self.END_FORMAT
        if full:
            line += self.CYAN+'\t '+str(user.email)+'\n'
            line += '    Bugs: '+str(len(user.bugs()))+'   Tasks: '+str(len(user.tasks()))
            line += '\n'+self.END_FORMAT
        print line
