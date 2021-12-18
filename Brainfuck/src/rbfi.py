"""
David Costell's Regular Brainfuck Interpreter [RBFI]
Your run-of-the-mill, not-so-special Brainfuck implementation
Version 1.1 - Finalized December 18, 2021
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
import sys                                           # Imports
try: file = open(sys.argv[1])                        # Get file from command line args
except IndexError: sys.exit(print("rbfi: No file specified.\nUsage: py rbfi.py [filename].bf"))
except FileNotFoundError: sys.exit(print("rbfi: The specified file was not found."))

array = [0]*30000                                    # Initialize the array (memory tape, 30,000 cells)
l = len(array)                                       # Get length of the array
ptr = array[0]                                       # Initialize the tape pointer
code = file.read()                                   # Initialize the Brainfuck file
codepos = 0                                          # Tracks the current position in the code
loopstack = []                                       # Used for loops

while codepos < len(code):                           # Iterate through the instructions and execute them
    try:
        if code[codepos] == ">": ptr+=1 if ptr<l else ptr  # Move pointer right (increment)
        if code[codepos] == "<": ptr-=1 if ptr>0 else ptr  # Move pointer left (decrement)
        if code[codepos] == "+": array[ptr]+=1 if array[ptr]<255 else -255 # Increment the cell where the pointer is
        if code[codepos] == "-": array[ptr]-=1 if array[ptr]>0 else -255   # Decrement the cell where the pointer is
        if code[codepos] == ".": sys.stdout.write(chr(array[ptr])) # Output ASCII value of cell where the pointer is
        if code[codepos] == ",": array[ptr]=ord(sys.stdin.read(1)) # Take input, read first byte as ASCII and assigns
                                                                   # it as the value of the cell where the pointer is
        if code[codepos] == "[": loopstack.append(codepos)      # Begin a loop (Jump if zero)
        if code[codepos] == "]":                                # End a loop (Jump unless zero)
            if array[ptr] == 0: loopstack.pop(-1)
            else: codepos = loopstack[-1]
        """
        # Extra debug instruction from Urban Muller's original BF interpreter
        # See: https://esolangs.org/wiki/Brainfuck#Extensions
        if code[codepos] == "#":
            print("-" * 55, f"Pointer position [Zero-indexed]: {str(ptr)}",
             f"Pointer cell value: {array[ptr]}", "Tape (first 50 cells):",
             sep="\n")
            for byte in array: print("[" + str(byte) + "]", end="")   
        """
        sys.stdout.flush()                                      # Flush the standard output stream
        codepos += 1                                            # Move to the next instruction (character)
    except Exception as error:                                  # Catch any errors during runtime
        print(f"rbfi: Runtime exception ({type(error).__name__})",
              error, sep="\n")