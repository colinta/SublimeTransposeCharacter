TransposeCharacter plugin for Sublime Text 2
============================================

Swaps two characters, lines, words, reverses a selection, or swaps two selections, depending on cursor location and selection(s).


Installation
------------

### Sublime Text 2

1. Using Package Control, install "TransposeCharacter"

Or:

1. Open the Sublime Text 2 Packages folder

    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/

2. clone this repo
3. Install keymaps for the commands (see Example.sublime-keymap for my preferred keys)

### Sublime Text 3

1. Open the Sublime Text 2 Packages folder
2. clone this repo, but use the `st3` branch

       git clone -b st3 git@github.com:colinta/SublimeTransposeCharacter

Commands
--------

`transpose_character`: Swaps two characters, reverses a selection, swaps two lines, or rotates multiple selections.

The behavior of `transpose_character` changes depending on the location of the
cursor and the selection.

If the cursor is in between two letters (anything other than a newline), it will
swap them:

`te|h  =>  the|`

At the beginning or end of a line, the behavior is to swap the lines:

    1. klmno|    1. abcde     1. abcde
    2. abcde  => 2. klmno| => 2. fghij
    3. fghij     3. fghij     3. klmno|


    1. fghij     1. fghij    1.|abcde
    2. klmno  => 2.|abcde => 2. fghij
    3.|abcde     3. klmno    3. klmno

If there is one selection, the selection *cursor* will be reversed in place.
This means you can move the cursor to the beginning or end of the selection,
which is very useful for extending line selections.

If there are multiple selections, the it swaps each pair of regions.

`‹abc›-‹ABC›-‹123›-‹456›  =>  ‹ABC›-‹abc›-‹456›-‹123› => ‹abc›-‹ABC›-‹123›-‹456›`
