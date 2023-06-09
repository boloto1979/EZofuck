The EZofuck programming language is a unique and esoteric creation based on the famous Brainfuck, developed by the German programmer Urban Müller. EZofuck was conceived as a tribute and variation of Brainfuck, maintaining the minimalist and defiant essence of its precursor.

Like Brainfuck, EZofuck adopts a programming model based on an infinite string of numbered cells, where each cell contains an integer numerical value. The pointer points to the current cell, allowing manipulation of these values ​​through a limited set of commands.

Inspired by the intriguing and obscure nature of Brainfuck, the EZofuck language raises the bar for complexity and obscurity. While Brainfuck has a minimum set of eight commands, EZofuck adds a few new commands and transforms the syntax in an even more cryptic way.

EZofuck maintains the basic Brainfuck commands, such as incrementing (+) and decrementing (-) the current cell value, advancing (>) and rewinding (<) the pointer on the ribbon, printing (.) the current cell value, and reading ( ,) an input value and store it in the current cell.

```
+++++ +++++             set cell 0 to 10
[
    >+++++ ++++++++     set cell 1 to 70 ('H')
    >+++++ ++++++        set cell 2 to 30 ('e')
    >+++++ +++++         set cell 3 to 20 ('l')
    >+++++ +             set cell 4 to 5 ('o')
    <<<.                  print 'H'
    >.                    print 'e'
    +++++ ++.             print 'l'
    .                     print 'l'
    +++++ +++++ +.        print 'o'
    >+++.                 print ','
    <<++++ +++++ +.       print ' '
    >.                    print 'W'
    +++++ ++.             print 'o'
    -----.                print 'r'
    ----- ----.           print 'l'
    ----- -----.          print 'd'
    >+++++ +++.           print '!'
    >.                    print '\n'
]
```
Here are the basic EZofuck language commands:

1.. - Prints the current cell value on the tape.<br>
2., - Reads a value from the input and stores it in the current cell.<br>
3.+ - Increments the current cell value by 1.<br>
4.- - Decrements the current cell value by 1.<br>
5.> - Moves the pointer to the next cell on the ribbon.<br>
6.< - Moves the pointer to the previous cell on the ribbon.<br>
7.[ - Starts a loop. If the current cell value is 0, the program jumps to the command after the next ']'.<br>
8.] - Ends a loop. If the value of the current cell is different from 0, the program returns to the command after the corresponding '['.<br>

In addition to these commands, EZofuck introduces additional commands that expand the range of possibilities. For example, the command ! performs a special arithmetic operation on the current cell, based on a peculiar mathematical sequence, and the ? triggers a series of random events that can affect program execution.

EZofuck's syntax is purposefully obscure and full of cryptic symbols in order to increase the challenge and complexity of the language. This makes reading and writing programs in EZofuck a Herculean task, but also provides a unique and exciting experience for programmers looking to venture into the esoteric realms of programming.

Although the EZofuck language is purely fictional and has no real implementations, it serves as a creative homage to Brainfuck and the visionary mind of Urban Müller, who inspired us to explore the limits of programming and create new forms of expression in the art of coding.

## Interpreter.tester.py

You can run the interpreter by supplying an EZofuck code in the code variable and get the resulting output. In the example, the EZofuck code +++++[>++++[>++<-]<-]>>. prints the character 'A' on the output.

## Compiler.test.py

In this example, the EZofuckCompiler class has a compile method that takes the EZofuck code as input and generates an optimized equivalent Python code. The compiler generates Python code that uses a list called "tape" to represent the tape of cells and a pointer called "ptr" to indicate the current cell.

The compiler steps through each EZofuck command and generates the corresponding Python code. EZofuck commands map to operations on the "tape" list and the "ptr" pointer of the generated Python code. For example, the command '.' is compiled into the sys.stdout.write(chr(tape[ptr])) operation, which prints the current cell value to the tape.

The compiler also handles the '[' and ']' loop commands to ensure the iterations run correctly. It uses indentation to generate well-structured Python code.
