![](https://github.com/MomsFriendlyRobotCompany/slurm/blob/master/pics/slurm.jpg?raw=true)

# Slurm


[![Actions Status](https://github.com/MomsFriendlyRobotCompany/slurm/workflows/walchko%20pytest/badge.svg)](https://github.com/MomsFriendlyRobotCompany/slurm/actions)
![GitHub](https://img.shields.io/github/license/MomsFriendlyRobotCompany/slurm)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/slurm)
![PyPI](https://img.shields.io/pypi/v/slurm)
![PyPI - Downloads](https://img.shields.io/pypi/dm/slurm?color=aqua)

This is a collection of tools I have used over the years collected together.

## Signal Catcher

`SignalCatch` catches `SIGINT` and `SIGTERM` signals and sets
`SignalCatch.kill` to `True`.

```python
from slurm import SignalCatch

sig = SignalCatch()

while True:
    if sig.kill == True:
        exit(0)
```

## Simple Processes

```python
from slurm import SimpleProcess

def func():
    # some simple process that does something
    for _ in range(10):
        print(".", end="")
        time.sleep(0.1)
    print("")

def test_process():
    p = SimpleProcess()
    p.start(func)
    print(p)
    p.join(timeout=2.0) # if not ended in 2 sec, will terminate() the process
```

## Storage

```python
from slurm import storage

pick = storage.read("file.pickle")
yaml = storage.read("file.yaml")
json = storage.read("file.json")
json = storage.read("file", "json")


data = [1,2,3,4]
storage.write("tom.pickle", data)
storage.write("bob.json", data)
storage.write("guess.file", data, "yml")
```

Also, for YAML files, you can put comments in:

```python
info = {
    "a": 1
}

num = 5
comm = f"""
# hello {num} dogs!!
# there
# big boy
"""
storage.write("t.yaml", info, comments=comm)
```

which will produce:

```yaml
# hello 5 dogs!!
# there
# big boy

a: 1
```

## Science Storage

Over the years I have collected a lot of data, but not completely documented
the sensors or their settings. I am trying to setup a data file that can:

- use primarly standard python libraries to read data files
- self documenting with info and `namedtuples`
- can use `gzip` for compression of large files

```python
from slurm import scistorage
from collections import namedtuple

Sensor = namedtuple("Sensor","x y z")

# document sensor setting in this data file
# there is no real format for this, just put good
# stuff here
info = {
    "TFmini": {
        "min": 0.3,
        "max": 12.0,
        "fov_deg": 4.6,
        "units": "m"
    },
    "LSM6DSOX": {
        "accel": {
            "range": (-4,4),
            "units": "g"
        },
        "gyro": {
            "range": (-2000,2000),
            "units": "dps"
        }
    },
    "LIS3MDL": {
        "range": (-4,4), # 4 gauss = 400 uT
        "units": "gauss"
    },
    "DPS310": {
        "sensors": ("temperature", "pressure")
    }
}

data = [] # some data stored in an array or deque
for i in range(100):
    data.append(Sensor(i,i,i)) # pretend you got some data from a sensor


scistorage.write(info, data, "data.pkl.gz") # *.gz uses gzip compression

bag = scistorage.read("data.pkl.gz")
print(bag["info"])
print(bag["data"])
```

## Network

```python
from slurm import network

print(network.get_ip()) # -> ip_address
print(network.host()) # -> (hostname, ip_address)
```

## Sleep Rate

Will sleep for a prescribed amount of time inside of a loop
irregardless of how long the loop takes

```python
from slurm import Rate

rate = Rate(10)  # let loop run at 10 Hz

while True:
    # do some processing
    rate.sleep()
```

## Files

```python
from slurm.files import rmdir, mkdir, run, rm, find

mkdir("some/path")
rmdir("some/path")
rm("/path/file.txt")
rm(["path/a.txt", "path/2/b.txt", "path/3/c.txt"])

find("/path/to/somewhere", "file_to_find") # -> list
find("/path/to/somewhere", "*.html") # -> list

run("ls -alh") # -> output
```

# MIT License

**Copyright (c) 2014 Kevin J. Walchko**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
