# -*- coding: utf-8 -*-
import os


def GetAllFile(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        yield path
        if os.path.isdir(path):
            for file in GetAllFile(path):
                yield file

if __name__ == '__main__':
    for filename in GetAllFile(os.path.dirname(__file__)):
        filepath = os.path.dirname(filename)
        ext = os.path.splitext(filename)[-1]
        name = os.path.splitext(os.path.basename(filename))[0]
        if os.path.isfile(filename) and ext == '.ui':
            os.system('pyuic5 "{0}" -o "{1}"'.format(filename,os.path.join(filepath, "Ui_"+name+'.py')))
