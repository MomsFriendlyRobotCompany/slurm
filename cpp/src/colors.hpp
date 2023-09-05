/**************************************************\
* The MIT License (MIT)
* Copyright (c) 2014 Kevin Walchko
* see LICENSE for full details
\**************************************************
* This is based off the python model colorama syntax.
* It should only work on Unix/Linux/macOS
*
* Examples:
* cout << Fore.RED << "hello" << Fore.RESET << endl;
* printf("%shello%s", Fore.RED.c_str(), Fore.RESET.c_str());
*/

#pragma once

#include <string>

namespace slurm {

class ForeColor {
public:
  std::string BLACK   = "\x1b[30m";
  std::string RED     = "\x1b[31m";
  std::string GREEN   = "\x1b[32m";
  std::string YELLOW  = "\x1b[33m";
  std::string BLUE    = "\x1b[34m";
  std::string MAGENTA = "\x1b[35m";
  std::string CYAN    = "\x1b[36m";
  std::string WHITE   = "\x1b[37m";
  std::string RESET   = "\x1b[0m";
};

class BackColor {
public:
  std::string BLACK   = "\x1b[40m";
  std::string RED     = "\x1b[41m";
  std::string GREEN   = "\x1b[42m";
  std::string YELLOW  = "\x1b[43m";
  std::string BLUE    = "\x1b[44m";
  std::string MAGENTA = "\x1b[45m";
  std::string CYAN    = "\x1b[46m";
  std::string WHITE   = "\x1b[47m";
  std::string RESET   = "\x1b[0m";
};

// do I want to do this?
// static ForeColor Fore;
// static BackColor Back;

} // slurm
