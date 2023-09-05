#include <gtest/gtest.h>
#include <iostream>
#include "slurm.hpp"

using namespace std;

TEST(slurm, logger) {
  EXPECT_NO_THROW({
    slurm::Logger log("file.log",stderr);
    cerr << "hello" << endl;
    EXPECT_TRUE(true);
    log.close();
  });
  EXPECT_TRUE(slurm::rmdir("file.log"));
}

TEST(slurm, file) {
  bool ret = slurm::mkdir("./my/deep/dir");
  EXPECT_TRUE(ret);
  ret = slurm::rmdir("./my/deep/dir");
  EXPECT_TRUE(ret);
}

TEST(slurm, colorization) {
  slurm::ForeColor Fore;
  slurm::BackColor Back;

  EXPECT_NO_THROW({
    cout << Back.BLUE << Fore.YELLOW;
    cout << "hello there";
    cout << Fore.RESET << Back.RESET << endl;
  });
}