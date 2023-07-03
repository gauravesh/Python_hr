def split_and_join(line):
    x=line.split()
    join = '-'.join(x)
    return join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
