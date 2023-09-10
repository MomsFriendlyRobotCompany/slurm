/**************************************************\
* The MIT License (MIT)
* Copyright (c) 2014 Kevin Walchko
* see LICENSE for full details
\**************************************************/
#pragma once

#include <chrono> // time: sec, msec, usec
// #include <ctime>  // time
#include <thread>  // this_thread

/*
 Allows you to set a rate in hertz for a loop to run and this class
 keeps track of it.

 Rate r(10); // sets 10 Hz
 while (1){
    // do something
    r.sleep();  // will adjust sleep time to keep 10Hz
 }
 */
class Rate {
public:
  Rate(double hertz) {
    last_time = time_point_cast<std::chrono::milliseconds>(
        std::chrono::system_clock::now());
    dt = std::chrono::milliseconds(int(1000 / hertz));
  }

  void sleep(void) {
    auto now = time_point_cast<std::chrono::milliseconds>(
        std::chrono::system_clock::now());

    auto diff = duration_cast<std::chrono::milliseconds>(now - last_time);
    if (diff < dt) {
      std::this_thread::sleep_for(dt - diff);
    }
    last_time = time_point_cast<std::chrono::milliseconds>(
        std::chrono::system_clock::now());
  }

protected:
  std::chrono::time_point<std::chrono::system_clock> last_time;
  // std::chrono::duration<double> dt;
  std::chrono::milliseconds dt;
};
