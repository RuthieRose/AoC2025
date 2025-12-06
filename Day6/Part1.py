
total = 0

problems = []

f = open("Day6/input.txt", "r")
for line in f:
    line = line.strip()
    row = line.split(' ')
    print(row)
    s = []
    for n in row:
        if len(n.strip()) > 0: 
            s.append(n)
    problems.append(s)

print(problems)

pivot = []

for i in range(0,len(problems[0])):
    problem_set = []
    for j in range(0,len(problems)):
        problem_set.append(problems[j][i])
    pivot.append(problem_set)

print(pivot)

while len(pivot) > 0:
    problem = pivot.pop()
    operand = problem.pop()
    problem_total = int(problem.pop())
    while len(problem) > 0:
        if operand == "*":
            problem_total *= int(problem.pop())
        else: 
            problem_total += int(problem.pop())
    total += problem_total


print(total)



