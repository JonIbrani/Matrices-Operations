
A_matrix = []
B_matrix = []

print("This program does the addition, subtraction, and multiplication of matrices")
row_number = int(input('Enter the number of rows for both matrixs A and B:\n'))
col_number = int(input('Enter the number of columnes for both matrixs A and B:\n'))

print('Matrix A:')
for i in range(row_number):
    row = []
    for j in range(col_number):
        element_a = int(input("Enter the elements rowwise for matrix A:\n"))
        row.append(element_a)
    A_matrix.append(row)

print('Matrix B:')
for x in range(row_number):
    Row = []
    for y in range(col_number):
        element_b = int(input("Enter the elements rowwise for matrix B:\n"))
        Row.append(element_b)
    B_matrix.append(Row)

print(f'A = {A_matrix}')
print(f'B = {B_matrix}')


result_multiply = [[0 for i in range(col_number)] for j in range(row_number)]
for i in range(len(A_matrix)):
    for j in range(len(A_matrix[0])):
        result_multiply[i][j] = A_matrix[i][j] + B_matrix[i][j]
print('\nA+B:')
for i in range(row_number):
    for j in range(col_number):
        print(format(result_multiply[i][j], "<5"), end='')
    print()



result_subtract = [[0 for i in range(col_number)] for j in range(row_number)]
for i in range(len(A_matrix)):
    for j in range(len(A_matrix[0])):
        result_subtract[i][j] = A_matrix[i][j] - B_matrix[i][j]
print('\nA-B:')
for i in range(row_number):
    for j in range(col_number):
        print(format(result_subtract[i][j], "<5"), end='')
    print()


result_multiply = [[0 for i in range(col_number)] for j in range(row_number)]
for i in range(len(A_matrix)):
    for j in range(len(A_matrix[0])):
        result_multiply[i][j] = A_matrix[i][j] * B_matrix[i][j]
print('\nA*B:')
for i in range(row_number):
    for j in range(col_number):
        print(format(result_multiply[i][j], "<5"), end='')
    print()