# Copyright (C) 2025 Philippe Proulx <eeppeliteloop@gmail.com>
# SPDX-License-Identifier: MIT

add_executable(mint-tester
    mint-tester.cpp
)

target_include_directories(mint-tester PRIVATE ../..)

add_executable(escape-tester
    escape-tester.cpp
)

target_include_directories(escape-tester PRIVATE ../..)
