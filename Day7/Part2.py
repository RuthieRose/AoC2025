
total = 0

grid = []

f = open("Day7/sample.txt", "r")

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

condensed = []
paths = []


for line in grid:
    if '^' in line or 'S' in line:
        condensed.append(line)
        paths.append([0]*len(line))


for line in condensed:
    print(''.join(line))

for i in range(0,len(condensed)):
    for j in range(0,len(condensed[i])):
        path = 0
        char = condensed[i][j]
        if i == 0:
            if char == 'S':
                path += 1
        elif i == 1:
            if j > 0 and condensed[i-1][j-1] == 'S':
                    path += paths[i-1][j-1]
            if j < len(condensed[i])-1 and condensed[i-1][j+1] == 'S':
                    path += paths[i-1][j+1]
        elif char == '|':
            if condensed[i-1][j] == '|':
                path += paths[i-1][j]             
            if j > 0:
                if condensed[i][j-1] == '^':
                    path += paths[i-1][j-1]
            if j < len(condensed[i])-1:
                if condensed[i][j+1] == '^':
                    path += paths[i-1][j+1]
        paths[i][j] = path


for line in paths:
    print(line)

total = sum(paths[-1])
print(total)





