def import_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    list1, list2 = [], []

    for line in lines:
        parts = line.strip().split()
        list1.append(parts[0])
        list2.append(parts[1])
    
    return list1, list2

def sort(list): 
    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list 

def distance(x1, x2):
    return abs(x1 - x2)

file = "input_1.txt"
list1, list2 = import_data(file)

list1 = sort(list1)
list2 = sort(list2)

distances = 0
n = len(list1)
for i in range(n):
    distances += distance(int(list1[i]), int(list2[i]))

print(distances)