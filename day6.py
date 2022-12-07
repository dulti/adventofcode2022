# input
with open('day6_input.txt', 'r') as f:
    datastream = f.readline().strip()
    
# part 1
for idx in range(0, len(datastream) - 4):
    four_char = datastream[idx:idx + 4]
    if len(set(four_char)) == len(four_char):
        print(idx + 4)
        break

# part 2
for idx in range(0, len(datastream) - 14):
    four_char = datastream[idx:idx + 14]
    if len(set(four_char)) == len(four_char):
        print(idx + 14)
        break