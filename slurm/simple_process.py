# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2018 Kevin Walchko
# see LICENSE for full details
##############################################
import multiprocessing as mp
from colorama import Fore
# import attr


# @attr.s(slots=True)
class SimpleProcess:
    """
    A simple class to help processes start/stop easily. It is main intended for
    testing and some simple things.

    .. code-block:: python

        p = SimpleProcess()       # create process
        p.start(function)         # start the process, runs function
        ...                       # stuff happens
        p.join()                  # time to go ... bye!
    """
    # _ps = attr.ib(init=False, default=None)
    _ps = None

    def __del__(self):
        if self._ps:
            self.join(0.1)

    @property
    def name(self):
        return self._ps.name

    @property
    def pid(self):
        return self._ps.pid

    def is_alive(self):
        """Check if the process is still running"""
        if self._ps:
            return self._ps.is_alive()
        else:
            return False

    def terminate(self):
        """Terminate the process"""
        if self._ps:
            self._ps.terminate()

    def start(self, func, name='simple_process', **kwargs):
        """Starts the process
          :func: function for multi-process
          :name: what to call the process
          :kwargs: args to pass function
        """
        if kwargs:
            kwargs = kwargs['kwargs']  # WTF???
            self._ps = mp.Process(name=name, target=func, kwargs=kwargs)
        else:
            self._ps = mp.Process(name=name, target=func)

        self._ps.start()
        print(f'>> {Fore.GREEN}Started{Fore.RESET}: {self._ps.name}[{self._ps.pid}]')

    def join(self, timeout=1.0):
        """
        Attempts to join() the process with the given timeout. If that fails, it calls
        terminate().

            :timeout: how long to wait for join() in seconds.
        """
        print(f'>> {Fore.RED}Stopping{Fore.RESET}: {self._ps.name}[{self._ps.pid}] ...')
        if self._ps:
            self._ps.join(timeout)
            if self._ps.is_alive():
                self._ps.terminate()
        self._ps = None
