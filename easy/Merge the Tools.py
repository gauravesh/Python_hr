def merge_the_tools(string, k):
    # your code goes here

    

    length_string = len(string)
    div_len = length_string//k
    sub_strings=[]

    #lets make substrings


    for i in range(div_len):
        sub_strings.append(string[(i)*k:(i+1)*k])

    clean_sub_strings=[]

    for j in sub_strings:
        new_string = j[0]
        dist_ele=[]  # Initialize new_string with the first character of the substring
        for i in range(1, k):  # Start the loop from 1
            if j[i] not in new_string:  # Only add the character if it's different from the previous one
                new_string += j[i]
        clean_sub_strings.append(new_string)
    
        
    for i in clean_sub_strings:
        print(i)
            




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
