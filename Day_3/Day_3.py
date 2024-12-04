import re                                   # import regex
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"     #r als Präfix für raw string -> \ wird nicht interpretiert
total_sum = 0 


with open("input.txt", "r") as file:    # Zeilen einzeln auslesen
    content = file.read()               #init als ein string
    matches = re.findall(pattern, content)  #regular expression search (regex)

    # do dont nutzen indem man den stringt durchließt bis ein do dont kommt und dann abh vom enable Wert drauf addiert oder nicht 

    for match in matches:

        x,y = map(int,match)    #transform matches into int x,y 

        total_sum += x * y

print(total_sum)           