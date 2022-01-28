# brainfuck for humans compiler (bf4hc)

**bf4hc** is the de-facto official implementation of the bf4h esoteric language.
It transcompiles bf4h programs into plain Brainfuck, and is 100% compliant with the specification for bf4h. All comments are ignored and do not make it into the output.

## Requirements
* Python 3.6 or newer installed

## Usage
```
$ python3 bf4hc.py [input filename] (-o [output filename])
```
`[input filename]` required. The bf4h program to transpile.

`-o [output filename]` optional. Sets a specified string to be the output filename. If not specified, output filename will be identical to input file.

Example usage:
```
$ python3 bf4hc.py program.bf4h -o output.bf
```

## License
```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2022 David Costell <davidcostell44@gmail.com>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
```