/**************************************\
 * The MIT License (MIT)
 * Copyright (c) 2014 Kevin Walchko
 * see LICENSE for full details
\**************************************/
#pragma once

// #include <iostream>
// #include <stdio.h> // freopen
#include <iomanip> // put_time
#include <ctime>   // time stuff
#include <sstream> // convert to string
// #include <cstdio>

namespace slurm {

class Logger {
  public:
  Logger(const std::string& filename, FILE *stream=stdout) : stream(stream) {
    // std::string fname = get_timedate() + filename;
    std::string fname = filename;
    freopen (fname.c_str(), "w", stream);
  }

  ~Logger() {
    if (stream != nullptr) fclose(stream);
  }

  void close() {
    fclose(stream);
    stream = nullptr;
  }

  std::string get_timedate() {
    auto t = std::time(nullptr);
    auto tm = *std::localtime(&t);

    std::ostringstream oss;
    oss << std::put_time(&tm, "%Y-%m-%d_%H-%M-%S_");
    return oss.str();
  }

  protected:
  FILE *stream;
};

} // slurm