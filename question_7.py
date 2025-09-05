l1 = [4,7,2,5,46,76,23,76,9,4]
l2 = [54,65,76,23,4,7,85,24,86,4]
l3=[]
for element in l1:
    for element2 in l2:
        if element==element2: #checks for equality
            l3.append(element) # adds to new list
l3 = list(dict.fromkeys(l3))    #creates new dictionary and then converts back to list , cuz dictionary cant have dupicate items
print(l3)