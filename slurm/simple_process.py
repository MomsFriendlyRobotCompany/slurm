# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2018 Kevin Walchko
# see LICENSE for full details
##############################################
import multiprocessing as mp
from colorama import Fore
import attr


@attr.s(slots=True)
class SimpleProcess(object):
    """
    A simple class to help processes start/stop easily. It is main intended for
    testing and some simple things.
    p = SimpleProcess()       # create process
    p.start(function)         # start the process, runs function
    ...                       # stuff happens
    p.join()                  # time to go ... bye!
    """
    ps = attr.ib(init=False, default=None)

    def __del__(self):
        if self.ps:
            self.join(0.1)

    @property
    def name(self):
        return self.ps.name

    @property
    def pid(self):
        return self.ps.pid

    def is_alive(self):
        """Check if the process is still running"""
        if self.ps:
            return self.ps.is_alive()
        else:
            return False

    def terminate(self):
        """Terminate the process"""
        if self.ps:
            self.ps.terminate()

    def start(self, func, name='simple_process', **kwargs):
        """Starts the process
          func: function for multi-process
          name: what to call the process
          kwargs: args to pass function
        """
        if kwargs:
            kwargs = kwargs['kwargs']  # WTF???
            self.ps = mp.Process(name=name, target=func, kwargs=kwargs)
        else:
            self.ps = mp.Process(name=name, target=func)

        self.ps.start()
        print(f'>> {Fore.GREEN}Started{Fore.RESET}: {self.ps.name}[{self.ps.pid}]')

    def join(self, timeout=1.0):
        """
        Attempts to join() the process with the given timeout. If that fails, it calls
        terminate().

        timeout: how long to wait for join() in seconds.
        """
        print(f'>> {Fore.RED}Stopping{Fore.RESET}: {self.ps.name}[{self.ps.pid}] ...')
        if self.ps:
            self.ps.join(timeout)
            if self.ps.is_alive():
                self.ps.terminate()
        self.ps = None
