#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: dxfattr
# Created: 2011-04-27

from collections import namedtuple

DXFAttr = namedtuple('DXFAttr', 'code xtype')
DXFAttr3 = namedtuple('DXFAttr3', 'code xtype subclass')
DefSubclass = namedtuple('DefSubclass', 'name attribs')

class DXFAttributes:
    def __init__(self, *subclassdefs):
        self._subclasses = []
        self._attribs = {}
        for subclass in subclassdefs:
            self.add_subclass(subclass)
            
    def add_subclass(self, subclass):
        subclass_index = len(self._subclasses)
        self._subclasses.append(subclass)
        self._add_subclass_attribs(subclass, subclass_index)
        
    def _add_subclass_attribs(self, subclass, subclass_index):
        for name, dxfattrib in subclass.attribs.items():
            self._attribs[name] = DXFAttr3(dxfattrib.code, dxfattrib.xtype, subclass_index)

    def __getitem__(self, name):
        return self._attribs[name]

    def __contains__(self, name):
        return name in self._attribs

    def keys(self):
        return self._attribs.keys()
    
    def subclasses(self):
        return iter(self._subclasses)
    