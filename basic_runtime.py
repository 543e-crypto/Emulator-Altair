class BasicRuntime:
    def __init__(self, program, sorted_lines):
        self.program = program
        self.sorted_lines = sorted_lines
        self.vars = {}
        self.current_idx = 0
        self.output = []

    def input_var(self, var_name):
        value = input(f"Input value for {var_name}: ")
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass
        self.vars[var_name] = value

    def eval_expr(self, expr):
        # Only allows variables and basic arithmetic
        for var in self.vars:
            expr = expr.replace(var, str(self.vars[var]))
        try:
            return eval(expr, {}, {})
        except Exception:
            return expr

    def run(self):
        while self.current_idx < len(self.sorted_lines):
            lineno = self.sorted_lines[self.current_idx]
            tokens, raw = self.program[lineno]
            if not tokens:
                self.current_idx += 1
                continue
            cmd = tokens[0].upper()
            if cmd == "PRINT":
                expr = raw[len("PRINT"):].strip()
                val = self.eval_expr(expr)
                print(val)
                self.output.append(str(val))
            elif cmd == "LET":
                assign = raw[len("LET"):].strip()
                if '=' in assign:
                    var, expr = assign.split('=', 1)
                    var = var.strip()
                    expr = expr.strip()
                    self.vars[var] = self.eval_expr(expr)
            elif cmd == "INPUT":
                var = tokens[1]
                self.input_var(var)
            elif cmd == "GOTO":
                target = int(tokens[1])
                if target in self.program:
                    self.current_idx = self.sorted_lines.index(target)
                    continue
            elif cmd == "END":
                break
            else:
                print(f"Unknown command: {cmd}")
            self.current_idx += 1
