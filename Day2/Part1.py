f = open("Day2/input.txt", "r")

invalid_id_sum = 0

def is_invalid(num): 
    string_num = str(num)
    l = len(string_num)
    if l % 2 == 1: return False
    mid = int(l/2)
    flag = True
    for i in range(0,mid):
        if string_num[i] != string_num[i+mid]: 
            flag = False
            break
    return flag
    



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