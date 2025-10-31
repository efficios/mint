# Copyright (C) 2025 Philippe Proulx <eeppeliteloop@gmail.com>
# SPDX-License-Identifier: MIT

add_executable (mint-tester mint-tester.cpp)
target_include_directories (mint-tester PRIVATE ../..)

add_executable (escape-tester escape-tester.cpp)
target_include_directories (escape-tester PRIVATE ../..)

add_executable (escape-ansi-tester escape-ansi-tester.cpp)
target_include_directories (escape-ansi-tester PRIVATE ../..)

add_executable (terminal-support-tester terminal-support-tester.cpp)
target_include_directories (terminal-support-tester PRIVATE ../..)

add_executable (terminal-support-errno-tester terminal-support-errno-tester.cpp)
target_include_directories (terminal-support-errno-tester PRIVATE ../..)
