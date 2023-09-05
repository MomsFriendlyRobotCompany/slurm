
#pragma once


#include <filesystem>

namespace slurm {

namespace fs = std::filesystem;

fs::path get_temp(const std::string& file) {
  return std::filesystem::temp_directory_path() / file;
}

static
bool rmdir(const fs::path& path) {
  std::uintmax_t num = fs::remove_all(path);
  if (num == 0) return false;
  return true;
}

static
bool mkdir(const fs::path& path) {
  bool ret = fs::create_directories(path);
  return ret;
}

static
bool touch(const fs::path& path) {
  return false;
}

} // slurm