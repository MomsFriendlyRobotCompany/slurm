![](pics/slurm.jpg)

# Slurm


[![Actions Status](https://github.com/MomsFriendlyRobotCompany/slurm/workflows/CheckPackage/badge.svg)](https://github.com/MomsFriendlyRobotCompany/slurm/actions)
![GitHub](https://img.shields.io/github/license/MomsFriendlyRobotCompany/slurm)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/slurm)
![PyPI](https://img.shields.io/pypi/v/slurm)
[![Downloads](https://img.shields.io/pypi/dm/slurm.svg)](https://img.shields.io/pypi/dm/slurm.svg)

**Under Development**


```python
from slurm import storage

yaml = storage.read("file.yaml")
json = storage.read("file.json")
json = storage.read("file", "json")


data = [1,2,3,4]
storage.write("bob.json", data)
storage.write("guess", data, "yml")
```

# MIT License

**Copyright (c) 2014 Kevin J. Walchko**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
