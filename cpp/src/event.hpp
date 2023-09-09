/**************************************************\
* The MIT License (MIT)
* Copyright (c) 2014 Kevin Walchko
* see LICENSE for full details
\**************************************************/
#pragma once

#include <atomic>

// https://gist.github.com/jncornett/e449826d2a1bd6b481f818176be0d2de
// https://stackoverflow.com/questions/69385119/how-do-wait-and-notify-work-for-stdatomic-in-c20
// A version of python's Event class. Assume is_set/set of a bool is atomic and
// no need for a mutex.
class Event {
public:
  Event() {}
  Event(const Event &e) = delete; // don't allow this
  ~Event() = delete;
  inline void set() noexcept { flag.test_and_set(); }
  inline void clear() noexcept { flag.clear(); }
  inline bool is_set() const { return flag.test(); }
  inline void wait(bool val) { flag.wait(val); } // block until value met
protected:
  std::atomic_flag flag{false}; // default to false
};
