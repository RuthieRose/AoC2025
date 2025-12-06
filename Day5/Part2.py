'''
fresh ingredient ID ranges (inclusive)
followed by a blank line
followed by a list of available ingredient ids

'''
total_fresh = 0

fresh = []

range_flag = True

f = open("Day5/input.txt", "r")
o = open("Day5/output.txt", "w")

for line in f:
    if line == '\n':
        range_flag = False
        continue
    line = line.strip()
    if range_flag is True:
        start,stop = line.split('-')
        start = int(start)
        stop = int(stop)
        
        fresh.append((start,stop))

    if range_flag is False:
        break  
    
fresh.sort()
condensed = [fresh.pop(0)]

i = 0

while len(fresh) > 0:
    start,stop = fresh.pop(0)
    prev_start,prev_stop = condensed[i]
    print(f'-----------------------------------------------------------', file=o)
    print(f'PREVIOUS SET IS start {prev_start} stop {prev_stop}',file=o)
    print(f'STARTING WITH start {start} stop {stop}',file=o)
    if start > prev_stop: 
        print(f'ADDING AS IS start {start} stop {stop}',file=o)
        condensed.append((start,stop))
        i += 1

    elif start >= prev_start and start <= prev_stop and stop > prev_stop:
        start = prev_stop + 1
        print(f'ADDING CONDENSED start {start} stop {stop}',file=o)
        condensed.pop()
        condensed.append((prev_start,stop))

    else: print(f'SKIPPED start {start}, stop {stop}',file=o)
    print(f'-----------------------------------------------------------', file=o)

for a in condensed:
    start,stop = a
    total_fresh += ((stop - start) + 1)
    print(f'start {start} stop {stop} fresh_count {stop - start + 1} total fresh {total_fresh}', file=o)


print(total_fresh)


