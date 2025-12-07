
total = 0

grid = []

f = open("Day7/sample.txt", "r")

# grid setup

for line in f:
    line = line.strip()
    line = list(map(str,line))
    grid.append(line)

#first pass
for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        char = grid[i][j]
        if char == 'S':
            grid[i+1][j] = '|'
        elif char == '^':
            #check above
            if grid[i-1][j] == "|":
                if j > 0: 
                    grid[i][j-1] = "|"
                if i < len(grid) - 1 and j > 0:
                    grid[i+1][j-1] = "|"
                if j < len(grid) - 1:
                    grid[i][j+1] = "|"
        elif char == '|':
            #add it below
            if i < len(grid) - 1:
                if grid[i+1][j] == ".":
                    grid[i+1][j] = "|"
    print(i,grid[i])

#second pass
for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        char = grid[i][j]
        if char == "^":
            if grid[i-1][j] == '|':
                total+= 1


print(total)


