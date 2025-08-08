def two_sum(arr , target):
    
    hash_map = {}

    for ele in arr:
        hash_map[ele] = target - ele

    print(hash_map)

    for key in hash_map:
        if hash_map[key] != key and  hash_map[key] in hash_map:
            print(hash_map[key] , key)
        
    

if __name__ == "__main__":

    arr = [10,-1,-2,-3,12]
    target = -3

    two_sum(arr,target)