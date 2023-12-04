def print_matrix(matrix):
    for index in matrix:
        print(index)


def play():
    matrix = [["0.0", "0.1", "0.2"],
              ["1.0", "1.1", "1.2"],
              ["2.0", "2.1", "2.2"]]
    count = 9
    print_matrix(matrix)
    while count > 0:
        print("Введите поочередно номер строки и столбца, на пересечении которых будет крестик 'X'")
        line_us = int(input("Номер строки: "))
        column_us = int(input("Номер столбца: "))
        if line_us < 0 or line_us > 2 or column_us < 0 or column_us > 2:
            print("Некорректные значения. Введите номер строки и столбца от 0 до 2.")
            continue
        if matrix[line_us][column_us] != "X" and matrix[line_us][column_us] != "0":
            matrix[line_us][column_us] = "X"
            count -= 1
            print_matrix(matrix)
        else:
            print("Это поле уже занято. Введите другие значения.")
            continue

        if count == 0:
            print("Игра закончена")
            break

        print("Введите поочередно номер строки и столбца, на пересечении которых будет крестик '0'")
        line_us = int(input("Номер строки: "))
        column_us = int(input("Номер столбца: "))
        if line_us < 0 or line_us > 2 or column_us < 0 or column_us > 2:
            print("Некорректные значения. Введите номер строки и столбца от 0 до 2.")
            continue
        if matrix[line_us][column_us] != "X" and matrix[line_us][column_us] != "0":
            matrix[line_us][column_us] = "0"
            count -= 1
            print_matrix(matrix)
        else:
            print("Это поле уже занято. Введите другие значения.")
            continue


play()