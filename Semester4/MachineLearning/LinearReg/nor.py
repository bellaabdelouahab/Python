import numpy as np
N= lambda Data: print((Data - min(Data) )/ (max(Data) - min(Data)))
# N(np.array([25,31,12,16,17,19]))


Z= lambda att1,att2: (sum([(att1[i]-att2[i])**2 for i in range(len(att1))]))**0.5
# Z([0.9,0.33,0.26,0.36,0.35],[0,1,0.53,0.26,1])

centers = [[5.2,13,7],[5,7.25,7],[4,5.7,6]]

D = lambda x : [[Z(j,i) for i in centers] for j in x]

print(D([[2.5,12.3,11],[3.2,10,8.5],[4.5,8,7.5],[3.7,6,7.3]]))