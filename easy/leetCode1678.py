#1678. Goal Parser Interpretation
def interpret(command):
    result = command.replace("()", "o")
    result = result.replace("(al)","al")
    print(result)


interpret("G()(al)")
interpret("G()(al)")
interpret("G()(al)")
interpret("G()(al)")