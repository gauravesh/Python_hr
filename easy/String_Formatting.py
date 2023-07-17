def print_formatted(number):
    space = len(bin(number)[2:])
    for i in range(1, number+1):
        decimal = str(i).rjust(space)
        octal = str(oct(i)[2:]).rjust(space)
        hexadecimal = str(hex(i)[2:]).upper().rjust(space)
        binary = str(bin(i)[2:]).rjust(space)
        
        print(decimal, octal, hexadecimal, binary)



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
