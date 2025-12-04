f = open("Day4/input.txt", "r")
total_rolls = 0

grid = []

'''
1. set up a grid system
2. have a utility that looks at all 8 positions around a paper and totals
'''

def utility(b,a):
    print(f'coordinates are {a},{b}')
    rolls = 0
    # upper left diagonal
    if b-1 >= 0 and a-1 >= 0:
        if grid[b-1][a-1] == 1:
            print(f'upper left is a roll')
            rolls += 1
    # upper center
    if b-1 >= 0: 
        if grid[b-1][a] == 1:
            print(f'upper center is a roll')
            rolls += 1
    # upper right diagonal
    if a+1 < len(grid[0]) and b-1 >= 0:
        if grid[b-1][a+1] == 1:
            print(f'upper right is a roll')
            rolls += 1
    # left
    if a-1 >= 0:
        if grid[b][a-1] == 1:
            print(f'left is a roll')
            rolls += 1
    # right
    if a+1 < len(grid[0]): 
        if grid[b][a+1] == 1:
            print(f'right is a roll')
            rolls +=1 
    # lower left diagonal
    if a-1 >= 0 and b+1 < len(grid):
        if grid[b+1][a-1] ==1:
            print(f'lower right is a roll')
            rolls += 1
    # lower center
    if b+1 < len(grid):
        if grid[b+1][a] ==1:
            print(f'lower center is a roll')
            rolls += 1
    # lower right diagonal
    if b+1 < len(grid) and a+1 < len(grid[0]):
        if grid[b+1][a+1] == 1:
            print(f'lower right is a roll')
            rolls += 1
    return rolls


for line in f: 
    line = line.strip()
    print(line)
    l = []
    for c in line:
        if c == '.':
            l.append(0)
        else: 
            l.append(1)
    grid.append(l)

print(grid)

for b in range(0,len(grid)):
    for a in range(0,len(grid[0])):
        if grid[b][a] ==1:
            r = utility(b,a)
            if r <= 3:
                print(f'coordinates are {a},{b}')
                print(f'total is less than 3')
                total_rolls += 1
   
print(f'total is {total_rolls}')