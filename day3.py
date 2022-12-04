import string

rucksacks = []
with open('day3_input.txt', 'r') as f:
    while line := f.readline():
        rucksacks.append(line.strip())

priorities = {letter: priority for letter, priority in zip(
    string.ascii_lowercase + string.ascii_uppercase,
    list(range(1, 53))
)}
    
# part 1
total_priorities = 0

for rucksack in rucksacks:
    first_comp = rucksack[:len(rucksack) // 2]
    second_comp = rucksack[len(rucksack) // 2:]
    wrong_item = set(first_comp) & set(second_comp)
    assert len(wrong_item) == 1
    total_priorities += priorities[wrong_item.pop()]

print(total_priorities)

# part 2
total_priorities = 0

for elf1, elf2, elf3 in zip(*[iter(rucksacks)] * 3):
    wrong_item = set(elf1) & set(elf2) & set(elf3)
    assert len(wrong_item) == 1
    total_priorities += priorities[wrong_item.pop()]

print(total_priorities)