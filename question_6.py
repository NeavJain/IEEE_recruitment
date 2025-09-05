cutoff_list = [
    ("Pilani", "CS", 327),
    ("Pilani", "Chemical", 247),
    ("Pilani", "Eco", 271),
    ("Pilani", "Bio", 236),
    ("Goa", "CS", 301),
    ("Goa", "Chemical", 239),
    ("Goa", "Eco", 263),
    ("Goa", "Bio", 234),
    ("Hyderabad", "CS", 298),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "Eco", 261),
    ("Hyderabad", "Bio", 234),
]
dict = {}
for camp , cour , cutoff in cutoff_list:
    if camp not in dict:       #adds campus dictionary if not present eg.pilani
        dict[camp]={}
    dict[camp][cour]=cutoff    #adds course and cutoff
print(dict)


    

