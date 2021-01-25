#!/usr/bin/env python
from slurm import network, storage

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
