def average(array):
    arr_set = set(array)
    sums=0
    intcount=0
    for i in (arr_set):
        sums = i+sums
        intcount +=1
    return (sums/intcount)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
