packets = []

with open('day13_input.txt', 'r') as f:
    while line := f.readline():
        if line.strip() != '':
            packets.append(eval(line.strip()))

# part 1

def compare_lists(left, right):
    max_len = max(len(left), len(right))
    for idx in range(max_len):
        if idx < len(left) and idx < len(right):
            if type(left[idx]) == int and type(right[idx]) == int:
                if left[idx] > right[idx]:
                    return False
                elif left[idx] < right[idx]:
                    return True
            elif type(left[idx]) == list and type(right[idx]) == list:
                rec_res = compare_lists(left[idx], right[idx])
                if rec_res is not None:
                    return rec_res
            else:
                if type(left[idx]) == int:
                    left[idx] = [left[idx]]
                elif type(right[idx]) == int:
                    right[idx] = [right[idx]]
                rec_res = compare_lists(left[idx], right[idx])
                if rec_res is not None:
                    return rec_res
        elif len(left) > idx >= len(right):
            return False
        elif len(right) > idx >= len(left):
            return True
    return None

correct_pairs = 0

for idx, packets_ab in enumerate(zip(*[iter(packets)] * 2)):
    if compare_lists(*packets_ab):
        correct_pairs += idx + 1

print(correct_pairs)

# part 2
packets.append([[2]])
packets.append([[6]])

from functools import cmp_to_key

def cmp_wrapper(left, right):
    res = packet_cmp(left, right)
    print(f'Comparing: {left} and {right}\nResult: {res}')
    return res

def packet_cmp(left, right):
    left = left.copy()
    right = right.copy()
    max_len = max(len(left), len(right))
    for idx in range(max_len):
        if idx < len(left) and idx < len(right):
            if type(left[idx]) == int and type(right[idx]) == int:
                if left[idx] > right[idx]:
                    return 1
                elif left[idx] < right[idx]:
                    return -1
            elif type(left[idx]) == list and type(right[idx]) == list:
                rec_res = packet_cmp(left[idx], right[idx])
                if rec_res != 0:
                    return rec_res
            else:
                if type(left[idx]) == int:
                    left[idx] = [left[idx]]
                elif type(right[idx]) == int:
                    right[idx] = [right[idx]]
                rec_res = packet_cmp(left[idx], right[idx])
                if rec_res != 0:
                    return rec_res
        elif len(left) > idx >= len(right):
            return 1
        elif len(right) > idx >= len(left):
            return -1
    return 0

std = sorted(packets, key=cmp_to_key(packet_cmp))
div_1 = std.index([[2]]) + 1
div_2 = std.index([[6]]) + 1
print(div_1 * div_2)
