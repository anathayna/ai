# problema do Caixeiro-Viajante 
# que é chamado do Problema de Roteamento de Veículos 
# ou Vehicle Routing Problem (VRP)

# sequência de locais que podemos chamar de 0, 1, 2, 3, 4, ..., até N
# o local 0 (zero) é o local da padaria de onde as vans saem e chegam. 

# desejável: menor rota possível
# nó = gene | indivíduo = conjunto de genes = rota

import random, math, numpy as np

def create_data_model():
    data = {}
    data['distance_matrix'] = [
        [ 0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354, 468, 776, 662 ], 
        # exemplo: entre 0 e 1, temos distância de 548.
        [ 548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674, 1016, 868, 1210 ],
        [ 776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164, 1130, 788, 1552, 754 ],
        [ 696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822, 1164, 560, 1358 ],
        [ 582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708, 1050, 674, 1244 ],
        [ 274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628, 514, 1050, 708 ],
        [ 502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856, 514, 1278, 480 ],
        [ 194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320, 662, 742, 856 ],
        [ 308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662, 320, 1084, 514 ],
        [ 194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388, 274, 810, 468 ],
        [ 536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764, 730, 388, 1152, 354 ],
        [ 502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114, 308, 650, 274, 844 ],
        [ 388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194, 536, 388, 730 ],
        [ 354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0, 342, 422, 536 ],
        [ 468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536, 342, 0, 764, 194 ],
        [ 776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274, 388, 422, 764, 0, 798 ],
        [ 662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730, 536, 194, 798, 0 ],
    ] # cada array contém 17 elementos no total
    data['num_vehicles'] = 4
    data['depot'] = 0
    return data


  
# hiperparâmetros
tamanho_populacao = 100
tx_mutacao = 0.50
tx_crossover = 0.15
tx_tragedia = 0.05
geracoes_max = 100_000
geracoes_tragedia = 100



data = create_data_model()
individuos = data['distance_matrix']
vans = data['num_vehicles']



individuo_a = individuos[0]
individuo_b = individuos[1]
individuo_c = individuos[2]
individuo_d = individuos[3]
individuo_e = individuos[4]
individuo_f = individuos[5]
individuo_g = individuos[6]
individuo_h = individuos[7]
individuo_i = individuos[8]
individuo_j = individuos[9]
individuo_k = individuos[10]
individuo_l = individuos[11]
individuo_m = individuos[12]
individuo_n = individuos[13]
individuo_o = individuos[14]
individuo_p = individuos[15]
individuo_q = individuos[16]



# gerar o individuo: veículo com uma sequência de entrega
# função fitness: tentar encontrar a melhor sequência
# função de mutação: sugestão fazer o flip (random.choices)
# função cross-over: cruzar os indivíduos (verificar se vale a pena fazer p/ esse problema, se não vai piorar)
# função tragédia: verificar se vale fazer nesse problema
# função seleção: seleciona/clasifica um sequência e enviar p/ as funções de mutação de cross-over
# finaliza com o while/loop até achar o melhor caso (importante: critério de parada (qtd de gerações/limite:1000))

# pegar o número de nós do problema
# pegar o número do nó que representa o ponto de origem



'''

mesma quilometragem por dia e pudessem carregar aproximadamente a mesma quantidade carga entre elas para quem nenhuma equipe ficasse sobrecarregada

dada uma quantidade de N de vans e as distâncias entre os pontos de entrega, deve gerar:

- Genes e indivíduos: o que é um indivíduo neste problema? R: pontos de entrega
- Função de fitness: como saber a qualidade de um conjunto de rotas
- Função de mutação: como mudar a ordem das cidades e entre as vans
- Função de crossover: como trocar genes entre os indivíduos

e será necessário testar taxas de mutação, crossover e quantidade de indivíduos que sobrará em cada geração.

- Função de Seleção: aplicar a Seleção por tragédia depois de 1000 gerações
- Função de Mutação: testar mais de um tipo de mutação. qual é a taxa ideal de mutação? outros valores melhoram ou pioram?
- Função de Cross-Over: qual é a taxa ideal de cross-over? outros valores melhoram ou pioram?

===========

SAÍDA
Van 1:
2 → 5 → 3

Van 2: 
4 → 6 → 1

===========

'''