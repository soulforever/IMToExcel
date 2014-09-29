# encoding=utf-8
# !/usr/bin/env python
'''
Created on 2014��9��29��

@author: Guti
'''


import excel
import IMinfo
import ConfigParser


def readConfig(configName, configFile='../etc/config'):
    conf = ConfigParser.ConfigParser()
    conf.read(configFile)
    confDict = dict(conf.items(configName))
    return confDict


def getNameList():
    exconf = readConfig('EXCEL')
    ex = excel(exconf['ExcelFile'])

    liName = []
    row = exconf['NameRow ']
    col = exconf['NameCol']

    while True:
        cell = ex. 
        

def write():
    exconf = readConfig('EXCEL')
    imconf = readConfig('IM')
    ex = excel(exconf['ExcelFile'])
    IMinfo.splitIMInfo(imconf['IMFile'], imconf['StartTime'])
    IMinfo.readIMInfo(imconf['IMFile'], imconf['Regex'], imconf['DividSymbol'])

    





if __name__ == '__main__':
    readConfig()