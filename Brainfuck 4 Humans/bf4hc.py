"""
bf4hc - brainfuck for humans compiler
Transpiler for the "human-friendly" Brainfuck derivative
Version 1.1 - 2nd of February, 2022

Copyright © 2022 David Costell <davidcostell44@gmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
"""
import argparse, pathlib, os

# Argparse setup
parser = argparse.ArgumentParser(description='bf4hc - brainfuck for humans compiler v1.1')
parser.add_argument('file', help='transcompilation target (the file to compile)')
parser.add_argument('-o', help='optional filename for output program', default='')
args = parser.parse_args()

# Raise an error if the specified input file doesn't exist
if not os.path.exists(args.file):
    raise FileNotFoundError(f'file "{args.file}" was not found')

# Translation table ('BF4H':'BF') 
table = {
    # Standard instructions
    'left':'<',
    'right':'>',
    'incr':'+',
    'decr':'-',
    'out':'.',
    'inp':',',
    'loop(':'[',
    ')':']'
}

with open(args.file, 'r') as inputfile:
    # Read the file's contents as the program, removing CRLF and tabs
    # as well as replacing the alternate separators ':;' with whitespace
    # In addition, ignore any line that starts with '//' (comment symbol)
    program = [line for line in inputfile.read()
    .replace('\r', '').replace('\n', ' ').replace('\t', ' ')
    .replace(':', ' ').replace(';', ' ').strip().split() if line != ''
    if not line.strip().startswith('//')]

    # Convert BF4H instructions to BF instructions
    outputcode = [table[line] for line in program if line in table]

    # Syntax checks
    if outputcode.count('[') > outputcode.count(']'):
        raise SyntaxError('invalid syntax - unclosed jump-if-zero "[" instruction')
    if outputcode.count('[') < outputcode.count(']'):
        raise SyntaxError('invalid syntax - stray jump-unless-zero "]" instruction')

    # Determine and define the output file's name
    outputname = pathlib.Path(f'./{args.file}').stem if not args.o else args.o
    # Remove redundant .bf postfix if afile name was specified ending in ".bf"
    outputname = outputname[:-3] if outputname.endswith('.bf') else outputname

    with open(f'{outputname}.bf', 'w') as outputfile:
        # Write the translated code into the output file
        outputfile.write(''.join((instruction for instruction in outputcode)))
