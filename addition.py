def add(addends: list[float]) -> float:
    sum = 0
    for addend in addends:
        sum = sum + addend

    return sum


def describe_add() -> str:
    return 'Returns the sum of all of the numbers passed to it.'


if __name__ == '__main__':
    import sys

    print(describe_add())

    if len(sys.argv) > 1:
        addends = [float(arg) for arg in sys.argv[1:]]
        print(add(addends))