

def product_ex_self(arr):

    zero_count = 0
    zero_index = -1

    product = 1

    for i in range(len(arr)):

        if arr[i] == 0:
            zero_count += 1
            zero_index = i
        else:
            product *= arr[i]

    result = [0]*len(arr)

    if zero_count == 0:
        for i in range(len(arr)):
            result[i] = product // arr[i]
    elif zero_count == 1:
        result[zero_index] = product

    return result



if __name__ == "__main__":

    arr = [2,1,4,2,0,7,3]

    print(product_ex_self(arr))