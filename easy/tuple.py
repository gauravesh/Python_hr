if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # Create a tuple from the integer_list
    integer_tuple = tuple(integer_list)
    
    # Compute the hash value of the tuple
    hash_value = hash(integer_tuple)
    print(hash_value)
