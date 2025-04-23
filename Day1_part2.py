def import_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    list1, list2 = [], []
    
    for line in lines:
        parts = line.strip().split()
        list1.append(parts[0])
        list2.append(parts[1])
    
    return list1, list2

file = "input_1.txt"
list1, list2 = import_data(file)

similarity = 0
for i in range(len(list1)):
    similarity += list1.count(list2[i]) * int(list2[i])

print(similarity)
