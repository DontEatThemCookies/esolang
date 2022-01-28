# brainfuck for humans (bf4h)
## Official Language Specification v1
* Version 1, 01/28/2022
* Authored by David Costell

## Introduction
brainfuck for humans, or in its short form **bf4h**, is a transpiled esoteric language 
designed to make Brainfuck coding "a little easier to do." In bf4h, all BF instructions
are transformed from symbols to a familiar Latin letter form. They're still not really that 
verbose, as they're still made up of 3-5 characters, so think of the original BF as machine 
code and bf4h as Assembly. Alternatively BF is to bf4h in the same way JavaScript is to 
TypeScript. Sort of.

The ultimate goal of bf4h is to make BF just a little bit more readable (maybe even more 
understandable) to the human coder. So if you're tired of using bracket/period/semicolon keys, 
bf4h is the solution.

## Features
Firstly, the instructions have changed as aforementioned. The full translation table
can be found in the **Instructions** section just below this one.

In bf4h, **all instructions must be separated.**  This is done in order to increase 
readability. There are multiple ways to achieve instruction separation:
```
Whitespace separation:
incr decr

Semicolon separation:
incr;decr

Colon separation:
incr:decr

Newline separation:
incr
decr

Take note that even the loop instructions
follow this rule:
loop( incr decr )

Unseparated instructions will be ignored
as they will be treated as comments:
incrdecr
```
In addition to the default Brainfuck comments (which is any character
that isn't a BF instruction), bf4h supports a higher-level form of commenting.
Below is how to make a bf4h-style comment:
```bf
// bf4h-style comments must begin with "//"
// Any line in a bf4h program beginning with "//" is fully
// ignored, just like how normal BF treats non-instruction characters.
// bf4h-style comments are mostly just to enhance readability, and
// the old BF style of commenting is still fully supported.

// Instructions in this line are ignored: right incr out
But these instructions are not - inp out
```

## Instructions
This table formally defines bf4h's instructions compared to their counterpart in the original BF:

| instruction                 	| bf4h  	| brainfuck 	|
|-----------------------------	|-------	|-----------	|
| move pointer left           	| left  	| <         	|
| move pointer right          	| right 	| >         	|
| increment cell value        	| incr  	| +         	|
| decrement cell value        	| decr  	| -         	|
| output ascii value of cell  	| out   	| .         	|
| input value into cell       	| inp   	| ,         	|
| start loop (jump if zero)   	| loop( 	| [         	|
| end loop (jump unless zero) 	| )     	| ]         	|

## Implementations
The de-facto official implementation of bf4h is **bf4hc** (bf4h compiler), written
in Python (version 3.6+ required.) bf4hc cleanly transpiles to plain Brainfuck.
It's licensed under the terms of the WTFPL by David Costell (the author of this spec.)

## Miscellaneous
This is a code snippet to convert plain Brainfuck to bf4h.
For optimal results, remove any non-instruction symbols in your BF code (such as comments)
```py
strg = 'your brainfuck code here'

# Separate instructions with whitespace then do the translation of symbols with .replace()
output = ''.join(c if (i + 1) % 1 else c + ' ' for (i, c) in enumerate(list(strg)))
.replace('<', 'left').replace('>', 'right').replace('+', 'incr').replace('-', 'decr')
.replace('.','out').replace(',', 'inp').replace('[', 'loop(').replace(']', ')').strip()
```

## Epilogue
For feedback such as errata/suggestions, feel free to contact the author of bf4h
("DontEatThemCookies" on GitHub).
