## The Regular Brainfuck Interpreter
#### David Costell
#### Version 1.2.2 - January 30, 2022

***

Brainfuck is an esoteric imperative programming
language invented by Urban Muller in the 1990s.
It is a challenge to program in it, as its design
is very minimal, with only a memory tape, pointer
and eight instructions. Brainfuck is notable for being
one of the most popular esoteric languages. It is also
Turing-complete.

The Regular Brainfuck Interpreter (RBFI) is, well, a
regular Brainfuck interpreter. No special or unique
tricks, it's a good old interpreter that works.
The RBFI's implementation is influenced by 
fabianishere's C interpreter(1) as well as the 
unofficial specification(2) authored by Sunjay Varma.

RBFI is NOT guaranteed to run any Brainfuck program
without issues whatsoever. This is due to many details
about Brainfuck being ambiguous and thus left to the
implementer to decide the exact behavior. 
If you encounter any issues, you can contact me at: 
<davidcostell44@gmail.com>

***

### Features
* Interprets Urban Muller's Brainfuck esoteric
  programming language.

***

### Usage
Python 3.6 or higher is required to run RBFI. \
For Windows users, a standalone .exe file
is also available. \
For users of other OSes, you can build it yourself
using Nuitka if you somehow want RBFI as a binary:
```sh
# assuming you are in the /Brainfuck directory
python3 -mnuitka --follow-imports --onefile src\rbfi.py
# the resulting binary can be found in working dir
```

The syntax:
```sh
# Python script
$ python3 rbfi.py [-h] [-d] [BF script filename]

# Windows executable
> rbfi [-h] [-d] [BF script filename]
```
**Required**: \
`BF script filename` - The Brainfuck program to
interpret.

**Optional**: \
`-d` - For debugging purposes \
`-h` - Displays help

***

### Changelog
#### v.1.2.2 | 01/30/2022
* This version is a Minor Patch
  * Re-licensed under the terms of the WTFPL
   
#### v.1.2.1 | 01/04/2022
* This version is a Minor Patch
  * An extra newline will now be printed upon program \
    termination in order for proper text formatting
  * Added additional exception catch for OSError, usually \
    indicating that the specified file cannot be accessed
  * Converted rbfi.py from CRLF to LF
  * This release does NOT include an updated executable for \
    Windows users

#### v1.2 | 12/27/2021
* Enhanced argument parsing (argparse)
  * Added debug flag argument (-d) \
    This provides basic debugging details upon \
    completing execution of the Brainfuck program.
* Other miscellaneous changes

#### v1.1 | 12/18/2021
* Added some exception catching
* RBFI no longer explicitly removes any
non-instruction characters, only ignores them. This
also means RegEx is not used anymore.
* Other minor changes

#### v1.0 | 12/17/2021
* Initial release

***

### License
```txt
Copyright (c) 2021 David Costell <davidcostell44@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
```

***
(1) https://github.com/fabianishere/brainfuck \
(2) https://github.com/brain-lang/brainfuck/blob/master/brainfuck.md