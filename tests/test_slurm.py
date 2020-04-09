# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2020 Kevin Walchko
# see LICENSE for full details
##############################################
from slurm import network, storage
from slurm.simple_process import SimpleProcess
import os
from math import pi
import time


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
    os.remove(fname)


def test_json():
    file_func('test.json')


def test_yaml():
    file_func('test.yml')

# Process ==================================================================

def func():
    for _ in range(10):
        print(".", end="")
        time.sleep(0.1)
    print("")

def test_process():
    p = SimpleProcess()
    p.start(func)
    print(p)
    p.join()

    assert True
