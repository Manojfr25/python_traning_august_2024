import numpy as np

vector = np.arange(5)
print('Vector:', vector)
print("Vector shape:", vector.shape)

matrix = np.ones([3, 2])
print("Matrix:", matrix)
print("Matrix shape:", matrix.shape)

tensor = np.zeros([2, 3, 3])
print("Tensor:", tensor)
print("Tensor shape:", tensor.shape)

print(tensor[0][1][1])


data1=np.array([1,2,3,4,5,6,])
data2=np.array([0,2,3,4,7,8])
data = np.stack((data1,data2),axis=0)
print(data)
