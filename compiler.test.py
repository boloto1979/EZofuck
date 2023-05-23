class EZofuckCompiler:
    def __init__(self):
        self.generated_code = ""
        self.indentation_level = 0

    def compile(self, code):
        self.generated_code = ""
        self.indentation_level = 0

        self.emit_line("import sys")
        self.emit_line("tape = [0] * 30000")
        self.emit_line("ptr = 0")

        for command in code:
            if command == ".":
                self.emit_line("sys.stdout.write(chr(tape[ptr]))")
            elif command == ",":
                self.emit_line("tape[ptr] = ord(sys.stdin.read(1)[0])")
            elif command == "+":
                self.emit_line("tape[ptr] += 1")
            elif command == "-":
                self.emit_line("tape[ptr] -= 1")
            elif command == ">":
                self.emit_line("ptr += 1")
            elif command == "<":
                self.emit_line("ptr -= 1")
            elif command == "[":
                self.emit_line("while tape[ptr] != 0:")
                self.indentation_level += 1
            elif command == "]":
                self.indentation_level -= 1
                self.emit_line("")

        return self.generated_code

    def emit_line(self, line):
        indentation = "\t" * self.indentation_level
        self.generated_code += indentation + line + "\n"


# Exemple
compiler = EZofuckCompiler()
code = "+++++[>++++[>++<-]<-]>>."
compiled_code = compiler.compile(code)
print("Compiled Code:")
print(compiled_code)
