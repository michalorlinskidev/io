from enum import Enum
from decimal import *


class Result(Enum):
    TRUE = "TAK"
    FALSE = "NIE"
    INVALID = "NONSENS"

    def __str__(self):
        return str(self.value)


def parse_number(number):
    number_components = number.split('/')
    if len(number_components) < 2:
        raise ValueError
    return Decimal(int(number_components[0])) / Decimal(int(number_components[1]))


if __name__ == '__main__':
    result = Result.TRUE

    with open('tkt.in') as file:
        try:
            for line in file:
                numbers = line.strip().split(" ")
                if len(numbers) < 3:
                    raise ValueError
                init = sorted(map(lambda x: parse_number(x), numbers[:3]))

                minimum1 = init[0]
                minimum2 = init[1]
                maximum = init[2]

                for i in range(3, len(numbers)):
                    value = parse_number(numbers[i])
                    if value < minimum2:
                        if value < minimum1:
                            minimum2 = minimum1
                            minimum1 = value
                        else:
                            minimum2 = value
                    elif value > maximum:
                        maximum = value

                if minimum1 + minimum2 <= maximum:
                    result = Result.FALSE
                    break
        except ValueError:
            result = Result.INVALID

    with open('tkt.out', 'w') as file:
        file.write(str(result))
    print(result)
