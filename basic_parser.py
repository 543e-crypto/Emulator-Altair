class BasicParser:
    def __init__(self, tokenized_lines):
        self.program = {}
        for lineno, tokens, raw in tokenized_lines:
            self.program[lineno] = (tokens, raw)
        self.sorted_lines = sorted(self.program.keys())

    def get_program(self):
        return self.program

    def get_sorted_lines(self):
        return self.sorted_lines
