
def parse_number(value):
    if len(value) != 6:
        raise ValueError
    return float(value)


def binary_search(table, value):
    left_index = 0
    right_index = len(table)
    index = 0
    while left_index != right_index - 1:
        index = (left_index + right_index) // 2
        if value < table[index]:
            left_index = index
        else:
            right_index = index

    return index


if __name__ == "__main__":
    result = ""
    with open("spo.in") as file:
        try:
            values = file.read().replace("\n", " ").split(" ")
            if len(values) == 0:
                raise ValueError
            elif len(values) == 1:
                result = 100
            else:
                counter = 0
                table = [parse_number(values[0])]

                for value in values[1:]:
                    number = parse_number(value)
                    if number < table[counter]:
                        counter += 1
                        table.append(number)
                    else:
                        position = binary_search(table, number)
                        table[position] = number
                result = (counter+1)*100
                print(table)
                print(counter)
        except ValueError:
            result = "NONSENS"

    with open('spo.out', 'w') as file:
        file.write(str(result))
    print(result)
