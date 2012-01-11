TransposeCharacter plugin for Sublime Text 2
=============================================

Swaps two characters, lines, words, or reverse a word.  Depending on cursor location and selection(s).


Installation
------------

1. Using Package Control, install "TransposeCharacter"

Or:

1. Open the Sublime Text 2 Packages folder

    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/

2. clone this repo

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

If there is one selection, it will be reversed in place.

(I'm using `‹›` to indicate "selected text")

`‹race car›  =>  ‹rac ecar›`

If there are multiple selections, the built-in `transpose` command is used, which rotates the selections.

`‹abc›-‹efg›-‹ijk›  =>  ‹ijk›-‹abc›-‹efg› => ‹efg›-‹ijk›-‹abc›  =>  ‹abc›-‹efg›-‹ijk›`