is_logging = True


def set_logging(val):
    global is_logging
    is_logging = val


def log(*args):
    global is_logging
    if is_logging:
        print_str = ""
        for s in args:
            print_str += str(s)
        print(print_str)
