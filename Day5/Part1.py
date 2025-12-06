'''
fresh ingredient ID ranges (inclusive)
followed by a blank line
followed by a list of available ingredient ids

looking at the IDs a simple list is probably not going to work. Do a list of tuples to iterate through instead.
'''
total_fresh = 0

ranges = []
ingredients = []

range_flag = True

f = open("Day5/input.txt", "r")
for line in f:
    if line == '\n':
        range_flag = False
        continue
    line = line.strip()
    if range_flag is True:
        start,stop = line.split('-')
        ranges.append((int(start),int(stop)))
    else:
        line = line.strip()
        ingredients.append(int(line))


print(ranges)
print(ingredients)

for ingredient in ingredients:
    for range in ranges:
        start,stop = range
        if ingredient >= start and ingredient <= stop:
            total_fresh += 1
            break
            

print(total_fresh)



