f = open("Day3/input.txt", "r")
total_joltage = 0

'''
Strategy:
Find the largest number beginning from left to right-1 at n location
Find the second largest number from n + 1
int and sum
'''

for line in f: 
    line = line.strip()
    max = -1
    second_max = -1
    print(line)
    n = -1
    
    for i in range(0,len(line)-1):
        joltage1 = int(line[i])
        if joltage1 > max: 
            max = joltage1
            n = i
    for j in range(n+1,len(line)):
        joltage2 = int(line[j])
        if joltage2 > second_max:
            second_max = joltage2
    
    joltage_rating = f'{max}{second_max}'
    total_joltage += int(joltage_rating)
    print(f'joltage_rating {joltage_rating}')


print(f'total_joltage is {total_joltage}')