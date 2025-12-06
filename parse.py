def parse_arg(arg):

    if len(arg) == 64:
        return arg
    if arg.isdigit() or arg[1:].isdigit():
        return int(arg)
    
    return arg