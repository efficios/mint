# mint

![](logo.png)

_**mint**_ is a single C++11 header to format terminal text using a
simple tag-based markup syntax.

![](demo1.png)

`mint.hpp` offers the `mint::mint()` function which transforms a string
containing terminal attribute tags into another string containing actual
terminal
[SGR codes](https://en.wikipedia.org/wiki/ANSI_escape_code#SGR).

`mint::mint()` automatically detects terminal support. If the standard
output isn't connected to a compatible terminal, it removes the
attribute tags instead of converting them to SGR codes.

> [!IMPORTANT]
> You may copy `mint.hpp` as is to your project.
> The only requirements are Linux and C++11.

## Markup syntax

_mint_ tags allow you to specify text attributes like colors, bold,
underline, and italic formatting.

The _mint_ markup syntax is straightforward and composable.

An opening tag is, between `[` and `]`, an unordered sequence of
specifiers (all optional, but at least one):

| Specifier | Description |
|---|---|
| `!` | Bold |
| `-` | Dim |
| `_` | Underline |
| `'` | Italic |
| `^` | Reverse video |
| `*` | Bright foreground color |
| `COLOR` | Foreground color |
| `:COLOR` | Background color |

`COLOR` is one of:

* **ANSI 16-color palette**:

  | Code | Color |
  |------|-------|
  | `d` | Default |
  | `k` | Black |
  | `r` | Red |
  | `g` | Green |
  | `y` | Yellow |
  | `b` | Blue |
  | `m` | Magenta |
  | `c` | Cyan |
  | `w` | White |

* **True color**:

  `#` followed with six hex digits (like a CSS color).

  Note that you can set two foreground or background colors within a
  single opening tag, for example:

  ```
  A [r#e74c3c]wonderful [!:m:#9b59b6]day[//]!
  ```

  If you're calling `mint::mint()` in auto mode and
  `mint::terminalSupport()` reports only ANSI 16-color palette support,
  then this function will ignore the true color specifiers and only keep
  the basic ones.

Spaces are allowed between specifiers within an opening tag.

A closing tag contains one or more `/` characters between `[` and `]`.
Each `/` closes one level.

Escape `[` with `\[` and `\` with `\\`. Use `mint::escape()` to escape
text for `mint::mint()`. Use `mint::escapeAnsi()` to return to a plain
string (no SGR codes) from the result of `mint::mint()`.

Opening and closing tags may be nested (maximum four levels of depth)
and must be balanced. Note that nesting is additive: a nested tag cannot
cancel an active attribute.

> [!IMPORTANT]
> The SGR code of any opening and closing tag always starts with a reset.

Because you must balance opening and closing tags, _mint_ is more suited
to [{fmt}](https://fmt.dev/12.0/) and `printf()` than I/O streams:

**Using _mint_ with {fmt}:**

```cpp
fmt::print(mint::mint("[w:r] [!]ERROR[/]: At offset [!*b]{:#x}[/]: {} [/]"),
           exc.offset(), exc.what());
```

![](demo2.png)

> [!NOTE]
> In this example, `mint::mint()` formats before `fmt::print()`,
> therefore we don't need to escape `exc.what()` with `mint::escape()`.

## API usage

Include the `mint.hpp` header in your C++ code:

```cpp
#include "mint.hpp"
```

See the documentation of `mint::mint()`, `mint::escape()`,
`mint::escapeAnsi()`, and `mint::terminalSupport()` in the header file
itself.

This project suggests that you wrap `mint::mint()` into your own
function which at least checks the [`NO_COLOR`](https://no-color.org/)
environment variable once to set the `when` parameter of `mint::mint()`
(`mint::When::Auto` or `mint::When::Never`).

## Testing

To test _mint_:

1. Build the testers:

   ```
   $ mkdir -p build && cd build && cmake .. && make
   ```

1. Test with [pytest](https://docs.pytest.org/en/stable/),
   providing the build directory:

   ```
   $ MINT_BUILD_DIR=$PWD pytest ../tests
   ```

## Contributing

To report a bug,
[create a GitHub issue](https://github.com/efficios/mint/issues/new).
