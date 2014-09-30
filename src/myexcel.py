# encoding=utf-8
# !/usr/bin/env python
'''
Created on 2014��9��30��

@author: Guti
'''

import excel


class myexcel(excel.excel):
    '''
    My excel class to handle the collection issue.
    '''

    def __init__(self, filename, div):
        excel.excel.__init__(self, filename)
        self.__keyword = u'姓名'
        self.div = div

    def __getBound(self, sheet):
        'Get the boundary'
        maxrow = 1
        maxcol = 1

        while True:
            maxrow += 1
            colfirst = self.getCell(sheet, maxrow, 1)
            if not colfirst:
                break

        for i in range(1, maxrow):
            col = 1
            while True:
                col += 1
                cell = self.getCell(sheet, i, col)
                if not cell:
                    maxcol = max(maxcol, col)
                    break

        return (maxrow, maxcol)

    def __whereis(self, sheet, needFind):
        'Find the position of something'
        t = self.__getBound(sheet)
        for row in range(1, t[0]):
            for col in range(1, t[1]):
                if self.getCell(sheet, row, col) == needFind:
                    return (row, col)

    def __getTittle(self, sheet):
        'Get the title tuple of the the sheet by key'
        t = self.__getBound(sheet)
        for row in range(1, t[0]):
            cell = self.getCell(sheet, row, 1)
            if cell == self.__keyword:
                return [self.getCell(sheet, row, col)
                        for col in range(1, t[1])]

    def getExpress(self, sheet):
        'Get the Express of form to collect information'
        t = self.__getTittle(sheet)
        lenTitle = t.__len__()
        div = self.div

        regKeyWord = ('+', '\\', '?', '*', '$', '#', '.')
        if div in regKeyWord:
            div = '\\' + div

        return (self.div.join(t), r'^.+(%s.+){%d}$' % (div, lenTitle))

    def getNameDict(self, sheet):
        'Get the Name List from excel'
        t = self.__getBound(sheet)
        for row in range(1, t[0]):
            cell = self.getCell(sheet, row, 1)
            if cell == self.__keyword:
                return dict([(r, self.getCell(sheet, r, 1))
                             for r in range(row + 1, t[0])])

    def write(self, sheet, dictIM, start=1):
        t = self.__getBound(sheet)
        d = self.getNameDict(sheet)
        for row, name in d.items():
            if name in dictIM:
                for col in range(start, t[1]):
                    self.setCell(sheet, row, col, dictIM[name][col-start])
        self.save()

if __name__ == '__main__':
    print help(myexcel)
