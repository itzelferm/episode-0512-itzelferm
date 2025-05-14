
def decrement(number: list[float]) -> float:
    answer = number[0] - 1

    return answer


def describe_decrement() -> str:
    return 'Returns the answer of the number decreased by 1.'


if __name__ == '__main__':
    import sys

    print(describe_decrement())

    if len(sys.argv) > 1:
        number = [float(arg) for arg in sys.argv[1:]]
        print(decrement(number))