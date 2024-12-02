list1 = []
list2 = []
sum = 0
similarity_score = 0 
with open("input.txt", "r") as file: # Zeilen einzeln auslesen

    for line in file:
        values = line.split()

        list1.append(int(values[0]))
        list2.append(int(values[1]))

    
    for i in range(len(list1)):
        similarity_score += list2.count(list1[i]) * list1[i]
    
    # list1 = sorted(list1)
    # list2 = sorted(list2)
    
    # for i in range(len(list1)):
        # difference = abs(list1[i]-list2[i])
        # sum += difference


print(list1)        
print(list2)  
print(similarity_score)
