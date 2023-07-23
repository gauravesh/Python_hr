def print_rangoli(n):
    vari = ord('a')+n
    if (n==1):
        print("a")
        return

    for i in range(1, n + 1):
        # Print spaces before the numbers
        print("-" * (2*(n - i)), end="")

        # Print the first half of the row in ascending order
        for j in range(1, i + 1):
            print(chr(vari-j), end='-')


        # Print the second half of the row in descending order
        for j in range(i - 1, 0, -1):
            if(j == 1 and i == n):
               print(chr(vari - j), end='')
            else:
                print(chr(vari-j), end='-')

        print("-" *((2* (n - i))-1))

    for i in range(n - 1, 0, -1):
        # Print spaces before the numbers
        print("-" * (2*(n - i)), end="")

        # Print the first half of the row in ascending order
        for j in range(1, i + 1):
            print(chr(vari-j), end='-')

        # Print the second half of the row in descending order
        for j in range(i - 1, 0, -1):

             print(chr(vari-j), end='-')


        print("-" * ((2*(n - i))-1))


n = 1  # Change this value to adjust the number of rows
print_rangoli(n)

