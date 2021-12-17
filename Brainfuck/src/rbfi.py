"""
David Costell's Regular Brainfuck Interpreter [RBFI]
Your run-of-the-mill, not-so-special Brainfuck implementation
Version 1.0 - Finalized December 17, 2021
---------------------------------------------------------------------------
Copyright (c) 2021 David Costell <davidcostell44@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
"""
import sys, re                                       # Imports
try: file = open(sys.argv[1])                        # Get file from command line args
except IndexError: sys.exit(print("rbfi: No file specified.\nUsage: py rbfi.py [filename]"))

array = [0]*30000                                    # Initialize the array (tape)
l = len(array)                                       # Get length of the array
ptr = array[0]                                       # Initialize the tape pointer
code = re.sub("[^><+\-.,\[\]]", "", file.read())     # Initialize the actual code (removes all comment chars)
codepos = 0                                          # Tracks the parser's current position in the code
loopstack = []                                       # Used for loops

while codepos < len(code):                           # Iterate through the instructions and execute them
    if code[codepos] == ">": ptr+=1 if ptr<l else ptr  # Move pointer right (increment)
    if code[codepos] == "<": ptr-=1 if ptr>0 else ptr  # Move pointer left (decrement)
    if code[codepos] == "+": array[ptr]+=1 if array[ptr]<255 else -255 # Increment the cell where the pointer is
    if code[codepos] == "-": array[ptr]-=1 if array[ptr]>0 else -255   # Decrement the cell where the pointer is
    if code[codepos] == ".": sys.stdout.write(chr(array[ptr])) # Output ASCII value of cell where the pointer is
    if code[codepos] == ",": array[ptr]=ord(sys.stdin.read(1)) # Take input, read first byte as ASCII and assigns
                                                               # it as the value of the cell where the pointer is
    try:
        if code[codepos] == "[": loopstack.append(codepos)      # Begin a loop (Jump if zero)
        if code[codepos] == "]":                                # End a loop (Jump unless zero)
            if array[ptr] == 0: loopstack.pop(-1)
            else: codepos = loopstack[-1]
    except Exception as e: sys.stderr.write(f"Error executing loop: {e}")
    sys.stdout.flush()                                      # Flush the standard output stream
    codepos += 1                                            # Move to the next instruction (character)
"""
# Optional debugging code
try:
    print("-"*55,f"Pointer position [Zero-indexed]: {str(ptr)}",
          f"Pointer cell value: {array[ptr]}","Array:",sep="\n")
    for byte in array: print("["+str(byte)+"]", end="")    # Array contents
except Exception as e:
    print("Exception while getting debug info:", e)
"""