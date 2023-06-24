if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    #print(arr)
    max_element=max(arr)
   # print(max_element)
    while(max_element == arr[-1]):
        arr.remove(arr[-1])
    #print(arr)
    print(max(arr))

