def get_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = [line.strip() for line in file.readlines()]
    return data

def count_xmas(grid):
    """
    Count the occurences of the word "MAS" and its reverse "SAM" in a "X" shape.

    The search is done by checking the center of the "X" shape for 'A',
    and then checking the four arms of the "X" shape for 'M' and 'S'.
    The arms are checked in pairs to account for both "XMAS" and "SAMX".

    """    
    n = len(grid)
    m = len(grid[0])
    count = 0

    for i in range(1, n-1):  
        for j in range(1, m-1): 
            # Check if the center of the "X" is 'A'
            if grid[i][j] == 'A':
                # Check top-left to bottom-right "MAS" (and "SAM" reversed)
                if (grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S') or (grid[i+1][j+1] == 'M' and grid[i-1][j-1] == 'S'):
                    # Check top-right to bottom-left "MAS" (and "SAM" reversed)
                    if (grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M') or (grid[i+1][j-1] == 'S' and grid[i-1][j+1] == 'M'):
                        count += 1

    return count

file = "input_4.txt"
data = get_data(file)

result = count_xmas(data)
print(result)
