import numpy as np
test = np.random.randint(1,100,size=(5,5))
print(test)
print(test[1:4 , 1:4])    #only access rows n colmns from 1 to 3 
print(test[0,0:])
print(test[0: , 4])
print(np.dot(test[0,0:],test[0: , 4]))