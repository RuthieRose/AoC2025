f = open("Day2/input.txt", "r")

invalid_id_sum = 0

'''
Scenarios: 

1. Invalid: Length is odd. 1 number is repeated for the entire length.
2. Valid: Length is odd. 1 number is not repeated for the entire length.
3. Invalid: Length is even. 1 number is repeated for the entire length.
4. Valid: Length is even. No numbers are repeated for the entire length.
5. Invalid: Length is even. 2 numbers are repeated twice
6. Invalid: Length is even. 3 numbers are repeated twice
7. Invalid: Length is even. 4 numbers are repeated twice
8. Invalid: Length is even. 5 numbers are repeated twice
9. Invalid: Length is odd. 3 number repeated 3 times
10. Invalid: Length is even. 2 numbers are repeated 2, 3 or 4 times


Check for l is odd and then check for all nums being the same. After:
For efficiency, count backward since likely most of them will already just be the doubled number

'''

def is_invalid(num): 
    string_num = str(num)
    l = len(string_num)
    if l == 1: return False
    # check for even or odd length
    # scenarios 1 and 2
    flag = True
    if l % 2 == 1:
        for i in range(0,l-1):
            if string_num[i] != string_num[i+1]:
                flag = False
        if flag == True: 
            return flag
         # scenario 9
        if l == 9:
            flag = True
            for i in range(0,3):
                if string_num[i] != string_num[i+3]:
                    flag = False
                if string_num[i] != string_num[i+6]:
                    flag = False
            if flag == True:
                return flag
        return False

    # even length. check for repeating numbers starting at the midpoint
    # scenarios 5,6,7 and 8

    mid = int(l/2)
    # start by halving it
    flag = True
    for i in range(0,mid):
        if string_num[i] != string_num[i+mid]: 
            flag = False
    if flag == True: 
        return flag

    # scenario 3
    flag = True
    for i in range(0,l-1):
        if string_num[i] != string_num[i+1]:
            flag = False
    if flag == True:
        return flag
    
    # scenario 10
    if l > 2:
        pairs = [(0,2),(1,3),(2,4),(3,5),(4,6),(5,7),(6,8),(7,9)]
        flag = True
        for i in range(0,8):
            a = pairs[i][0]
            b = pairs[i][1]
            if a < l and b < l:
                if string_num[a] != string_num[b]:
                    flag = False
        if flag == True:
            return flag
        
    return False

    



for line in f: 
    line = line.strip()
    invalid_id_list = line.split(',')
    print(invalid_id_list)
    for id_range in invalid_id_list:
        start_range, stop_range = id_range.split('-')
        start_range = int(start_range)
        stop_range = int(stop_range)
        print(start_range, stop_range)
        for i in range(start_range, stop_range+1):
            if is_invalid(i):
                invalid_id_sum += i
                print(i, ' is invalid')

print(invalid_id_sum)