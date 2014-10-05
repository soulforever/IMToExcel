# encoding=utf-8
# !/usr/bin/env python
'''
Created on 2014��9��30��

@author: Guti

contol.py  --module for config and startup
'''


import os
import shutil
from ConfigParser import ConfigParser


def isCopy(srcFile, dstFile):
    '''
    Using to check if it's needed to copy a file
    :param srcFile: source full path for copying
    :param dstFile: destination full path for copying'''

    if not os.path.exists(dstFile):
        return True

    if round(os.stat(srcFile).st_mtime, 1)\
            > round(os.stat(dstFile).st_mtime, 1):
        return True

    return False


def synToSubmit(src, dst):
    '''
    Using to synchronous the Java file with removing the package part
    The function will check the making time of file
    Using recursion
    :param src: source full path for synchronous
    :param dst: destination full path for synchronous'''

    if not os.path.exists(dst):
        os.mkdir(dst)

    for elem in os.listdir(src):
        srcObj = os.path.join(src, elem)
        dstObj = os.path.join(dst, elem)

        if os.path.isdir(srcObj):
            synToSubmit(srcObj, dstObj)
        else:
            if isCopy(srcObj, dstObj):
                shutil.copy2(srcObj, dstObj)


def readConfig(section, option, Cfile='../etc/config'):
    'Read the config file to dictionary'
    conf = ConfigParser()
    conf.read(Cfile)
    return conf.get(section, option)


def writeConfig(section, option, value, Cfile='../etc/config'):
    conf = ConfigParser()
    conf.read(Cfile)
    conf.set(section, option, value)
    conf.write(open(Cfile, 'w'))


def getInputFileTuple():
    'get the input tuple of the file'
    inputPath = os.getcwd() + '/../temp/'
    listDir = os.listdir(inputPath)
    t = {}
    t.fromkeys('tx')
    for name in listDir:
        if name.endswith('.txt'):
            t['t'] = os.path.join(inputPath, name)
        if name.endswith('.xls') or name.endswith('.xlsx'):
            t['x'] = os.path.join(inputPath, name)
    return t


def envCheck():
    'Check the file system'
    dirStruct = ['input', 'output', 'temp']
    dirStruct = ['../' + d for d in dirStruct]
    for d in dirStruct:
        if not os.path.exists(d):
            os.mkdir(d)


def clrPath(rootdir):
    filelist = os.listdir(rootdir)
    for f in filelist:
        filepath = os.path.join(rootdir, f)
        if os.path.isfile(filepath) and (f.endswith('.txt')
                                         or f.endswith('.xls') or
                                         f.endswith('.xlsx')):
            os.remove(filepath)
            print filepath+" removed!"
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)
            print "dir "+filepath+" removed!"

if __name__ == '__main__':
    print __doc__
