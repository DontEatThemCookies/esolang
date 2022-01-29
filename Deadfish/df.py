"""
Deadfish Interpreter for Python 3+
v1 - 01/29/2022

https://esolangs.org/wiki/Deadfish

David Costell (DontEatThemCookies on GitHub)
WTFPL v2
"""

try:
    acc = 0
    while True:
        # Get input program
        cmd = input(">> ")

        # Check if the input matches a file
        try:
            cmd = open(cmd).read().strip() 
        except OSError: 
            pass

        # Execute given instructions
        for inst in cmd:
            if inst == "i":
                acc += 1
            elif inst == "d":
                acc -= 1
            elif inst == "s":
                acc *= acc
            elif inst == "o":
                print(acc)
            
            if acc == 256 or acc < 0:
                acc = 0
# Graceful exit for Ctrl + C, Ctrl + D/Ctrl + Z & Return
except KeyboardInterrupt:
    exit(0)
except EOFError:
    exit(0)
