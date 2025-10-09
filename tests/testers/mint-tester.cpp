/*
 * Copyright (C) 2025 Philippe Proulx <eeppeliteloop@gmail.com>
 * SPDX-License-Identifier: MIT
 */

#include <iostream>
#include <stdexcept>

#include "mint.hpp"

int main(int argc, char *argv[])
{
    if (argc < 2) {
        return 1;
    }

    try {
        std::cout << mint::mint(argv[1], true);
    } catch (const std::runtime_error& exc) {
        std::cout << "ERROR: " << exc.what();
        return 1;
    }

    return 0;
}
