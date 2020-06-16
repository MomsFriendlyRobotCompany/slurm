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
import pathlib         # recursive file finding
from math import ceil  # file size
from colorama import Fore


def run(cmd):
    """Runs a command string and returns the output"""
    cmds = cmd.split()
    return check_output(cmds).strip().decode("utf-8")


def mkdir(path):
    """Makes a directory"""
    try:
        os.mkdir(path)
    except FileExistsError:
        # folder was already created ... it's ok
        pass


def rmdir(path):
    """Removes (deletes) a directory"""
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        # folder was already deleted or doesn't exist ... it's ok
        pass

def rm(fname):
    """Removes (deletes) a file or list of files"""
    if fname is None:
        # print(f"{Fore.RED}*** No file to remove ***{Fore.RESET}")
        return
    if not isinstance(fname, list):
        fname = [fname]
    for f in fname:
        try:
            os.remove(f)
            # print(f"{Fore.RED}- {f}{Fore.RESET}")
        except FileNotFoundError:
            # folder was already deleted or doesn't exist ... it's ok
            pass


def find(path, fname):
    """Given a path, this will recursively search for a file (bob.txt) or
    pattern (*.txt). It returns an array of found file paths."""
    fn = []
    for p in pathlib.Path(path).rglob(fname):
        fn.append(p)
    return fn


def touch(file):
    """Given a file name, operates like the Unix touch command"""
    pathlib.Path(file).touch()


def file_size(s):
    """Given a file size in bytes, this returns a printable size

    Returns: (size, prefix) - > (12.345, 'GB')
    """
    s = ceil(s/8)
    mem = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    for x in range(1, 6):
        if s > 1000:
            s = ceil(s / 1024)
            size = mem[x]
    return s, size
