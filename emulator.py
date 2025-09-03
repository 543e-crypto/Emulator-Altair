from basic_lexer import BasicLexer
from basic_parser import BasicParser
from basic_runtime import BasicRuntime

def main():
    print("Altair BASIC Minimal Emulator")
    print("Enter your BASIC program. End input with an empty line.")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    lexer = BasicLexer(lines)
    tokenized = lexer.tokenize()
    parser = BasicParser(tokenized)
    program = parser.get_program()
    order = parser.get_sorted_lines()
    runtime = BasicRuntime(program, order)
    runtime.run()

if __name__ == "__main__":
    main()