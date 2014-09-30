# encoding=utf-8
# !/usr/bin/env python
'''
Created on 2014��9��30��

@author: Guti

contol.py  --module for config and startup
'''


import os
import shutil
import ConfigParser


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


def readConfig(configName='IM', configFile='../etc/config'):
    'Read the config file to dictionary'
    conf = ConfigParser.ConfigParser()
    conf.read(configFile)
    confDict = dict(conf.items(configName))
    return confDict


def getInputFileTuple():
    inputPath = '../input/'
    listDir = os.listdir(inputPath)
    t = {}
    for name in listDir:
        if name.endswith('.txt'):
            t['txt'] = os.path.join(inputPath, name)
        if name.endswith('.xls') or name.endswith('.xlsx'):
            t['xls'] = os.path.join(inputPath, name)
    return t


if __name__ == '__main__':
    print __doc__
