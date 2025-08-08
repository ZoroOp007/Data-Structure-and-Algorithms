def duplicate(arr):

    # O(n) and also n space 
    hash_map = {} 
    duplicates = []

    for i in arr:

        if i not in hash_map:
            hash_map[i] = 1
        else:
            duplicates.append(i)
    
    return duplicates

if __name__ == "__main__":

    arr = [2,15,6,2,3,4,5,3,4]

    result = duplicate(arr)

    print(result)