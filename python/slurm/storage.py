# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2014 Kevin Walchko
# see LICENSE for full details
##############################################

import yaml
import pickle
import os
try:
    import simplejson as json
except ImportError:
    import json


def get_size(fname):
    """Returns the file size"""
    return os.path.getsize(fname)

def _storage_read(fname, func, access='r'):
    fname = os.path.expanduser(fname)
    # print(fname)
    try:
        with open(fname, access) as fd:
            data = func(fd)

    except IOError:
        raise Exception(f'Could not open {fname} for reading')

    return data

def _storage_write(fname, func, data, access='w', comments=None, compress=False):
    fname = os.path.expanduser(fname)
    # print(fname)
    try:
        with open(fname, access) as fd:
            if comments:
                fd.write(comments + "\n")
            func(data, fd)

    except IOError:
        raise Exception(f'Could not open {fname} for writing')


def write(fname, data, fmt=None, comments=None):
    """
    Writes a Pickle, Yaml or Json file
        :filename: file name
        :data: data to be written
        :fmt: [optional] format (pickle, yaml or json)
    """
    if not fmt:
        fmt = fname.split(".")[-1]

    if fmt in ['yml', 'yaml']:
        _storage_write(fname, yaml.safe_dump, data, comments=comments)
    elif fmt == "json":
        _storage_write(fname, json.dump, data)
    elif fmt == "pickle":
        _storage_write(fname, pickle.dump, data, 'wb')
    elif fmt == "pickle.gz":
        _storage_write(fname, pickle.dump, data, 'wb', compress=True)
    else:
        raise Exception(f"Unknown format: {fmt}")

def read(fname, fmt=None):
    """
    Reads a Pickle, Yaml or Json file
        :fname: file name
        :fmt: [optional] format (pickle, yaml or json)
    return
        :data: dictionary of data
    """
    if not fmt:
        fmt = fname.split(".")[-1]

    if fmt in ['yml', 'yaml']:
        return _storage_read(fname, yaml.safe_load)
    elif fmt == "json":
        return _storage_read(fname, json.load)
    elif fmt == "pickle":
        return _storage_read(fname, pickle.load, 'rb')
    else:
        raise Exception()
