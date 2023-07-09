def count_substring(string, sub_string):
    c=0
    for i in range(0,len(string)):
        modify=string[i:len(sub_string)+i]
        #print(modify)
        if (modify==sub_string):
           #print(sub_string)
           c=c+1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count) 
