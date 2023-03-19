import numpy as np
from numpy import random

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim) # 0 dim
print(b.ndim) # 1 dim
print(c.ndim) # 2 dim
print(d.ndim) # 3 dim
print(c.shape) # (2, 3)
print(d.shape) # (2,2,3)

##############################################################

x = [1,2,3]
e = np.asarray(x)
print(e)

##############################################################

np.zeros(2) # array de 2 zeros
np.ones(2) # array de 2 uns
np.empty(2) # conteúdo randômico, dependente na memória
# np.random(3) # realmente randômico
np.arange(4) # de 0 a 4
np.linspace(0, 10, num=5) # de 0 a 10, divididos em 5 elementos

##############################################################

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5o elemento da primeira linha: ', arr[1, 4])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

##############################################################

f = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(f) # cópia ordenanda

##############################################################

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a, b))
# array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
np.concatenate((x, y), axis=1) # concatenar pelas linhas 

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
np.concatenate((x, y), axis=0) # concatenar pelas colunas 

##############################################################

g = np.array([1,2,3])
x = g.copy()

##############################################################

data = np.array([1, 2, 3])
data[1] # 2
data[0:2] # array([1, 2])
data[1:] # array([2, 3])

##############################################################

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])
five_up = (a >= 5)
print(a[five_up])
# And e Ou: & |
c = a[(a > 2) & (a < 11)]
print(c)
# Não zeros
b = np.nonzero(a < 5)
print(b)

##############################################################

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.where(arr%2 == 1) # retorna apeas os índices

##############################################################

data = np.array([1, 2])
ones = np.ones(2, dtype=int)
data + ones
# array([2, 3])
data - ones
# array([0, 1])
data * data
# array([1, 4])
data / data
# array([1., 1.])
# sum, max, min, sum
a.sum()
# valores únicos
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19,
20])
print(np.unique(a))

##############################################################

x=random.randint(100, size=(5)) # 5 inteiros até 100
x = random.rand(5) # 5 floats
x = random.rand(3, 5) # 3 linhas com 5 colunas
x = random.choice([3, 5, 7, 9]) # escolhe 1 aleatoriamente
x = random.choice([3, 5, 7, 9], size=(3, 5)) # escolhe 1 aleatoriamente - 3 linhas com 5 colunas
print(x)

##############################################################

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)) # p probabilidades, 100 itens

##############################################################

a = np.array([1,2,3,4,5])
np.savetxt('learn_numpy_out.txt',a) # salva em uma arquivo com cada conteúdo em uma linha
b = np.loadtxt('learn_numpy_out.txt')
print(b)