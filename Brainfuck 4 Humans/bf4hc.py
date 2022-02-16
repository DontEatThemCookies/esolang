"""
bf4hc - brainfuck for humans compiler
Transpiler for the "human-friendly" Brainfuck derivative
Version 1.2 - 16th of February, 2022

Copyright © 2022 David Costell <davidcostell44@gmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
"""
import argparse, pathlib, os

# Argparse setup
parser = argparse.ArgumentParser(description='bf4hc - brainfuck for humans compiler v1.2')
parser.add_argument('file', help='transcompilation target (the file to compile)')
parser.add_argument('-o', help='optional filename for output program', default='')
args = parser.parse_args()

# Raise an error if the specified input file doesn't exist
if not os.path.exists(args.file):
    raise FileNotFoundError(f'file "{args.file}" was not found')

# Instruction table ('BF4H':'BF') 
table = {
    # Standard instructions
    'left':'<',
    'right':'>',
    'incr':'+',
    'decr':'-',
    'out':'.',
    'inp':',',
    'loop(':'[',
    ')':']',
    # Other instructions
    'clr':'[-]',
}

with open(args.file, 'r') as inputfile:
    # Read the file's contents as the program, removing CRLF and tabs as
    # well as replacing the alternate separators (e.g. ':') with whitespace,
    # resulting in a clean, easily-parsable list of bf4h instructions 
    program = [inst for inst in inputfile.read().replace('\r', '').replace('\t', ' ')
    .replace('\n', ' ').replace(':', ' ').replace(';', ' ').strip().split() if inst != ''
    if inst in table or inst in '/**/']
    
    # Prevent instructions being parsed inside of bf4h-style comments
    start = end = 0
    for idx,inst in enumerate(program):
        if inst == '/*':
            start = idx
        elif inst == '*/':
            end = idx
    [program.remove(i) for i in program[start+1:end]]

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
