def is_safe(values):
    differences = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    all_smallstep = all(1 <= diff <= 3 or -1 >= diff >= -3 for diff in differences)
    all_positive = all(diff > 0 for diff in differences)
    all_negative = all(diff < 0 for diff in differences)
    # print(all_positive,all_negative,all_smallstep)
    return (all_positive or all_negative) and all_smallstep

ramp = []
difference = []
counter_safe = 0

with open("input.txt", "r") as file: # Zeilen einzeln auslesen
    for line in file:
        values = [int(x) for x in line.split()]
        if is_safe(values):
                counter_safe += 1
                print("is safe")
                continue
        for i in range(len(values)):
            modified_values = values[:i] + values[i + 1:]
            print(modified_values)
            if is_safe(modified_values):
                counter_safe += 1
                print("is safe after correction")
                break
        # ramp = []
        # difference = [] 

        # for i in range(len(values)-1):
        #     ramp.append(sign(values[i+1]-values[i])) 
        #     difference.append(values[i+1]-values[i])
        
        # all_positive = all(x > 0 for x in ramp)
        # all_negative = all(x < 0 for x in ramp)
        # all_smallstep = all(1 <= x <= 3 or -1 >= x >= -3 for x in difference)
        
        # if (all_positive or all_negative) and all_smallstep:
        #     counter_safe += (all_positive or all_negative) and all_smallstep   
        
        # else:
        #     for i in range(len(values)):
        #         modified_values = values[:i] + values[i + 1:]

        #         if 
print(counter_safe)           
