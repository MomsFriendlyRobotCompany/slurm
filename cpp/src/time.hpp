/**************************************************\
* The MIT License (MIT)
* Copyright (c) 2014 Kevin Walchko
* see LICENSE for full details
\**************************************************/
#pragma once

#include <chrono> // time: sec, msec, usec
#include <ctime>  // time
#include <iomanip>
#include <sstream> // ostringstream
#include <thread>  // sleep_for


inline void msleep(int msec) {
  std::this_thread::sleep_for(std::chrono::milliseconds(msec));
}
inline void usleep(int usec) {
  std::this_thread::sleep_for(std::chrono::microseconds(usec));
}
inline void sleep(int sec) {
  std::this_thread::sleep_for(std::chrono::seconds(sec));
}


// std::string time_date();
static std::string time_date() {
  time_t t     = std::time(nullptr);
  struct tm lt = *std::localtime(&t);

  std::ostringstream oss;
  oss << std::put_time(&lt, "%d-%m-%Y %H:%M:%S");
  return oss.str();
}


static uint64_t microsSinceEpoch() {
  // struct timeval tv;
  // uint64_t micros = 0;
  // gettimeofday(&tv, NULL);
  // micros = ((uint64_t)tv.tv_sec) * 1000000 + tv.tv_usec;

  uint64_t micros = 0;
  // using namespace std::chrono;
  micros = duration_cast<std::chrono::microseconds>(
               std::chrono::system_clock::now().time_since_epoch())
               .count();

  return micros;
}

static uint64_t millis() {
  // struct timeval tv;
  // uint64_t micros = 0;
  // gettimeofday(&tv, NULL);
  // micros = ((uint64_t)tv.tv_sec) * 1000000 + tv.tv_usec;

  uint64_t msec = 0;
  // using namespace std::chrono;
  msec = duration_cast<std::chrono::milliseconds>(
             std::chrono::system_clock::now().time_since_epoch())
             .count();

  return msec;
}

//////////////////////////////////////////////////////////////////////
/*
 A simple stop watch to time an event.
 */
// class Clock {
// public:
//     Clock();
//     void start();
//     double stop();

// protected:
//     double now();
//     double hack;
// };

// Clock::Clock(): hack(0.0) {}

// void Clock::start(){
//     hack = now();
// }

// double Clock::stop(){
//     return now() - hack;
// }

// double Clock::now(){
//     auto now_ms = time_point_cast<microseconds>(system_clock::now());
//     auto epic = now_ms.time_since_epoch();
//     double time = (double)epic.count();
//     return time/1E6;
// }

//////////////////////////////////////////////////////////////////////

// /*
//  Allows you to set a rate in hertz for a loop to run and this class
//  keeps track of it.

//  Rate r(10); // sets 10 Hz
//  while (1){
//     // do something
//     r.sleep();  // will adjust sleep time to keep 10Hz
//  }
//  */
// class Rate {
// public:
//   Rate(double hertz) {
//     last_time = time_point_cast<std::chrono::milliseconds>(
//         std::chrono::system_clock::now());
//     // dt = std::chrono::milliseconds(int(1000/hertz));
//     dt = std::chrono::milliseconds(int(1000 / hertz));
//   }

//   void sleep(void) {
//     auto now = time_point_cast<std::chrono::milliseconds>(
//         std::chrono::system_clock::now());

//     auto diff = duration_cast<std::chrono::milliseconds>(now - last_time);
//     if (diff < dt) {
//       std::this_thread::sleep_for(dt - diff);
//     }
//     last_time = time_point_cast<std::chrono::milliseconds>(
//         std::chrono::system_clock::now());
//   }

// protected:
//   std::chrono::time_point<std::chrono::system_clock> last_time;
//   // std::chrono::duration<double> dt;
//   std::chrono::milliseconds dt;
// };

/////////////////////////////////////////////////////////////////////////

// static uint64_t microsSinceEpoch() {
//   // struct timeval tv;
//   // uint64_t micros = 0;
//   // gettimeofday(&tv, NULL);
//   // micros = ((uint64_t)tv.tv_sec) * 1000000 + tv.tv_usec;

//   uint64_t micros = 0;
//   // using namespace std::chrono;
//   micros = duration_cast<std::chrono::microseconds>(
//                std::chrono::system_clock::now().time_since_epoch())
//                .count();

//   return micros;
// }

// static uint64_t millis() {
//   // struct timeval tv;
//   // uint64_t micros = 0;
//   // gettimeofday(&tv, NULL);
//   // micros = ((uint64_t)tv.tv_sec) * 1000000 + tv.tv_usec;

//   uint64_t msec = 0;
//   // using namespace std::chrono;
//   msec = duration_cast<std::chrono::milliseconds>(
//              std::chrono::system_clock::now().time_since_epoch())
//              .count();

//   return msec;
// }

////////////////////////////////////////////////////////////////////////////
// https://en.cppreference.com/w/cpp/chrono

/*
https://www.geeksforgeeks.org/chrono-in-c/

system_clock-It is the current time according to the system (regular clock
  which we see on the toolbar of the computer). It is written as-
  std::chrono::system_clock
steady_clock-It is a monotonic clock that will never be adjusted.It goes at a
  uniform rate. It is written as- std::chrono::steady_clock
high_resolution_clock– It provides the smallest possible tick period. It is
  written as-std::chrono::high_resolution_clock
*/

/*
https://en.cppreference.com/w/cpp/chrono/c/timespec_get
https://en.cppreference.com/w/cpp/chrono/c
C++17
If base is TIME_UTC, then:
- ts->tv_sec is set to the number of seconds since epoch, truncated to a whole
value
- ts->tv_nsec is set to the integral number of nanoseconds, rounded to the
resolution of the system clock #include <cstdio> #include <ctime>

inline double difftime(const timespec &a, const timespec &b) {
    return (double)(a.tv_sec - b.tv_sec) + 1e-9*(a.tv_nsec - b.tv_nsec);
}

int main()
{
    std::timespec ts;
    std::timespec_get(&ts, TIME_UTC);
    char buf[100];
    std::strftime(buf, sizeof buf, "%D %T", std::gmtime(&ts.tv_sec));
    std::printf("Current time: %s.%09ld UTC\n", buf, ts.tv_nsec);

    timespec ts2;
    timespec_get(&ts2, TIME_UTC);
    std::printf("diff %f\n", difftime(ts2,ts));
}
>> Current time: 06/24/16 20:07:42.949494132 UTC
*/
