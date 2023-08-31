#include <gtest/gtest.h>
#include "slurm.hpp"

// Demonstrate some basic assertions.
TEST(gciSensors, dummy) {
  // Expect two strings not to be equal.
  EXPECT_STRNE("hello", "world");
  // Expect equality.
  EXPECT_EQ(7 * 6, 42);

  EXPECT_TRUE(true);
}