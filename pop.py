n = int(input())
s = set(map(int, input().split()))
n_operations = int(input())
for i in range(n_operations):
    str_input = input()
    words = str_input.split()
    if(words[0] == 'pop'):
        s.pop()
    elif(words[0]=='remove'):
        
        s.remove(int(words[1]))
        
    elif(words[0]=='discard'):
        s.discard(int(words[1]))
        
print(sum(s))
        
    
