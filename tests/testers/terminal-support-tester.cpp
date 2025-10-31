/*
 * Copyright (C) 2025 Philippe Proulx <eeppeliteloop@gmail.com>
 * SPDX-License-Identifier: MIT
 */

#include <iostream>

#include "mint.hpp"

int main()
{
    const auto support = mint::terminalSupport();

    switch (support) {
    case mint::TerminalSupport::None:
        std::cout << "none";
        break;
    case mint::TerminalSupport::BasicColor:
        std::cout << "basic-color";
        break;
    case mint::TerminalSupport::TrueColor:
        std::cout << "true-color";
        break;
    }

    return 0;
}
