
def pop_n(elems, n):
    popped = []
    for i in range(0, n):
        if len(elems) > 0:
            popped.append(elems.pop())

    return popped
