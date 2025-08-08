def stock( arr ):

    """
    Approach will be to maintain a min and max variable and return the diffrence as the profit
    """
    mi = mx = arr[0]

    for i in arr:

        if i > mx:
            mx = i
        
        if i < mi:
            mi = i
    
    return mx - mi

if __name__ == "__main__":
    arr = [1,3,2,2,4,2,5]

    print(stock(arr))