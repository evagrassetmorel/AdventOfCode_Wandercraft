def import_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    data = []

    for line in lines:
        numbers = line.strip().split()
        data.append([int(nb) for nb in numbers])

    return data

def check_data(data):
    """
    Checks the safety of the data by verifying if each report is sorted 
    (either ascending or descending) and if the difference between 
    consecutive elements in a report is within the range [1, 3].

    Parameters:
    data (list of lists): A list containing reports, where each report 
                          is a list of integers.

    Returns:
    int: The safety score.
    
    """
    safety = 0
    
    for report in data:
        sorted_report = sorted(report)
        if sorted_report == report or sorted_report[::-1] == report:
            
            difference = 0
            for i in range(len(report) - 1):
                if 1 <= abs(report[i]-report[i + 1]) <= 3:
                    difference += 1
            if difference == len(report) - 1:
                safety += 1

    return safety

file = "input_2.txt"
data = import_data(file)

safety = check_data(data)
print(safety)

