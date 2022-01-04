"""
David Costell's Regular Brainfuck Interpreter [RBFI]
Your run-of-the-mill, not-so-special Brainfuck implementation
Version 1.2.1 - Finalized January 4, 2022

This work is licensed under the MIT License. See the LICENSE file for details.
"""
import sys, argparse                                 # Imports

parser=argparse.ArgumentParser(description="a regular Brainfuck interpreter")
parser.add_argument("file", help="the Brainfuck program to interpret (file)")
parser.add_argument("-d", help="for debugging purposes", action="store_true")
args=parser.parse_args()

try: file = open(args.file)                          # Get file from args
except FileNotFoundError: sys.exit(print("rbfi: The specified file was not found"))
except OSError: sys.exit(print("rbfi: Couldn't access the specified file (OSError)"))

array = [0]*30000                                    # Initialize the array (memory tape of 30,000 cells)
l = len(array)                                       # Get length of the array
ptr = array[0]                                       # Initialize the tape pointer
code = file.read()                                   # Initialize the Brainfuck code
codepos = 0                                          # Tracks the current position in the code
loopstack = []                                       # Used by the loop instructions "[" and "]"

while codepos < len(code):                           # Iterate through the instructions and execute them
    try:
        if code[codepos] == ">": ptr+=1 if ptr<l else ptr  # Move pointer right (increment)
        if code[codepos] == "<": ptr-=1 if ptr>0 else ptr  # Move pointer left (decrement)
        if code[codepos] == "+": array[ptr]+=1 if array[ptr]<255 else -255 # Increment the cell where the pointer is
        if code[codepos] == "-": array[ptr]-=1 if array[ptr]>0 else -255   # Decrement the cell where the pointer is
        if code[codepos] == ".": sys.stdout.write(chr(array[ptr])) # Output ASCII value of cell where the pointer is
        if code[codepos] == ",": array[ptr]=ord(sys.stdin.read(1)) # Read 1-byte input as ASCII and assigns it as the
                                                                # value of the cell where the pointer is
        if code[codepos] == "[": loopstack.append(codepos)      # Begin a loop (Jump if zero)
        if code[codepos] == "]":                                # End a loop (Jump unless zero)
            if array[ptr] == 0: loopstack.pop(-1)
            else: codepos = loopstack[-1]

        sys.stdout.flush()                                      # Flush the standard output stream
        codepos += 1                                            # Move to the next instruction (character)

    except Exception as error:                                  # Catch any errors during runtime
        sys.exit(print(f"rbfi: Runtime exception ({type(error).__name__})", error, sep="\n"))

if args.d:                                                      # Debug mode
    print("", "-" * 55, "RBFI - Debugging details",
     f"Pointer position [Zero-indexed]: {str(ptr)}",
     f"Pointer cell value: {array[ptr]}", "Tape (first 50 cells):",
     sep="\n")
    for byte in array[:50]: print(f"[{byte}]", end="")
    print("")                                                   # Newline
