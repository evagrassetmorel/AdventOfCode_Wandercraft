import re

def extract_patterns(file_path):
    """
    Extracts patterns from the file and returns a list of tuples
    containing the numbers from the 'mul' function calls.

    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = []

    for line in lines:
        matches = re.findall(r"mul\((\d+),(\d+)\)", line)
        data.extend(matches)  
    
    return data

file = "input_3.txt"
data = extract_patterns(file)

sum = 0
for item in data:
     sum += int(item[0]) * int(item[1])

print(sum)