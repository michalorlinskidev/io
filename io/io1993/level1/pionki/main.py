import copy


def print_matrix(matrix):
    for row in matrix:
        print(row)


def print_result(matrix, counter, moves, desc):
    print_matrix(matrix)
    print("--------------------------------")
    print(moves)
    print("--------------------------------")
    print(counter)
    print("--------------------------------")
    print(desc)


def create_matrix(rows, cols):
    matrix = []
    size = rows * cols
    for i in range(size):
        equation = []
        for j in range(size):
            equation.append(0)
        matrix.append(equation)

    for i in range(size):
        for j in [-9, -8, -7]:
            sum = i + j
            if 0 <= sum < size and i // cols - 1 == sum // cols:
                matrix[i][i + j] = 1
        for j in [-1, 1]:
            sum = i + j
            if 0 <= sum < size and i // cols == sum // cols:
                matrix[i][i + j] = 1
        for j in [7, 8, 9]:
            sum = i + j
            if 0 <= sum < size and i // cols + 1 == sum // cols:
                matrix[i][i + j] = 1
    return matrix


def compute_matrix(matrix, result):
    compute_matrix = copy.deepcopy(matrix)
    size = len(compute_matrix)
    for i in range(size):
        compute_matrix[i].append(result[i])

    for i in range(size):
        if compute_matrix[i][i] == 0:
            for k in range(i + 1, size):
                if compute_matrix[k][i] == 1:
                    temp_row = compute_matrix[i]
                    compute_matrix[i] = compute_matrix[k]
                    compute_matrix[k] = temp_row
                    break
        for j in range(size):
            if i != j and compute_matrix[j][i] == 1:
                for k in range(size + 1):
                    compute_matrix[j][k] = (compute_matrix[j][k] + compute_matrix[i][k]) % 2

    counter = 0
    moves = []
    for i in range(size):
        counter += compute_matrix[i][size]
        if compute_matrix[i][size] == 1:
            moves.append(i)

    return compute_matrix, counter, moves


if __name__ == '__main__':

    try:
        board_black = []
        board_white = []
        with open("pio.in") as file:
            board_color = file.read().replace("\n", "")
            if len(board_color) != 64:
                raise ValueError
            for v in board_color:
                if v == 'B':
                    board_white.append(0)
                    board_black.append(1)
                else:
                    board_white.append(1)
                    board_black.append(0)

        matrix = create_matrix(8, 8)
        black_matrix, black_counter, black_moves = compute_matrix(matrix, board_black)
        white_matrix, white_counter, white_moves = compute_matrix(matrix, board_white)

        with open('pin.out', 'w') as file:
            if black_counter > white_counter:
                print_result(white_matrix, white_counter, white_moves, 'white')
                file.write(str(white_counter) + "\n")
                file.write(str(white_moves))
            else:
                print_result(black_matrix, black_counter, black_moves, 'black')
                file.write(str(black_counter) + "\n")
                file.write(str(black_moves))

    except ValueError:
        print("NONSENS")
