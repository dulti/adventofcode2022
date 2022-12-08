from functools import reduce
from itertools import accumulate
import operator

# input - build a tree!
fs = {'/': {}}
current_dir = ['/']

def fs_read(fs, path):
    return reduce(operator.getitem, path, fs)
    
def fs_write(fs, path, new):
    fs_read(fs, path[:-1])[path[-1]] = new

with open('day7_input.txt', 'r') as f:
    while line := f.readline().strip():
        if line.startswith('$'):
            args = line.split(' ')
            if args[1] == 'cd':
                path = args[2]
                if path == '/':
                    current_dir = ['/']
                elif path == '..':
                    current_dir.pop()
                else:
                    current_dir.append(path)
                    
        elif line.startswith('dir'):
            _, dir = line.split(' ')
            # if the dir was not seen before, add it
            if dir not in fs_read(fs, current_dir).keys():
                fs_write(fs, current_dir + [dir], {})
        else:
            size, name = line.split(' ')
            # if the file was not seen before, add it and write size
            if name not in fs_read(fs, current_dir).keys():
                fs_write(fs, current_dir + [name], int(size))
                
# part 1
dir_sizes = {}
def get_dirs_size(fs, path):
    dir_content = fs_read(fs, path).keys()
    for element in dir_content:
        if type(size := fs_read(fs, path + [element])) == int:
            # is file
            # add all sizes
            # store in flat structure with full path as key
            for dir in list(accumulate([el] for el in path)): 
                # add this size to each dir
                dir_sizes[tuple(dir)] = dir_sizes.get(tuple(dir), 0) + size
        else:
            # is dir, just call it on the dir
            get_dirs_size(fs, path + [element])

get_dirs_size(fs, ['/'])      

# now find small dirs (<= 1e5) and add them up
total_size = sum([size for _, size in dir_sizes.items() if size <= 1e5])
print(total_size)

# part 2
total_space = 7e7
free_space = total_space - dir_sizes[tuple(['/'])]

smallest_suitable_size = float('inf')

for dir, size in dir_sizes.items():
    if free_space + size > 3e7 and size < smallest_suitable_size:
        smallest_suitable_size = size
        
print(smallest_suitable_size)