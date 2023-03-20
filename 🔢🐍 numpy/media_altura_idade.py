import numpy as np

# descubra a média de altura de quem nasceu entre 1998 e 2005.
# ambos os arquivos têm o mesmo tamanho e estão relacionados pelo índice. Use o índice de um em outro.

altura = np.loadtxt('altura.txt')
idade = np.loadtxt('idade.txt')

range_idade = np.where(idade>1997)
