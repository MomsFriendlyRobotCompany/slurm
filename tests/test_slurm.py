from slurm import network, storage
import os
from math import pi

# Network ==================================================================

def test_ip():
    ip = network.get_ip()

    assert ip, f"Invalid IP found:{ip}"

# Storages ==================================================================

def file_func(fname):
    _, ext = fname.split(".")

    data = {'a': 1, 'bob': [1, 2, 3, 4], 'c': "hello cowboy", 'd': {'a': pi}}

    storage.write(fname, data)
    d = storage.read(fname)
    assert d == data, f"{d} != {data}"
    os.remove(fname)


def test_json():
    file_func('test.json')


def test_yaml():
    file_func('test.yml')
