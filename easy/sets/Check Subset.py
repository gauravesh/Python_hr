# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases_number=int(input())
def check_subset(f_list,s_list):
    #edge cases no f_list, no s_list
    
    if len(f_list) > len(s_list):
        return False
    for _ in (f_list):
        if _ not in s_list:
            return False
        s_list.remove(_)
    return True
    
    
for _ in range((test_cases_number)):
    numberElements_A = int(input())
    Elements_A= list(map(int,input().split()))
    
    numberElements_B = int(input())
    Elements_B= list(map(int,input().split()))
    
    print(check_subset(Elements_A,Elements_B))
    
