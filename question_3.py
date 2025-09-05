import numpy as np
test = np.random.randint(1,100,size=(5,5))    #randomly creates 2d array of 5x5
print(test)
print(np.mean(test))   
print(np.max(test))
print(np.min(test))
test = test.reshape(1,25)      #changes it to 1x25
test = np.sort(test)      
print(test)



