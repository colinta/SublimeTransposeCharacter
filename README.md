TransposeCharacter
==================

Swaps two characters, lines, words, reverses a selection, or swaps two selections, depending on cursor location and selection(s).

Installation
------------

Using Package Control, install "TransposeCharacter" or clone this repo in your packages folder.

I recommended you add key bindings for the commands. I've included my preferred bindings below.
Copy them to your key bindings file (⌘⇧,).

Commands
--------

`transpose_character`: Swaps two characters, reverses a selection (moves the cursor from the front to back and vice versa), moves text up/down to the next line, or swaps multiple selections.

The behavior of `transpose_character` changes depending on the location of the cursor and the selection.

If the cursor (`|`) is in between two letters (anything other than a newline), it will swap them:

`te|h  =>  the|` (you can reverse the direction, too, I have ⌃T move the cursor to the right, and ⇧⌃T move it to the left)

At the beginning or end of a line, the behavior is to move the line up/down:

    # Cursor at the end of the line moves that line down
    1  klmno|        1  abcde         1  abcde
    2  abcde    =>   2  klmno|   =>   2  fghij
    3  fghij         3  fghij         3  klmno|


    # Cursor at the beginning of the line moves that line up
    1  fghij         1  fghij         1 |abcde
    2  klmno    =>   2 |abcde    =>   2  fghij
    3 |abcde         3  klmno         3  klmno

(If this seems like an unintuitive connection to "transpose", keep in mind that we are, in effect, transposing two *lines*)

If there is one selection, the selection *cursor* will be reversed in place.
This means you can move the cursor to the beginning or end of the selection,
which is very useful for extending line selections.

    # []| represents the selection and cursor
    1  [klmno]|   =>   1  |[klmno]    =>     1  [klmno]|

If there are multiple selections, the it swaps each pair of regions.

`‹abc›-DEF-‹123›-‹456›  =>  DEF-‹abc›-‹456›-‹123› => ‹abc›-DEF-‹123›-‹456›`

Key Bindings
------------

Copy these to your user key bindings file.

<!-- keybindings start -->
    { "keys": ["ctrl+t"], "command": "transpose_character" },
    { "keys": ["ctrl+shift+t"], "command": "transpose_character", "args": {"reverse": true} },
<!-- keybindings stop -->
