/**************************************\
 * The MIT License (MIT)
 * Copyright (c) 2014 Kevin Walchko
 * see LICENSE for full details
\**************************************/
#pragma once

#include <math.h>
#include <stdint.h>

namespace Units {

// Angular
constexpr float rad2deg = 180.0f / M_PI;
constexpr float deg2rad = M_PI / 180.0f;
constexpr float rps2rpm = 0.0f;     // FIXME
constexpr float rpm2rps = 0.10472f; // FIXME

// Magnetism
constexpr float gauss2tesla = 1e-5f;
constexpr float tesla2gauss = 1e5f;

// Pressure
constexpr float pa2atm = 9.86923e-6f;
constexpr float atm2pa = 101325.0f;

// Temperature
inline float f2c(float f) { return 0.5555556f * (f - 32.0f); }
inline float c2f(float c) { return 1.8f * c + 32.0f; }
inline float c2k(float c) { return c + 273.15f; }
inline float k2c(float k) { return k - 273.15f; }

// Distance
constexpr float m2mi  = 0.000621371f; // meters to miles
constexpr float mi2m  = 1609.34f;     // miles to meters
constexpr float km2mi = 0.621371f;
constexpr float mi2km = 1.60934f;
constexpr float ft2m  = 0.3048; // feet to meters

// bits/bytes ... useful?
static uint16_t to_b16(const uint8_t b[2], const bool little = true) {
  union {
    uint16_t s;   // short
    uint8_t b[2]; // byte
  } buff;

  if (little) {
    buff.b[0] = b[0];
    buff.b[1] = b[1];
  }
  else {
    buff.b[0] = b[1];
    buff.b[1] = b[0];
  }

  return buff.s;
}

/*
 * Need to fix day for 29, 30, 31 days
 *
 * Is this useful?
 */
inline float decimal_date(uint8_t yr, uint8_t mon, uint8_t day) {
  return static_cast<float>(yr) + static_cast<float>(mon) / 12.0f +
         static_cast<float>(day) / 30.0f;
}

} // namespace Units