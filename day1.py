inputs = []

with open('day1_input.txt', 'r') as f:
    this_input = []
    while line := f.readline():
        if line != '\n':
            this_input.append(int(line))
        else:
            inputs.append(this_input.copy())
            this_input = []

# part 1            
biggest_sum = 0
for elf in inputs:
    elf_sum = sum(elf)
    if elf_sum > biggest_sum:
        biggest_sum = elf_sum
        
print(biggest_sum)

# part 2
calorie_sum = [sum(elf) for elf in inputs]
top_three_sum = sum(sorted(calorie_sum)[-3:])
print(top_three_sum)