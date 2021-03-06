import numpy as np

print("Numpy declaring")
print("==================================")
x = [[1,2,3], [4,5,6], [7,8,9]]
print(x)
print('- - - - - - - - - - - - - - - - -')
print('converting to matrices: ')
y = np.array(x)
print(y)
print('- - - - - - - - - - - - - - - - -')
m = np.zeros((3,2))
print(m)
print('- - - - - - - - - - - - - - - - -')
n = np.zeros((2,3))
print(n)
print('- - - - - - - - - - - - - - - - -')
print('a square matrix:')
n = np.zeros((3,3))
print(n)
print('- - - - - - - - - - - - - - - - -')
n = np.zeros((2,3)) + 5
print(n)
print('- - - - - - - - - - - - - - - - -')
print('a unity matrix in 1D:')
n = np.ones(3)
print(n)
print('- - - - - - - - - - - - - - - - -')
print('a unity matrix in 2D:')
n = np.ones((3,4))
print(n)
print('- - - - - - - - - - - - - - - - -')
print('an identity matrix, check out the diagonal! Square is implied for the diagonal, so row i and colon j are equal: ')
n = np.eye(4)
print(n)
print('- - - - - - - - - - - - - - - - -')
print('fast making of an array in 1D:')
n = np.arange(100)
print(n)
print('- - - - - - - - - - - - - - - - -')
print('fast making of an array in 1D, limited:')
n = np.arange(3,10)
print(n)
print('- - - - - - - - - - - - - - - - -')
print('fast making of an array in 2D:')
n = np.arange(50).reshape(5,10)
print(n)
print('- - - - - - - - - - - - - - - - -')
print('linearly spaced array:')
n = np.linspace(0,1)
print(n)
print('- - - - - - - - - - - - - - - - -')
print('linearly spaced array, limited to only 5 elements:')
n = np.linspace(0,10,5)
print(n)
print('- - - - - - - - - - - - - - - - -')
print('getting min and max values:')
x = [1,2,3,4,5]
x = np.array(x)
print(x)
a = x.max()
print(a)
b = x.min()
print(b)
print('- - - - - - - - - - - - - - - - -')
print('getting min and max values and index:')
x = [1,2,3,4,5]
x = np.array(x)
print(x)
a = x.max()
c = x.argmax()
print(a)
print("at index: ")
print(c)
b = x.min()
d = x.argmin()
print(b)
print("at index: ")
print(d)
print('- - - - - - - - - - - - - - - - -')
print('getting random values(between 0 and 1):')
x = np.random.rand(5)
print(x)
print('- - - - - - - - - - - - - - - - -')
print('getting random values, negatives included:')
x = np.random.randn(5)
print(x)
print('- - - - - - - - - - - - - - - - -')
print('getting random values, limited, specified range:')
x = np.random.randint(1,100)
print(x)
print("----------------------------------")
print()
print("Indexing and slicing")
print("==================================")
x = np.arange(0,21)
print(x)
print('- - - - - - - - - - - - - - - - -')
print('getting the index value: ')
y = x[8]
print(y)
z = x[-1]
print(z)
print('- - - - - - - - - - - - - - - - -')
print('slicing: ')
y = x[:10]
print(y)
z = x[10:]
print(z)
a = x[2:5]
print(a)
b = x[1:10]
print(b)
c = x[-10:-1]
print(c)
print('- - - - - - - - - - - - - - - - -')
print('slicing and changing the values: ')
y = x[5:15] = 40
print(y)
print(x)
print('- - - - - - - - - - - - - - - - -')
print('slicing and changing the values, but without mutation! ')
x = np.arange(0,21)
print(x)
y = x.copy()
print(y)
z = y[5:15] = 40
print(z)
print(y)
print("----------------------------------")
print()
print("Slicing 2D Matrix and conditional selection")
print("==================================")
x = np.arange(25).reshape(5,5)
print(x)
print('- - - - - - - - - - - - - - - - -')
print('Slicing in 2D matrix:')
print('x[i][j]')
y = x[2][2]
print(y)
z = x[4][2]
print(z)
a = x[2,2]
print(a)
b = x[4,2]
print(b)
c = x[0:2,2:]
print(c)
d = x[1:4,1:4]
print(d)
print('- - - - - - - - - - - - - - - - -')
print('Conditional selection in 2D matrix:')
x = np.arange(1,21)
print(x)
y = x[x > 12]
print(y)
print("----------------------------------")
print()
print("Operations in numpy")
print("==================================")
x = np.arange(12).reshape(3,4)
print('x = ')
print(x)
y = np.arange(10,22).reshape(3,4)
print('y = ')
print(y)
print('- - - - - - - - - - - - - - - - -')
z = x + y
print('z = x + y = ')
print(z)
print('- - - - - - - - - - - - - - - - -')
z = x * y
print("In numpy, the matrices have to be in the same order for multiplying, although it wouldn't be required mathematically: ")
print('z = x * y = ')
print(z)
print('- - - - - - - - - - - - - - - - -')
z = x.sum()
print("Just one extra example of a very commonly used method: ")
print('z = x.sum()')
print(z)
print('- - - - - - - - - - - - - - - - -')
z = np.full((3,3), True)
print("Just one extra example of a very commonly used method: ")
print('z = np.full((3,3), True)')
print(z)
print("----------------------------------")