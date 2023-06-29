      
if __name__ == '__main__':
    N = int(input())
    mlist = []
    for i in range(N):
        commd = input()
        lst = commd.split()
        if lst[0]=="insert":
            mlist.insert(int(lst[1]),int(lst[2]))
        elif lst[0]=="remove":
            mlist.remove(int(lst[1]))
        elif lst[0]=="append":
            mlist.append(int(lst[1]))
        elif lst[0]=="sort":
            mlist.sort()
        elif lst[0]=="pop":
            mlist.pop()
        elif lst[0]=="reverse":
            mlist.reverse()
        elif lst[0]=="print":
            print(mlist)
        
