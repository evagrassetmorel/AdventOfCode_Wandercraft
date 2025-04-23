def import_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = []

    for line in lines:
        numbers = line.strip().split()
        data.append([int(nb) for nb in numbers])

    return data

def is_safe(report):
    """
    Checks the safety of the data by verifying if each report is sorted 
    (either ascending or descending) and if the difference between 
    consecutive elements in a report is within the range [1, 3].

    Parameters:
    report (list): A list of integers.

    Returns:
    bool: True if the report is safe, False otherwise.

    """
    safety = 0
    
    sorted_report = sorted(report)
    if sorted_report == report or sorted_report[::-1] == report:

        for i in range(len(report) - 1):
            if not (1 <= abs(report[i]-report[i + 1]) <= 3):
                return False
        return True
    
    return False


def check_data(data):
    """
    Checks the safety of the data by using the is_safe function.

    If a report is not safe, it checks if removing one element makes it safe.

    Parameters:
    data (list of lists): A list containing reports, where each report 
                          is a list of integers.

    Returns:
    int: The safety score.

    """
    safety = 0

    for report in data:
        if is_safe(report):
            safety += 1
        
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                if is_safe(modified_report):
                    safety += 1
                    break

    return safety

file = "input_2.txt"
data = import_data(file)

safety = check_data(data)
print(safety)