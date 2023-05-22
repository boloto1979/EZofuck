class EZofuckInterpreter:
    def __init__(self):
        self.cells = [0]
        self.pointer = 0

    def interpret(self, code):
        output = ""
        loop_stack = []

        i = 0
        while i < len(code):
            command = code[i]

            if command == ".":
                output += chr(self.cells[self.pointer])
            elif command == ",":
                self.cells[self.pointer] = ord(input("Input a character: ")[0])
            elif command == "+":
                self.cells[self.pointer] += 1
            elif command == "-":
                self.cells[self.pointer] -= 1
            elif command == ">":
                self.pointer += 1
                if self.pointer >= len(self.cells):
                    self.cells.append(0)
            elif command == "<":
                self.pointer -= 1
                if self.pointer < 0:
                    self.pointer = 0
            elif command == "[":
                if self.cells[self.pointer] == 0:
                    loop_count = 1
                    while loop_count > 0:
                        i += 1
                        if code[i] == "[":
                            loop_count += 1
                        elif code[i] == "]":
                            loop_count -= 1
                else:
                    loop_stack.append(i)
            elif command == "]":
                if self.cells[self.pointer] != 0:
                    i = loop_stack[-1]
                else:
                    loop_stack.pop()

            i += 1

        return output
    
# Example of use
interpreter = EZofuckInterpreter()
code = "+++++[>++++[>++<-]<-]>>."
output = interpreter.interpret(code)
print("Output:", output)
