Super Stack! is a stack-based esoteric programming language by User:Orange in the Esolang Wiki.
It was created in 2009, and its core revolves on a manipulable stack. It is Turing-complete (more accurately, Brainfuck-equivalent). 

This folder contains v2 of the official Super Stack! implementation in Python, originally written in Python 2.4 and ported to Python 3 by David Costell (davidcostell44@gmail.com).

Further information:
https://esolangs.org/wiki/Super_Stack!

INSTRUCTIONS:

1. Open your terminal
2. Run the following command:

python superstack.py [program name].ss! [-d]

The -d parameter is optional.
It stands for "debug", and enabling it will result in the program executing with additional debug functions.

SAMPLE PROGRAMS:

Hello World
```
0 33 100 108 114 111 87 32 44 111 108 108 101 72
if outputascii fi
```

Cat
```
1
if
    0
    inputascii
    if outputascii fi `output-stack
    pop
    10 outputascii
fi
```

Fibonacci Sequence
```
0 1
if
    dup output
    dup cycle add
fi
```

"Guess the Passcode"
```
0
58 101 100 111 67 32
115 115 97 80 32
114 101 116 110 69
if outputascii fi pop

inputascii

`compare each letter
109 sub
not if pop
97 sub
not if pop
114 sub
not if pop
115 sub
not if pop
104 sub
not if pop
	0
	100 101 116 110 97 114 71 32
	115 115 101 99 99 65
	if outputascii fi pop
	quit
fi fi fi fi fi

`wrong
0
71 78 79 82 87
if outputascii fi pop
```

FizzBuzz
```
-100
if
    dup 101 add
    
    dup output
    
    dup 3 mod
    not if
        pop
        0 122 122 105 102 `fizz
        if outputascii fi pop
        0
    fi pop
    
    dup 5 mod
    not if
        pop
        0 122 122 117 98 `buzz
        if outputascii fi pop
        0
    fi pop
    
    10 outputascii `newline
    
    pop
    1 add
fi

inputascii
```

"Simple Chat Bot"
```
1 if pop
   0 58 116 117 112 110 105
   if outputascii fi pop
   
   inputascii 0
   
   5 random
   if pop
       cycle if cycle fi
   0 fi pop
   
   0 58 116 117 112 116 117 111
   if outputascii fi pop
   
   cycle if dup outputascii cycle fi
   10 outputascii
1 fi
```

Taken from the Example Programs section in the Super Stack! wiki page.