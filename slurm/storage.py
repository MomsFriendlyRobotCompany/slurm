# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2014 Kevin Walchko
# see LICENSE for full details
##############################################

import yaml
import os
try:
    import simplejson as json
except ImportError:
    import json


def storage_read(fname, func):
    try:
        with open(fname, 'r') as fd:
            data = func(fd)

    except IOError:
        raise Exception(f'Could not open {fname} for reading')

    return data

def get_size(fname):
    return os.path.getsize(fname)

def storage_write(fname, func, data):
    try:
        with open(fname, 'w') as fd:
            func(data, fd)

    except IOError:
        raise Exception(f'Could not open {fname} for writing')


def write(fname, data, fmt=None):
    """
    Writes a Yaml or Json file
        filename: file name
        data: data to be written
        fmt: [optional] format (yaml or json)
    """
    if not fmt:
        (f,fmt) = fname.split(".")

    if fmt in ['yml', 'yaml']:
        storage_write(fname, yaml.safe_dump, data)
    elif fmt == "json":
        storage_write(fname, json.dump, data)
    else:
        raise Exception()

def read(fname, fmt=None):
    """
    Reads a Yaml or Json file
        fname: file name
        fmt: [optional] format (yaml or json)
        return: data
    """
    if not fmt:
        (f, fmt) = fname.split(".")

    if fmt in ['yml', 'yaml']:
        return storage_read(fname, yaml.safe_load)
    elif fmt == "json":
        return storage_read(fname, json.load)
    else:
        raise Exception()
