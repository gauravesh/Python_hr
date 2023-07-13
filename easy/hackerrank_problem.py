rows,cols = map(int, input().split())

arr = [['' for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        if j >= (cols // 2) - i and j <= (cols // 2) + i and i < rows // 2:
            arr[i][j] = '.|.'
        if j >= (cols // 2) - (rows - i - 1) and j <= (cols // 2) + (rows - i - 1) and i >= rows // 2:
            arr[i][j] = '.|.'
        if i == rows // 2:
            arr[i][j] = ''
        if j == cols // 2 and i == rows // 2:
            arr[i][j] = 'WELCOME'

new_array = []
for row in arr:
    new_array.append(''.join(row))
    #print((''.join(row)).center(cols))

for current_row in range(rows):
    while len(new_array[current_row]) != cols:
        new_array[current_row] = '-' + new_array[current_row] + '-'

for row in new_array:
    print(row)
