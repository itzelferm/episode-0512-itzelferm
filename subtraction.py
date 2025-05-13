
def subtract(subs: list[float]) -> float:
    difference = subs[0]
    for sub in subs[1:]:
        difference = difference - sub

    return difference


def describe_subtract() -> str:
    return 'Returns the difference of all of the numbers passed to it.'


if __name__ == '__main__':
    import sys

    print(describe_subtract())

    if len(sys.argv) > 1:
        subs = [float(arg) for arg in sys.argv[1:]]
        print(subtract(subs))