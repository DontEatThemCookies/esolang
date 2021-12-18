## The Regular Brainfuck Interpreter
#### David Costell
#### Version 1.1 - December 18, 2021

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
tricks, it's a good ol' interpreter that just works.
The RBFI's implementation is based on fabianishere's
C interpreter(1) as well as the unofficial 
specification(2) authored by  Sunjay Varma.

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
Syntax:
```sh
# Python script
$ py rbfi.py [script filename]

# Windows executable
rbfi [script filename]
```

***

### Changelog
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