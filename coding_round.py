"""
Question : we are given a string consist of numbers and a key value,
 we have to return the count of partition we can make so that the sum of each partition is 
 less than the key value.

 So our approach will be to take the elements one by one and add it untill the sum is less than the key itself
 then store in array if it becomes larger, then again traverse the result array and check if the sum is less than the key
 or not if not then return -1 else return the length of the array. this will be our output and the time complexity will be
 O(n)
"""

def count_String_partition(S,key):

    temp = s = 0
    result = []

    for i in range(len(S)):

        temp = temp*10 + int(S[i])

        if temp <= key:
            s = temp
        else:
            if( s == 0):
                s = temp//10

            result.append(s)
            temp = s = 0
            temp = temp*10 + int(S[i])

    result.append(temp)

    print(result)

    psum = 0
    for i in range(len(result)):
        psum += result[i]

    if psum <= key:
        return len(result)
    else:
        return -1
    


if __name__ == "__main__":

    St = "1213"
    key = 999

    print(count_String_partition(St,key))