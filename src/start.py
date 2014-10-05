# encoding=utf-8
# !/usr/bin/env python
'''
Created on 2014��9��29��

@author: Guti
'''

import control
import myexcel
import IMinfo
import shutil
import os


def makeChoice():
    prompt = '''
Choose the manage command:
(E)dit the config
(P)rocess the data

Enter choice:
    '''
    chosen = False
    while not chosen:
        try:
            choice = raw_input(prompt).strip()[0].lower()
        except (IOError, KeyboardInterrupt):
            choice = 'q'
        print 'You picked : [%s]' % choice

        if choice not in 'ep':
            print 'Invalid option, try again.'
        else:
            chosen = True

        if choice == 'e':
            getData()
        if choice == 'p':
            processData()


def processData():
    sheet = 'sheet1'
    control.envCheck()
    control.synToSubmit('../input', '../temp')
    t = control.getInputFileTuple()
    if t['t'] and t['x']:
        DividSymbol = control.readConfig('IM', 'DividSymbol')
        Regex = control.readConfig('IM', 'Regex')
        StartTime = control.readConfig('IM', 'StartTime')
        print '''
Config list:
DividSymbol is %s
Regex is %s
StartTime is %s
        ''' % (DividSymbol, Regex, StartTime)
        confirm = raw_input('Confirm?')
        if not confirm or confirm.strip().lower() == 'y':

            IMinfo.splitIMInfo(t['t'], StartTime)
            d = IMinfo.readIMInfo(t['t'], Regex, DividSymbol)
            exc = myexcel.myexcel(t['x'], DividSymbol)
            exc.write(sheet, d)
            control.synToSubmit('../temp', '../output')
            control.clrPath('../temp/')
            control.clrPath('../input/')
    else:
        print '.xls or .txt file not found!'


def getData():
    sheet = 'sheet1'
    control.envCheck()
    control.synToSubmit('../input/', '../temp/')
    t = control.getInputFileTuple()
    if t['x']:

        div = raw_input('Input the divide symbol> ')
        control.writeConfig('IM', 'DividSymbol', div)

        exc = myexcel.myexcel(t['x'], div)
        express = exc.getExpress(sheet)
        print 'The express for statistic is: ' + express[0]

        reg = raw_input('The regular expression is: ' + express[1]
                        + '.(confirm/input new)')
        if reg:
            express[1] = reg
        control.writeConfig('IM', 'Regex', express[1])

        startTime = raw_input('Publish the express and then input\
the start time> ')
        control.writeConfig('IM', 'StartTime', startTime)

        print 'Config process is over, waiting for the submition.'
    else:
        print '.xls file not found!'

if __name__ == '__main__':
    makeChoice()
