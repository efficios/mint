/*
 * Copyright (C) 2025 Philippe Proulx <eeppeliteloop@gmail.com>
 * SPDX-License-Identifier: MIT
 */

#include <iostream>
#include <cerrno>

#include "mint.hpp"

int main()
{
    errno = 42;
    mint::terminalSupport();
    std::cout << errno << '\n';
    return 0;
}
