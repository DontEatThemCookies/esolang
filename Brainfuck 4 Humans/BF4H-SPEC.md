# brainfuck for humans (bf4h)
## Official Language Specification v1
* Version 1.2, 02/16/2022
* Authored by David Costell

## Introduction
brainfuck for humans, or in its short form **bf4h**, is a transpiled esoteric language 
designed to make brainfuck coding "a little easier to do." In bf4h, all BF instructions
are transformed from symbols to a familiar Latin letter form. They're still not really that 
verbose, as they range from 3-5 character instructions. You could think of BF as 
machine code and bf4h as assembly.

The ultimate goal of bf4h is to make BF more readable (perhaps more understandable) to the human coder. So if you're tired of using bracket/period/semicolon keys, bf4h is the solution.

## Features
Firstly, the instructions have changed as aforementioned. The full instruction table
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

Tab separation (since 1.2):
incr	decr

Take note that even the loop instructions
follow this rule:
loop( incr decr )

Unseparated instructions will be ignored
as they will be treated as comments:
incrdecr
```
In addition to the default brainfuck comments (which is any character
that isn't a BF instruction), bf4h supports a higher-level form of commenting.
Below is how to make a bf4h-style comment:
```bf
/*
Yes, they're just C-style comments.

bf4h-style comments must begin with "/*" and terminated with "*/", otherwise
raising a syntax error. Any instruction that is enclosed within a comment block
are ignored. bf4h-style comments are mostly just to enhance readability, and
the original BF style of commenting is still fully supported.
*/

/* Instructions in this line are ignored: right incr out */
But these instructions are not - inp out
```

## Instructions
This table formally defines bf4h's instructions compared to their counterpart in the original BF:

| instruction                 	| bf4h  	| brainfuck 	| version |
|-----------------------------	|-------	|-----------	|---------
| move pointer left           	| left  	| <         	| 1.0
| move pointer right          	| right 	| >         	| 1.0
| increment cell value        	| incr  	| +         	| 1.0
| decrement cell value        	| decr  	| -         	| 1.0
| output ascii value of cell  	| out   	| .         	| 1.0
| input value into cell       	| inp   	| ,         	| 1.0
| start loop (jump if zero)   	| loop( 	| [         	| 1.0
| end loop (jump unless zero) 	| )     	| ]         	| 1.0
| clr (sets cell value to zero) | clr       | \[-]          | 1.2

## Implementations
The de-facto official implementation of bf4h is **bf4hc** (bf4h compiler), written
in Python (version 3.6+ required.) bf4hc cleanly transpiles to plain brainfuck.
It's licensed under the terms of the WTFPL by David Costell (the author of this spec.)

## Miscellaneous
This is a code snippet to convert plain brainfuck to bf4h.
For optimal results, remove any non-instruction characters in your BF code (such as comments)
```py
strg = 'your brainfuck code here [,.]'

# Separate instructions with whitespace then do the translation of symbols with .replace()
output = ''.join(c if (i + 1) % 1 else c + ' ' for (i, c) in enumerate(list(strg)))
.replace('<', 'left').replace('>', 'right').replace('+', 'incr').replace('-', 'decr')
.replace('.','out').replace(',', 'inp').replace('[', 'loop(').replace(']', ')').strip()
```

## Epilogue
bf4h is a joke - brainfuck will always be a brainfuck to code in.

For feedback such as errata/suggestions, feel free to contact the author of bf4h
("DontEatThemCookies" on GitHub).
