import re

def arithmetic_arranger(problems, calculate=False):
    # error for to many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # preparing initial variables
    rex = re.compile(r'^[0-9]{1,4}$')
    possible_operators = ["+", "-"]
    formated = []

    # creating a string formatting function for final result
    def format(first, operator, second, calculate):
        x = int(first)
        y = int(second)
        r = x + y if operator == '+' else x - y
        base = r if r > 0 else 0 - r
        n = max([len(first), len(second), len(str(base))]) if calculate else max(
          [len(first), len(second)])

        r = str(r)
        n += 2  # for the op and a space
        res = [first.rjust(n), operator + " " + second.rjust(n - 2), '-' * n]
        if calculate:
              res.append(r.rjust(n))
        return res

    # assigning the variables for the arguments in the problem
    for problem in problems:
        [first, operator, second] = problem.split()

        if operator not in possible_operators:
              return "Error: Operator must be '+' or '-'."

        if rex.match(first) is None or rex.match(second) is None:
              return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
              return "Error: Numbers cannot be more than four digits."

        formated.append(format(first, operator, second, calculate))

    # final formatting
    ff = formated[0]
    spaces = " " * 4
    for p in formated[1:]:
        for i in range(0, len(ff)):
            ff[i] += spaces + p[i]
            
    if not calculate:
        ff = ff[0:3]

    return '\n'.join(ff)
