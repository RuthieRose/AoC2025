zeroes = 0
place = 50
print("the dial starts at 50")


f = open("Day1/input.txt", "r")
o = open("Day1/output.txt", "a") 


for line in f: 
    line = line.strip()
    dir = line[0]
    steps = line[1:]
    steps = int(steps)
    pointer = place
    

    '''
    Scenarios

    1. Dir is R. At Upper Bound. 

    2. Dir is R. Not at Upper Bound.

    3. Dir is L. At Lower Bound.

    4. Dir is L. Not at Lower Bound. 

    Take one step at a time. A reset counts as one step.


    '''

    while steps > 0:
        
        # Scenario 1
        if pointer == 99 and dir == 'R':
            pointer = 0
            steps -= 1
        
        # Scenario 2
        elif dir == 'R':
            steps -= 1
            pointer += 1

        # Scenario 3
        elif dir == 'L' and pointer == 0:
            pointer = 99
            steps -= 1

        # Scenario 4
        elif dir == 'L': 
            pointer -= 1
            steps -= 1


    if pointer == 0: 
        zeroes += 1


    place = pointer
        
    print('final spot for ', line, ' place: ', place, file=o)


print(zeroes)
        

