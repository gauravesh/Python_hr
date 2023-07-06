if __name__ == '__main__':
    s = input()
    a = [False]*5
    for i in s:
        if (i.isalnum() == True):
            a[0]=True
        if (i.isalpha() == True):
            a[1]=True
        if (i.isdigit() == True):
            a[2]=True
        if (i.islower() == True):
            a[3]=True
        if (i.isupper() == True):
            a[4]=True
    
        
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])
