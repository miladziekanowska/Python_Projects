def arithmetic_arranger(problems: list, solve = False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_value = []
    second_value = []
    operator = []
    lengths = []
    separator_len = []
    separator = []
    result = []

    for operation in problems:
        first_value.append(operation.split(" ")[0])
        operator.append(operation.split(" ")[1])
        second_value.append(operation.split(" ")[2])

    for i in first_value:
        if len(i) > 4:
            print("Error: Numbers cannot be more than four digits.")

    for i in second_value:
        if len(i) > 4:
            print("Error: Numbers cannot be more than four digits.")

    for i in operator:
        if i == "+" or i == "-":
            continue
        else:
            print("Error: Operator must be '+' or '-'.")

    for i in first_value:
        try:
            i = int(i)
        except:
            print("Error: Numbers must only contain digits.")

    for i in second_value:
        try:
            i = int(i)
        except:
            print("Error: Numbers must only contain digits.")

    for v in range(0, len(first_value)):
        if operator[v] == "+":
            result.append(str(int(first_value[v]) + int(second_value[v])))
            lengths.append((len(first_value[v]), len(second_value[v])))
            separator_len.append(max(lengths[v]) + 2)
            separator.append("-" * separator_len[v])
        else:
            result.append(str(int(first_value[v]) - int(second_value[v])))
            lengths.append((len(first_value[v]), len(second_value[v])))
            separator_len.append(max(lengths[v]) + 2)
            separator.append("-" * separator_len[v])

    for v in range(0, len(first_value)):
        if v != len(first_value) - 1:
            top = first_value[v].rjust(separator_len[v] + 1) + "    "
            middle = operator[v] + second_value[v].rjust(separator_len[v] - 1) + "    "
            line = separator[v] + "    "
            bottom = result[v].rjust(separator_len[v]) + "    "
        else:
            top = first_value[v].rjust(separator_len[v] + 1)
            middle = operator[v] + second_value[v].rjust(separator_len[v] - 1)
            line = separator[v]
            bottom = result[v].rjust(separator_len[v])



    print(first_value)
    print(operator)
    print(second_value)
    print(result)
    print(separator)
