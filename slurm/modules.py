# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2020 Kevin Walchko
# see LICENSE for full details
##############################################
from types import ModuleType as MT

def importedModules():
    """
    Determines the version of imported modules if it can. Unfortunately
    some authors do strange things that makes this simple process more
    difficult.
    """
    s = set()
    libs = {}
    for k,v in globals().items():
        if type(v) is MT and not k.startswith('__'):
            n = v.__package__
            if n is None:
                n = v.__name__
            n = n.split('.')[0]
            
            if n in ["spatialmath","roboticstoolbox"]:
                n += "-python"

            if n != '':
                s.add(n)

    for n in s:
        try:
            libs[n] = version(n)
        except:
            libs[n] = "unknown"
            
    return libs
