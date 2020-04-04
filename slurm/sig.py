# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2014 Kevin Walchko
# see LICENSE for full details
##############################################
import signal
from colorama import Fore, Back, Style


class SignalCatch(object):
    """
    Catches SIGINT and SIGTERM signals and sets kill = True

    $ kill -l
     1) SIGHUP     2) SIGINT       3) SIGQUIT     4) SIGILL
     5) SIGTRAP    6) SIGABRT      7) SIGEMT      8) SIGFPE
     9) SIGKILL    10) SIGBUS     11) SIGSEGV    12) SIGSYS
    13) SIGPIPE    14) SIGALRM    15) SIGTERM    16) SIGURG
    17) SIGSTOP    18) SIGTSTP    19) SIGCONT    20) SIGCHLD
    21) SIGTTIN    22) SIGTTOU    23) SIGIO      24) SIGXCPU
    25) SIGXFSZ    26) SIGVTALRM  27) SIGPROF    28) SIGWINCH
    29) SIGINFO    30) SIGUSR1    31) SIGUSR2

    https://stackoverflow.com/questions/18499497/how-to-process-sigterm-signal-gracefully
    """
    _kill = False
    kill_init = False

    @property
    def kill(self):
        return self._kill

    @kill.setter
    def kill(self, val):
        self._kill = val
        print("SIGNAL CHANGED KILL:", self._kill)
        # raise Exception("WTF")

    def kill_signals(self):
        if self.kill_init:
            print("*** KILL ALREADY SET ***")
            return
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        self.kill_init = True

    def exit_gracefully(self, signum, frame):
        """
        When handler gets called, it sets the self.kill to True
        """
        if signum == 2:
            self.kill = True
            # print(Back.RED + ">> Got signal[{}]".format(signum) + Style.RESET_ALL)
            print(f"{Back.RED}>> Got signal[{signum}]{Style.RESET_ALL}")
        else:
            # print(Back.YELLOW + ">> Got signal[{}]".format(signum) + Style.RESET_ALL)
            print(f"{Back.YELLOW}>> Got signal[{signum}]{Style.RESET_ALL}")
