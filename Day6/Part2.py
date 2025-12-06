
total = 0

problems = []

f = open("Day6/input.txt", "r")
for line in f:
    row = line.strip('\n')
    problems.append(row)

operands = problems.pop()
operands_list = operands.split()

pivot = []

working_num = ''
working_set = []

for i in range(0,len(problems[0])):
    for j in range(0,4):
        if problems[j][i] != ' ':
            working_num = working_num + problems[j][i]
    working_set.append(working_num)
    working_num = ''
    if problems[0][i] == ' ' and problems[1][i] == ' ' and problems[2][i] == ' ' and problems[3][i] == ' ':
        # this is a break in the problem
        # append to pivot
        working_set.append(operands_list.pop(0))
        pivot.append(working_set)
        working_set = []
working_set.append(operands_list[0])
pivot.append(working_set)
print(pivot)

while len(pivot) > 0:
    problem = pivot.pop()
    problem = [elem for elem in problem if elem != '']
    operand = problem.pop()
    problem_total = int(problem.pop())
    while len(problem) > 0:
        if operand == "*":
            problem_total *= int(problem.pop())
        else: 
            problem_total += int(problem.pop())
    total += problem_total

print(total)



