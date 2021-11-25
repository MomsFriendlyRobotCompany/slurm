# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2014 Kevin Walchko
# see LICENSE for full details
##############################################
import dill
from pathlib import Path
import gzip


def compression(path):
    """
    Based on filename, is compression being used?
    """
    compress = None
    ext = path.suffix
    if ext == ".gz":
        compress = True
    elif ext == ".dil":
        compress = False
    else:
        raise Exception(f"invalid file extension [{ext}], must be .dil or .dil.gz")

    return compress

def write(info, data, fname, compressionlevel=3):
    """
    Stores data in a binary file using dill. This is better than pickle when
    using namedtuples to store data.

    info: dict holding sensor info/settings
    data: sensor data, [{},{},...,{}]
    fname: file name, file extension: *.dil=uncompressess, *.dil.gz=compressed
    compressionlevel: [low,fastest] 1-9 [highest,slowest]
    """
    bag = {
        "info": info,
        "data": data
    }

    path = Path(fname).expanduser()
    compress = compression(path)

    with path.open("wb") as fd:
        if compress:
            d = dill.dumps(bag)
            d = gzip.compress(d, compresslevel=compressionlevel)
            fd.write(d)
        else:
            dill.dump(bag, fd)

def read(fname):
    """
    Opens and reads a data file.

    fname: file name, file extension: *.dil=uncompressess, *.dil.gz=compressed
    """
    path = Path(fname).expanduser()
    compress = compression(path)

    with path.open("rb") as fd:
        if compress:
            d = fd.read()
            d = gzip.decompress(d)
            data = dill.loads(d)
        else:
            data = dill.load(fd)

    return data
