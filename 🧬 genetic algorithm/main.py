import random
import math

# população = lista de indivíduos
# indivíduo é a solução do problema

senha_correta = ";/?h6fAdfd4,.fgSKYRfg6 5jY5W%@77f }gjnbn -49#$@#%%$&*&*"

# domínio
CARACTERES = "abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !?@#$%ˆ&*()-=+[];:,.<>/?~\{\}\\|_"

# hiperparâmetros/magic numbers
tamanho_populacao = 100
tx_mutacao = 0.50
tx_crossover = 0.15
tx_tragedia = 0.05
geracoes_max = 100_000
geracoes_tragedia = 100

def fitness(senha): # acerto = fitness
  score = 0
  for i in range(len(senha_correta)):
    if senha_correta[i] == senha[i]: score += 1
  return score

def gerar_individuo(): # gera_senha_aleatoria
  senha = ""
  for i in range(len(senha_correta)):
    senha += random.choice(CARACTERES) # gene = cada caractere
  return senha

# mutação c/ taxa
def mutacao(populacao):
  populacao_escolhida = random.choices(populacao, k=math.ceil(tx_mutacao*len(populacao)))
  return [mutacao_flip(individuo) for individuo in populacao_escolhida]

# mutação trocando valor de gene p/ um gene aleatório
def mutacao_flip(individuo): # mutação = muda_um
  novo_individuo = list(individuo) # nova_senha = novo indivíduo
  index = random.randint(0, len(individuo) - 1)
  novo_individuo[index] = random.choice(CARACTERES) # mutando gene | caracter = gene
  return "".join(novo_individuo)

def crossover(populacao, geracao):
  populacao_crossover = []
  funcao_decaimento_crossover = 1 # math.exp(-geracao/200)
  qtd = funcao_decaimento_crossover*tx_crossover*len(populacao)
  populacao_escolhida = random.choices(populacao, k=math.ceil(qtd))
  [1, 2, 3, 4]
  for i in range(len(populacao_escolhida) - 1):
    for j in range(i+1, len(populacao_escolhida)):
      ind1 = populacao_escolhida[i]
      ind2 = populacao_escolhida[j]

      index = random.randint(0, len(senha_correta) - 1)
      populacao_crossover.append(ind1[0:index] + ind2[index:])
      populacao_crossover.append(ind2[0:index] + ind1[index:])

  return populacao_crossover

# seleção dos indivíduos mais aptos (não funcionou muito p/ selecionar as melhores senhas)
def selecao_com_tragedia(populacao, geracao):
  nova_populacao = sorted(populacao, key=fitness, reverse=True)
  if (geracao % geracoes_tragedia == 0):
    tamanho_tragedia = math.ceil(tamanho_populacao*tx_tragedia)
    novos_individuos = [gerar_individuo() for _ in range(0, tamanho_populacao - tamanho_tragedia)]
    return nova_populacao[0:tamanho_tragedia] + novos_individuos
  else:
    return nova_populacao[0:tamanho_populacao]

def selecao(populacao, geracao):
  nova_populacao = sorted(populacao, key=fitness, reverse=True)
  return nova_populacao[0:tamanho_populacao]

individuo = gerar_individuo() # indivíduo = senha
populacao = [gerar_individuo() for _ in range(0, tamanho_populacao)]
populacao = sorted(populacao, key=fitness, reverse=True) # ordenar população
geracao = 0

while fitness(populacao[0]) != len(senha_correta) and geracao < geracoes_max:
  geracao += 1
  populacao_mutada = mutacao(populacao)
  populacao_crossover = crossover(populacao, geracao)
  populacao = selecao(populacao_mutada + populacao + populacao_crossover, geracao)
  if geracao % 100 == 0 or (geracao % 10 == 0 and geracao < 100):
    print("------ intermediário: " + str(geracao) + " ------")
    print("senha:" + populacao[0])
    print("taxa de acerto: " + str(fitness(populacao[0])))

print("------ final: " + str(geracao) + " ------")
print("senha:" + populacao[0])
print("taxa de acerto: " + str(fitness(populacao[0])))

# build & run: python3 main.py
