
for i in range(6,0,-1):     #outer loop to change line
    
        for j in range(0,i):   #to print spaces at beginning in decreasing order
            print(" ",end="")
        for k in range(0,7-i):   # prints & in increasing order
                print("&",end="")
        print()
    