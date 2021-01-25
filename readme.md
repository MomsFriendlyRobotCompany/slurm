![](https://github.com/MomsFriendlyRobotCompany/slurm/blob/master/pics/slurm.jpg?raw=true)

# Slurm


[![Actions Status](https://github.com/MomsFriendlyRobotCompany/slurm/workflows/walchko%20pytest/badge.svg)](https://github.com/MomsFriendlyRobotCompany/slurm/actions)
![GitHub](https://img.shields.io/github/license/MomsFriendlyRobotCompany/slurm)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/slurm)
![PyPI](https://img.shields.io/pypi/v/slurm)

This is a collection of tools I have used over the years collected together.

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

## Network

```python
from slurm import network

ip = network.get_ip()
print(ip)
```

## Sleep Rate

Will sleep for a prescribed amount of time inside of a loop
irregardless of how long the loop takes

```python
from slurm.rate import Rate

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

## Google Drive Access

This only supports downloading shared file links.

```python
from slurm.googledrive import GoogleDrive

url = "shared link from google drive"
gd = GoogleDrive()
gd.download(url, dumpHeader=True)
```

# MIT License

**Copyright (c) 2014 Kevin J. Walchko**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
