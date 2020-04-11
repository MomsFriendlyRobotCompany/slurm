# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2014 Kevin Walchko
# see LICENSE for full details
##############################################
from subprocess import check_output  # call command line
import os              # make directories, change current dir, etc
import platform        # macOS or windows
import shutil          # move and delete files/folders

def run(cmd):
    """Runs a command string and returns the output"""
    cmds = cmd.split()
    return check_output(cmds).decode("utf-8")


def mkdir(path):
    """Makes a directory"""
    try:
        os.mkdir(path)
    except FileExistsError:
        # folder was already created ... it's ok
        pass


def rmdir(path):
    """Removes a directory"""
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        # folder was already deleted or doesn't exist ... it's ok
        pass

def file_size(s):
    """Given a file size in bytes, this returns a printable size

    Returns: (size, prefix) - > (12.345, 'GB')
    """
    mem = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    for x in range(1, 6):
        if s > 1000:
            s = math.ceil(s / 1024)
            size = mem[x]
    return s, size
