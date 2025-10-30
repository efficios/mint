/*
 * Copyright (C) 2025 Philippe Proulx <eeppeliteloop@gmail.com>
 * SPDX-License-Identifier: MIT
 */

#include <iostream>

#include "mint.hpp"

int main()
{
    std::cout << (mint::hasTerminalSupport() ? "true" : "false") << '\n';
    return 0;
}
