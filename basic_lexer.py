import re

class BasicLexer:
    def __init__(self, source_lines):
        self.source_lines = source_lines

    def tokenize(self):
        tokenized_lines = []
        for line in self.source_lines:
            line = line.strip()
            if not line:
                continue
            match = re.match(r'^(\\d+)\s+(.*)$', line)
            if match:
                lineno, code = match.groups()
                tokens = code.strip().split()
                tokenized_lines.append((int(lineno), tokens, code.strip()))
        tokenized_lines.sort(key=lambda x: x[0])
        return tokenized_lines
