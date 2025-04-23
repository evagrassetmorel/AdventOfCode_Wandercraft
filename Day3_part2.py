import re

def extract_patterns(file_path):
    """
    Extracts patterns from the file and returns a list of tuples
    containing the numbers from the 'mul' function calls.

    The function also handles the 'do()' and 'don't()' tokens to determine
    whether to include the 'mul' tokens in the output list.
    The 'do()' token activates the inclusion of 'mul' tokens, while the
    'don't()' token deactivates it.

    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        tokens = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", content)
        
        data = []
        
        active = True
        for token in tokens:
            if token == "don't()":
                active = False
            elif token == "do()":
                active = True
            elif token.startswith("mul") and active:
                data.append(token[4:-1].split(","))
    
    return data

file = "input_3.txt"
data = extract_patterns(file)

sum = 0
for item in data:
     sum += int(item[0]) * int(item[1])

print(sum)