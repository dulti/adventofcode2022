assignment_pairs = []
with open('day4_input.txt', 'r') as f:
    while line := f.readline():
        pairs = line.strip().split(',')
        pair = [pairs[0].split('-'), pairs[1].split('-')]
        pair_proper = [list(range(int(elf[0]), int(elf[1]) + 1)) for elf in pair]
        assignment_pairs.append(pair_proper)

# part 1
# when a pythonist is bored with the simple tasks they begin to make one-line solutions

total_nested = sum([
    1 if set(elf1).issubset(set(elf2)) or set(elf1).issuperset(set(elf2)) 
      else 0 
      for elf1, elf2 in assignment_pairs
])
      
print(total_nested)

# part 2

total_overlapping = sum([
    1 if len(set(elf1) & set(elf2)) > 0 else 0
    for elf1, elf2 in assignment_pairs
])

print(total_overlapping)
    