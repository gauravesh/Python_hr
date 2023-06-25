if __name__ == '__main__':
    stu = []
    record = []
    for _ in range(int(input())):
        name = input()
        stu.append(name)
        score = float(input())
        stu.append(score)
        record.append(stu)
        stu=[]
        
 #finding the min value
    
 
#print(record)
    min_value= min(record, key=lambda x: x[1])
    min_col = min_value[1]
#removing all min value
    new_list = [sub_list for sub_list in record if sub_list[1] != min_col]
    
#print(new_list)
#finding second lowest value
    min_second= min(new_list, key=lambda x: x[1])
    min_2_col = min_second[1]
#print(min_2_col)
#creating list for it 
    final_list = [s_list for s_list in new_list if s_list[1] == min_2_col]
# print(final_list)
    
    x_list=[]
    for sublist in final_list:
        first_element = sublist[0]
        x_list.append(first_element)
   # print(x_list)
#sorting list
    x_list.sort()
    for a in x_list:
        print(a)
  
   
           
            
    
    
