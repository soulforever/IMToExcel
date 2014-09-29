# encoding=utf-8
# !/usr/bin/env python
'''
Created on 2014��9��29��

@author: Guti
'''

import re
import shutil


def readIMInfo(IMFile, regex, div):
    "Read the IMInfo and get the dictionary that will be written."
    reInfo = re.compile(regex)
    dictInfo = {}

    with open(IMFile) as f:
        for line in f:
            if reInfo.match(line.strip()):
                li = line.strip().split(div)
                dictInfo[li[0]] = li[1:]
    return dictInfo


def splitIMInfo(IMFile, StartTime):
    "Split IM chat file by the start time when the collection began."
    reInfo = re.compile(StartTime)

    with open(IMFile) as f:
        with open(IMFile+'temp', 'a') as fw:
            fw.truncate()
            flag = False
            for line in f:
                if reInfo.match(line):
                    flag = True
                if flag:
                    fw.write(line)

    shutil.move(IMFile+'temp', IMFile)


if __name__ == '__main__':
    print help(readIMInfo)
