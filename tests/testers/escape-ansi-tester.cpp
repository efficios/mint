/*
 * Copyright (C) 2025 Philippe Proulx <eeppeliteloop@gmail.com>
 * SPDX-License-Identifier: MIT
 */

#include <iostream>

#include "mint.hpp"

int main(int argc, char *argv[])
{
    if (argc < 2) {
        return 1;
    }

    std::cout << mint::escapeAnsi(mint::mint(argv[1], mint::When::Always));
    return 0;
}
