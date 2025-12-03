f = open("Day3/input.txt", "r")
total_joltage = 0

'''
Strategy:
joltage length has to equal 12. while length is less than 12:
-> Find the largest number beginning from left to (right-spots remaining) at n location
-> number is then put in the appropriate place
-> new line begins at n+1

int and sum
'''

for line in f: 
    line = line.strip()
    joltage_line = line
    joltage_list = []
    while len(joltage_list) < 12:
        max = -1
        n = -1
        for i in range(0,(len(joltage_line) - (11 - len(joltage_list)))):
            joltage = int(joltage_line[i])
            if joltage > max:
                max = joltage
                n = i
        joltage_list.append(str(max))
        joltage_line = joltage_line[n+1:]
    joltage_list_int = int(''.join(joltage_list))
    print(f'joltage_list, {joltage_list_int}')
    total_joltage += joltage_list_int


print(f'total_joltage, {total_joltage}')

