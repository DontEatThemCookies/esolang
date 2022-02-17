"""
bf4hc - brainfuck for humans compiler
Transpiler for the "human-friendly" Brainfuck derivative
Version 1.3 - 17th of February, 2022

Copyright © 2022 David Costell <davidcostell44@gmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
"""
import argparse, pathlib, os
from string import printable

# Argparse setup
parser = argparse.ArgumentParser(description='bf4hc - brainfuck for humans compiler v1.3')
parser.add_argument('file', help='transcompilation target (the file to compile)')
parser.add_argument('-o', help='optional filename for output program', default='')
args = parser.parse_args()

# Raise an error if the specified input file doesn't exist
if not os.path.exists(args.file):
    raise FileNotFoundError(f'file "{args.file}" was not found')

# Instruction table ('BF4H':'BF') 
table = {
    # Standard instruction set
    'left':'<',
    'right':'>',
    'incr':'+',
    'decr':'-',
    'out':'.',
    'inp':',',
    'loop(':'[',
    ')':']',
    # Extended instruction set
    'clr':'[-]',
    'clear':'[-]',
    'set': '[-]',
    'setn': '[-]',
}

with open(args.file, 'r') as inputfile:
    # Read the file's contents as the program, removing CRLF and tabs as
    # well as replacing the alternate separators (e.g. ':') with whitespace,
    # resulting in a clean, easily-parsable list of bf4h instructions 
    program = [inst for inst in inputfile.read().replace('\r', '').replace('\t', ' ')
    .replace('\n', ' ').replace(':', ' ').replace(';', ' ').strip().split() if inst != '']
    
    # Prevent instructions being parsed inside of bf4h-style comments
    start = end = 0
    for idx,inst in enumerate(program):
        if inst == '/*':
            start = idx
        elif inst == '*/':
            end = idx
    [program.remove(i) for i in program[start+1:end]]

    # Code for the set and setn instructions
    for idx,inst in enumerate(program):
        try:
            if inst == 'set':
                    if program[idx+1][0] in printable:
                        num = ord(program[idx+1][0])
                        value = ("incr " * num).split()
                        [program.insert(idx+1, val) for val in value]
                    else:
                        raise Exception
            elif inst == 'setn':
                    num = int(program[idx+1])
                    value = ("incr " * num).split()
                    [program.insert(idx+1, val) for val in value]
        except Exception:
            raise ValueError(f'set: invalid value "{program[idx+1]}"')

    # Perform translation (substitution) of BF4H instructions to BF instructions
    outputcode = [table[inst] for inst in program if inst in table]
    # Syntax checks
    if outputcode.count('[') > outputcode.count(']'):
        raise SyntaxError('invalid syntax - unclosed jump-if-zero "[" instruction(s)')
    if outputcode.count('[') < outputcode.count(']'):
        raise SyntaxError('invalid syntax - stray jump-unless-zero "]" instruction(s)')
    if outputcode.count('/*') > outputcode.count('/*'):
        raise SyntaxError('invalid syntax - unterminated comment marker(s)')
    if outputcode.count('*/') < outputcode.count('/*'):
        raise SyntaxError('invalid syntax - stray comment ending marker(s)')

    # Determine and define the output file's name
    outputname = pathlib.Path(f'./{args.file}').stem if not args.o else args.o
    # Remove redundant .bf postfix if a file name was specified ending in ".bf"
    outputname = outputname[:-3] if outputname.endswith('.bf') else outputname

    with open(f'{outputname}.bf', 'w') as outputfile:
        # Write the translated code into the output file
        outputfile.write(''.join((inst for inst in outputcode)))
