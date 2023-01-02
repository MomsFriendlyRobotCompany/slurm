# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2020 Kevin Walchko
# see LICENSE for full details
##############################################
from slurm import network, storage
# from slurm.files import mkdir, rmdir, run, rm, touch, file_size
# from slurm import SimpleProcess
# from slurm import Rate
from slurm import scistorage
from slurm import *
from slurm.files import *
import os
from math import pi
import time
from collections import namedtuple
import random


# Rate =====================================================================

def test_rate():
    rate = Rate(10)
    a = time.time()

    for i in range(10):
        rate.sleep()

    b = time.time()

    assert (b-a) < 1.1

# Network ==================================================================

def test_ip():
    ip = network.get_ip()
    print(f"ip: {ip}")
    assert ip, f"Invalid IP found:{ip}"

# Storages ==================================================================

def file_func(fname):
    # _, ext = fname.split(".")

    data = {'a': 1, 'bob': [1, 2, 3, 4], 'c': "hello cowboy", 'd': {'a': pi}}

    storage.write(fname, data)
    d = storage.read(fname)
    assert d == data, f"{d} != {data}"

    fname = os.path.expanduser(fname)
    os.remove(fname)


def test_json():
    file_func('test.json')


def test_yaml():
    file_func('test.yml')


def test_yaml():
    file_func('test.pickle')

# doesn't work github!
# def test_user_home():
#     file_func('~/github/slurm/tests/test2.pickle')

# SciStorage ===============================================================

def test_sci():
    T = namedtuple("T","a")
    data = [random.uniform(-10,10) for _ in range(10)]

    fname = "test.pkl"
    info  = {"name":"test"}

    scistorage.write(info, data, fname)
    d = scistorage.read(fname)
    assert d["data"] == data, f"Uncompressed: {d} != {data}"
    assert d["info"] == info

    fname = os.path.expanduser(fname)
    os.remove(fname)

    fname += ".gz"

    scistorage.write(info, data, fname)
    d = scistorage.read(fname)
    assert d["data"] == data, f"Compressed: {d} != {data}"
    assert d["info"] == info

    fname = os.path.expanduser(fname)
    os.remove(fname)

# Process ==================================================================

def func():
    for _ in range(10):
        print(".", end="")
        time.sleep(0.01)
    print("")

def test_process():
    p = SimpleProcess()
    p.start(func)
    print(p)
    p.join()

    assert True

def func2(a,b,c):
    # for _ in range(10):
    #     print(".", end="")
    #     time.sleep(0.1)
    # print("")
    assert a == 10
    assert b == 20
    assert c == 30

def test_process_args():
    p = SimpleProcess()
    p.start(func2, args=(10,20,30,))
    print(p)
    p.join()

    assert True

# Files ====================================================================

def test_files():
    dir = "tmp_dir"

    try:
        mkdir(dir)
        os.chdir(dir)
        touch("kevin.test")
        ls = os.listdir()
        r = run("ls").split("\n")
        assert ls == r, f"slurm.files.run failed: {ls} != {r}"
        os.chdir("..")
        rmdir(dir)

        assert True
    except Exception as e:
        assert False, f"slurm.files failed: {e}"

def test_size():
    for f, ans in zip([1024*8, 1024**2*8, 1024**3*8], ["KB", "MB", "GB"]):
        a,b = file_size(f)
        # print(a,b)
        assert a == 1, f"{a} -> 1"
        assert b == ans, f"{b} -> {ans}"
