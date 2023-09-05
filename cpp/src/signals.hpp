/**************************************************\
* The MIT License (MIT)
* Copyright (c) 2014 Kevin Walchko
* see LICENSE for full details
\**************************************************/
#pragma once

// #include <functional>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
// #include <iostream>

/*
https://stackoverflow.com/questions/1641182/how-can-i-catch-a-ctrl-c-event
https://www.geeksforgeeks.org/inheritance-in-c/
https://stackoverflow.com/questions/12662891/how-can-i-pass-a-member-function-where-a-free-function-is-expected

http://www.yolinux.com/TUTORIALS/C++Signals.html
*/
/*
kevin@Logan build $ kill -l
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL
 5) SIGTRAP	 6) SIGABRT	 7) SIGEMT	 8) SIGFPE
 9) SIGKILL	10) SIGBUS	11) SIGSEGV	12) SIGSYS
13) SIGPIPE	14) SIGALRM	15) SIGTERM	16) SIGURG
17) SIGSTOP	18) SIGTSTP	19) SIGCONT	20) SIGCHLD
21) SIGTTIN	22) SIGTTOU	23) SIGIO	24) SIGXCPU
25) SIGXFSZ	26) SIGVTALRM	27) SIGPROF	28) SIGWINCH
29) SIGINFO	30) SIGUSR1	31) SIGUSR2

https://www.linusakesson.net/programming/tty/

SIGHUP - terminate on hangup condition
SIGINT - terminate, ^C
SIGQUIT - core dump, ^\
SIGPIPE - terminate, write to pipe with no readers
SIGCHLD - ignore, when a child process dies or changes state
SIGSTOP - suspend, ^Z, application suspends
SIGCONT - wake up, un-suspends a stopped process
SIGSTP - suspend, ^Z, suspends a process
*/

/*
 This class captures the SIGINT signal and sets ok to false. Since ok is
 static, any class that inherits this will see the status change and
 allow it close down cleanly.

  SigCapture sc;
  sc.on(); // will now capture SIGINT
  while (sig.ok) { do something }

 or choose a different signal like SIGHUP

  SigCapture sc;
  sc.capture(SIGHUP); // or sc.capture(SIGHUP, my_callback);
  while (sig.ok) { do something }
 */
class SigCapture {
public:
  SigCapture() : enabled(false) {}
  // static void my_handler(int s); // signal handler function
  // void capture(int sig, std::function<void(int)> func);
  void capture(int sig) {
    if (enabled) return;

    struct sigaction sigIntHandler;
    sigIntHandler.sa_handler = SigCapture::shutdown; // can I do this?
    sigemptyset(&sigIntHandler.sa_mask);
    sigIntHandler.sa_flags = 0;

    sigaction(sig, &sigIntHandler, NULL);

    enabled = true;
  }
  void capture(int sig, void (*func)(int)) {
    if (enabled) return;

    struct sigaction sigIntHandler;
    sigIntHandler.sa_handler = func;
    sigemptyset(&sigIntHandler.sa_mask);
    sigIntHandler.sa_flags = 0;

    sigaction(sig, &sigIntHandler, NULL);

    enabled = true;
  }
  void on() {
    if (enabled) return;

    struct sigaction sigIntHandler;
    sigIntHandler.sa_handler = SigCapture::shutdown;
    sigemptyset(&sigIntHandler.sa_mask);
    sigIntHandler.sa_flags = 0;

    sigaction(SIGINT, &sigIntHandler, NULL);

    enabled = true;
  }
  static void shutdown(int sig = 0) { ok = false; }

  // protected:
  inline static bool ok = true; // global status on if a SIGINT has occured
  bool enabled;                 // is it turned on?
};
