def get_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = [line.strip() for line in file.readlines()]
    return data

def count_xmas(grid):
    """
    Count the occurrences of the word "XMAS" and its reverse "SAMX" in a grid.
    The search is done in all 8 possible directions: horizontal, vertical, and diagonal.

    """
    n = len(grid)
    m = len(grid[0])
    count = 0

    def check_positions(start_i, start_j, di, dj):
        word = "".join(grid[start_i + k * di][start_j + k * dj] for k in range(4))
        return word

    # Search horizontal (normal and reversed)
    for i in range(n):
        for j in range(m - 3):  
            if grid[i][j:j+4] == "XMAS":
                count += 1
            if grid[i][j:j+4] == "SAMX":
                count += 1

    # Search vertical (normal and reversed)
    for j in range(m):
        for i in range(n - 3):  
            vertical_word = "".join(grid[i+k][j] for k in range(4))
            if vertical_word == "XMAS":
                count += 1
            if vertical_word == "SAMX":
                count += 1

    # Search diagonal (top-left to bottom-right and reversed)
    for i in range(n - 3):
        for j in range(m - 3):
            diagonal_word = "".join(grid[i+k][j+k] for k in range(4))
            if diagonal_word == "XMAS":
                count += 1
            if diagonal_word == "SAMX":
                count += 1

    # Search diagonal (top-right to bottom-left and reversed)
    for i in range(n - 3):
        for j in range(3, m):
            diagonal_word = "".join(grid[i+k][j-k] for k in range(4))
            if diagonal_word == "XMAS":
                count += 1
            if diagonal_word == "SAMX":
                count += 1

    return count

file = "input_4.txt"
data = get_data(file)

result = count_xmas(data)
print(result)