def sign(x): 
    return (x > 0) - (x < 0) 
ramp = []
difference = []
counter_safe = 0

with open("input.txt", "r") as file: # Zeilen einzeln auslesen

    for line in file:
        values = [int(x) for x in line.split()]
        ramp = []
        difference = [] 

        for i in range(len(values)-1):
            ramp.append(sign(values[i+1]-values[i])) 
            difference.append(values[i+1]-values[i])
        
        all_positive = all(x > 0 for x in ramp)
        all_negative = all(x < 0 for x in ramp)
        all_smallstep = all(1 <= x <= 3 or -1 >= x >= -3 for x in difference)
        

        if (all_positive or all_negative) and all_smallstep:
            counter_safe += (all_positive or all_negative) and all_smallstep   
        


        
         
    
           
print(counter_safe)           
