# Copyright (C) 2025 Philippe Proulx <eeppeliteloop@gmail.com>
# SPDX-License-Identifier: MIT

import subprocess
import pytest
import os

testers_path = os.path.join(os.environ['MINT_BUILD_DIR'], 'tests', 'testers')
mint_tester_path = os.path.join(testers_path, 'mint-tester')


def _test_success(input_string: str, expected_output: str):
    result = subprocess.run([mint_tester_path, input_string], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout == expected_output


def _test_failure(input_string: str, expected_error: str):
    result = subprocess.run([mint_tester_path, input_string], capture_output=True, text=True)
    assert result.returncode == 1
    assert result.stdout == f'ERROR: {expected_error}'


def _test_escape(input_string: str, expected_output: str):
    result = subprocess.run([os.path.join(testers_path, 'escape-tester'), input_string],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout == expected_output


def _test_escape_ansi(input_string: str, expected_output: str):
    result = subprocess.run([os.path.join(testers_path, 'escape-ansi-tester'), input_string],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout == expected_output


def test_bold():
    _test_success('[!]bold text[/]', '\033[0;1mbold text\033[0m')


def test_underline():
    _test_success('[_]underlined text[/]', '\033[0;4munderlined text\033[0m')


def test_italic():
    _test_success('[#]italic text[/]', '\033[0;3mitalic text\033[0m')


def test_dim():
    _test_success('[-]dim text[/]', '\033[0;2mdim text\033[0m')


def test_bright_red():
    _test_success('[*r]bright red[/]', '\033[0;91mbright red\033[0m')


def test_bright_alone():
    _test_success('[*]bright alone[/]', '\033[0mbright alone\033[0m')


def test_bright_default_color():
    _test_success('[*d]bright default[/]', '\033[0;99mbright default\033[0m')


def test_fg_color_default():
    _test_success('[d]default color[/]', '\033[0;39mdefault color\033[0m')


def test_fg_color_black():
    _test_success('[k]black text[/]', '\033[0;30mblack text\033[0m')


def test_fg_color_red():
    _test_success('[r]red text[/]', '\033[0;31mred text\033[0m')


def test_fg_color_green():
    _test_success('[g]green text[/]', '\033[0;32mgreen text\033[0m')


def test_fg_color_yellow():
    _test_success('[y]yellow text[/]', '\033[0;33myellow text\033[0m')


def test_fg_color_blue():
    _test_success('[b]blue text[/]', '\033[0;34mblue text\033[0m')


def test_fg_color_magenta():
    _test_success('[m]magenta text[/]', '\033[0;35mmagenta text\033[0m')


def test_fg_color_cyan():
    _test_success('[c]cyan text[/]', '\033[0;36mcyan text\033[0m')


def test_fg_color_white():
    _test_success('[w]white text[/]', '\033[0;37mwhite text\033[0m')


def test_bg_color_default():
    _test_success('[:d]default bg[/]', '\033[0;49mdefault bg\033[0m')


def test_bg_color_black():
    _test_success('[:k]black bg[/]', '\033[0;40mblack bg\033[0m')


def test_bg_color_red():
    _test_success('[:r]red bg[/]', '\033[0;41mred bg\033[0m')


def test_bg_color_green():
    _test_success('[:g]green bg[/]', '\033[0;42mgreen bg\033[0m')


def test_bg_color_yellow():
    _test_success('[:y]yellow bg[/]', '\033[0;43myellow bg\033[0m')


def test_bg_color_blue():
    _test_success('[:b]blue bg[/]', '\033[0;44mblue bg\033[0m')


def test_bg_color_magenta():
    _test_success('[:m]magenta bg[/]', '\033[0;45mmagenta bg\033[0m')


def test_bg_color_cyan():
    _test_success('[:c]cyan bg[/]', '\033[0;46mcyan bg\033[0m')


def test_bg_color_white():
    _test_success('[:w]white bg[/]', '\033[0;47mwhite bg\033[0m')


def test_bold_underline():
    _test_success('[!_]bold and underlined[/]', '\033[0;1;4mbold and underlined\033[0m')


def test_bold_dim():
    _test_success('[!-]bold and dim[/]', '\033[0;1;2mbold and dim\033[0m')


def test_bold_italic():
    _test_success('[!#]bold and italic[/]', '\033[0;1;3mbold and italic\033[0m')


def test_dim_underline():
    _test_success('[-_]dim and underline[/]', '\033[0;2;4mdim and underline\033[0m')


def test_dim_italic():
    _test_success('[-#]dim and italic[/]', '\033[0;2;3mdim and italic\033[0m')


def test_underline_italic():
    _test_success('[_#]underline and italic[/]', '\033[0;3;4munderline and italic\033[0m')


def test_all_text_attributes():
    _test_success('[!-_#]all text attrs[/]', '\033[0;1;2;3;4mall text attrs\033[0m')


def test_attribute_order_bold_red():
    _test_success('[r!]red bold[/]', '\033[0;1;31mred bold\033[0m')


def test_attribute_order_mixed():
    _test_success('[#_!]mixed order[/]', '\033[0;1;3;4mmixed order\033[0m')


def test_attribute_order_color_first():
    _test_success('[y!_#:b]color first[/]', '\033[0;1;3;4;33;44mcolor first\033[0m')


def test_bold_red():
    _test_success('[!r]bold red[/]', '\033[0;1;31mbold red\033[0m')


def test_underline_blue():
    _test_success('[_b]underline blue[/]', '\033[0;4;34munderline blue\033[0m')


def test_italic_green():
    _test_success('[#g]italic green[/]', '\033[0;3;32mitalic green\033[0m')


def test_dim_red():
    _test_success('[-r]dim red[/]', '\033[0;2;31mdim red\033[0m')


def test_fg_and_bg_colors():
    _test_success('[y:b]yellow on blue[/]', '\033[0;33;44myellow on blue\033[0m')


def test_bold_italic_underline_red_on_white():
    _test_success('[!#_r:w]complex[/]', '\033[0;1;3;4;31;47mcomplex\033[0m')


def test_bright_bold_cyan():
    _test_success('[*!c]bright bold cyan[/]', '\033[0;1;96mbright bold cyan\033[0m')


def test_bright_yellow():
    _test_success('[*y]bright yellow[/]', '\033[0;93mbright yellow\033[0m')


def test_bright_green():
    _test_success('[*g]bright green[/]', '\033[0;92mbright green\033[0m')


def test_bright_magenta():
    _test_success('[*m]bright magenta[/]', '\033[0;95mbright magenta\033[0m')


def test_bright_black():
    _test_success('[*k]bright black[/]', '\033[0;90mbright black\033[0m')


def test_bright_blue():
    _test_success('[*b]bright blue[/]', '\033[0;94mbright blue\033[0m')


def test_bright_white():
    _test_success('[*w]bright white[/]', '\033[0;97mbright white\033[0m')


def test_bright_with_bg_only():
    _test_success('[*:r]bright bg[/]', '\033[0;41mbright bg\033[0m')


def test_plain_text():
    _test_success('no tags here', 'no tags here')


def test_empty_string():
    _test_success('', '')


def test_empty_tagged_content():
    _test_success('[r][/]', '\033[0;31m\033[0m')


def test_tags_with_surrounding_text():
    _test_success('before [r]red[/] after', 'before \033[0;31mred\033[0m after')


def test_multiple_separate_tags():
    _test_success('[r]red[/] and [b]blue[/]', '\033[0;31mred\033[0m and \033[0;34mblue\033[0m')


def test_escape_backslash():
    _test_success('\\\\', '\\')


def test_escape_bracket():
    _test_success('\\[', '[')


def test_escape_in_text():
    _test_success('Use \\[r] for red', 'Use [r] for red')


def test_nested_bold_in_red():
    _test_success('[r]red [!]and bold[/][/]',
                  '\033[0;31mred \033[0;1;31mand bold\033[0;31m\033[0m')


def test_nested_red_in_bold():
    _test_success('[!]bold [r]and red[/][/]',
                  '\033[0;1mbold \033[0;1;31mand red\033[0;1m\033[0m')


def test_nested_underline_in_italic():
    _test_success('[#]italic [_]and underline[/][/]',
                  '\033[0;3mitalic \033[0;3;4mand underline\033[0;3m\033[0m')


def test_nested_dim_in_bold():
    _test_success('[!]bold [-]and dim[/][/]',
                  '\033[0;1mbold \033[0;1;2mand dim\033[0;1m\033[0m')


def test_nested_bold_in_dim():
    _test_success('[-]dim [!]and bold[/][/]',
                  '\033[0;2mdim \033[0;1;2mand bold\033[0;2m\033[0m')


def test_nested_bg_in_fg():
    _test_success('[r]red [:b]on blue[/][/]',
                  '\033[0;31mred \033[0;31;44mon blue\033[0;31m\033[0m')


def test_nested_fg_in_bg():
    _test_success('[:b]blue bg [y]yellow text[/][/]',
                  '\033[0;44mblue bg \033[0;33;44myellow text\033[0;44m\033[0m')


def test_nested_three_levels():
    _test_success('[r]red [!]bold [_]underline[/][/][/]',
                  '\033[0;31mred \033[0;1;31mbold \033[0;1;4;31munderline\033[0;1;31m\033[0;31m\033[0m')


def test_nested_bright_in_color():
    _test_success('[r]red [*]bright[/][/]',
                  '\033[0;31mred \033[0;91mbright\033[0;31m\033[0m')


def test_nested_color_in_bright():
    _test_success('[*r]bright red [g]green[/][/]',
                  '\033[0;91mbright red \033[0;92mgreen\033[0;91m\033[0m')


def test_nested_all_attributes():
    _test_success('[!]b [_]u [#]i [r]r[/][/][/][/]',
                  '\033[0;1mb \033[0;1;4mu \033[0;1;3;4mi \033[0;1;3;4;31mr\033[0;1;3;4m\033[0;1;4m\033[0;1m\033[0m')


def test_nested_with_text_between():
    _test_success('[r]start [!]middle[/] end[/]',
                  '\033[0;31mstart \033[0;1;31mmiddle\033[0;31m end\033[0m')


def test_nested_same_attribute():
    _test_success('[!]bold [!]still bold[/][/]',
                  '\033[0;1mbold \033[0;1mstill bold\033[0;1m\033[0m')


def test_nested_multiple_colors():
    _test_success('[r]red [g]green [b]blue[/][/][/]',
                  '\033[0;31mred \033[0;32mgreen \033[0;34mblue\033[0;32m\033[0;31m\033[0m')


def test_nested_multiple_backgrounds():
    _test_success('[:r]red bg [:b]blue bg[/][/]',
                  '\033[0;41mred bg \033[0;44mblue bg\033[0;41m\033[0m')


def test_consecutive_nested_tags():
    _test_success('[!][_][#]text[/][/][/]',
                  '\033[0;1m\033[0;1;4m\033[0;1;3;4mtext\033[0;1;4m\033[0;1m\033[0m')


def test_empty_opening_tag():
    _test_failure('[]', 'Empty opening tag')


def test_expecting_color_letter_fg():
    _test_failure('[', 'Expecting `]` to terminate the opening tag')


def test_expecting_color_letter_bg():
    _test_failure('[:', 'Expecting color letter')


def test_unknown_color_letter():
    _test_failure('[x]text[/]', 'Unknown color letter `x`')


def test_unknown_bg_color_letter():
    _test_failure('[:x]text[/]', 'Unknown color letter `x`')


def test_incomplete_escape_sequence():
    _test_failure('text\\', 'Incomplete escape sequence at end of string')


def test_invalid_escape_sequence():
    _test_failure('\\a', 'Invalid escape sequence')


def test_unbalanced_closing_tag():
    _test_failure('[/]', 'Unbalanced closing tag')


def test_unbalanced_closing_tag_extra():
    _test_failure('[r]text[/] xyz [/] meow', 'Unbalanced closing tag')


def test_expecting_bracket_after_slash():
    _test_failure('[/x', 'Expecting `]` after `[/`')


def test_unbalanced_opening_tag():
    _test_failure('[r]text', 'Unbalanced opening tag')


def test_unbalanced_opening_tag_nested():
    _test_failure('[r]text [!]more', 'Unbalanced opening tag')


def test_unclosed_opening_tag():
    _test_failure('[r', 'Expecting `]` to terminate the opening tag')


def test_maximum_nesting_depth_exceeded():
    _test_failure('[r][g][b][y][m][c]text[/][/][/][/][/][/]', 'Maximum nesting depth exceeded')


def test_escape_backslash():
    _test_escape('\\', '\\\\')


def test_escape_bracket():
    _test_escape('[', '\\[')


def test_escape_both():
    _test_escape('\\[', '\\\\\\[')


def test_escape_plain_text():
    _test_escape('hello', 'hello')


def test_escape_mixed():
    _test_escape('Use [r] for red', 'Use \\[r] for red')


def test_escape_multiple_brackets():
    _test_escape('[red] [blue]', '\\[red] \\[blue]')


def test_escape_multiple_backslashes():
    _test_escape('\\\\\\', '\\\\\\\\\\\\')


def test_escape_tag_syntax():
    _test_escape('[!r]bold red[/]', '\\[!r]bold red\\[/]')


def test_escape_ansi_plain_text():
    _test_escape_ansi('plain text', 'plain text')


def test_escape_ansi_bold():
    _test_escape_ansi('[!]bold text[/]', 'bold text')


def test_escape_ansi_red():
    _test_escape_ansi('[r]red text[/]', 'red text')


def test_escape_ansi_bold_red():
    _test_escape_ansi('[!r]bold red[/]', 'bold red')


def test_escape_ansi_nested():
    _test_escape_ansi('[r]red [!]and bold[/][/]', 'red and bold')


def test_escape_ansi_multiple_tags():
    _test_escape_ansi('[r]red[/] and [b]blue[/]', 'red and blue')


def test_escape_ansi_all_attributes():
    _test_escape_ansi('[!-_#*r:b]complex[/]', 'complex')


def test_escape_ansi_bright_colors():
    _test_escape_ansi('[*g]bright green[/]', 'bright green')


def test_escape_ansi_with_surrounding_text():
    _test_escape_ansi('before [y]yellow[/] after', 'before yellow after')


def test_escape_ansi_empty_string():
    _test_escape_ansi('', '')


def test_escape_ansi_nested_three_levels():
    _test_escape_ansi('[r]red [!]bold [_]underline[/] back[/] normal[/]', 'red bold underline back normal')
