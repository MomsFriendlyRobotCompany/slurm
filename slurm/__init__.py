# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2014 Kevin Walchko
# see LICENSE for full details
##############################################

from .sig import SignalCatch
from .rate import Rate
from .simple_process import SimpleProcess

from importlib.metadata import version # type: ignore

__author__ = 'Kevin Walchko'
__license__ = 'MIT'
__version__ = version("slurm")
