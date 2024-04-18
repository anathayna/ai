import numpy as np
from minimax import melhor_jogada_agente


class JogoHex():
  VAZIO = 0
  HUMANO = 1
  AGENTE = 2


  def __init__(self, tamanho=5, tabuleiro=None):
    self.tamanho = tamanho
    self.tabuleiro = tabuleiro if tabuleiro is not None else np.zeros((tamanho, tamanho), dtype=int)


  
  def jogo_valido(self, posicao):
    x, y = posicao
    return 0 <= x < self.tamanho and 0 <= y < self.tamanho



  def turno(self, jogador):
    if jogador == self.HUMANO:
        return self.AGENTE
    return self.HUMANO

  

  def venceu(self, jogador):
    for i in range(self.tamanho):
        movimento = (0, i) if jogador == self.HUMANO else (i, 0)
        if self.chegou_ao_oposto(jogador, movimento, {}):
            return True
    return False



  def chegou_ao_oposto(self, jogador, movimento, visitado):
    if not self.contem_jogador(movimento, jogador) or (movimento in visitado and visitado[movimento]):
      return False

    if self.esta_na_borda(jogador, movimento):
      return True

    visitado[movimento] = True

    for n in self.vizinhos(movimento):
      if self.chegou_ao_oposto(jogador, n, visitado):
        return True

    return False



  def contem_jogador(self, coordenadas, jogador):
    return self.tabuleiro[coordenadas] == jogador

  
  
  def esta_na_borda(self, jogador, movimento):
    (x, y) = movimento
    return (jogador == self.HUMANO and x == self.tamanho - 1) or (jogador == self.AGENTE and y == self.tamanho - 1)



  def vizinhos(self, coordenadas):
    (x, y) = coordenadas
    vizinhos = []
    if x - 1 >= 0: vizinhos.append((x-1, y))
    if x + 1 < self.tamanho: vizinhos.append((x+1, y))
    if x - 1 >= 0 and y + 1 <= self.tamanho - 1: vizinhos.append((x-1, y+1))
    if x + 1 < self.tamanho and y - 1 >= 0: vizinhos.append((x+1, y-1))
    if y + 1 < self.tamanho: vizinhos.append((x, y+1))
    if y - 1 >= 0: vizinhos.append((x, y-1))
    return vizinhos


  
  def converter_jogada(self, jogada):
    jogada = jogada.strip()
    if len(jogada) < 2 or len(jogada) > 3:
      return (-1, -1)

    if not jogada[0].isalpha() or not jogada[1:].isdigit():
      return (-1, -1)

    caractere = ord(jogada[0].lower()) - ord('a')
    return (caractere, int(jogada[1:]))

  

  def jogada_valida(self):
    return self.tabuleiro[self.x] == self.HUMANO



  def colocar_peca(self, coordenadas, jogador):
    if self.jogo_valido(coordenadas) and self.tabuleiro[coordenadas] == self.VAZIO:
        self.tabuleiro[coordenadas] = jogador
        return True
    return False


  
  def capturar_jogada_agente(self):
    jogada = melhor_jogada_agente(self)
    self.colocar_peca(jogada, self.AGENTE)


  
  def espaco_disponivel(self):
    result = np.where(self.tabuleiro == self.VAZIO)
    return list(zip(result[0], result[1]))


  
  def calcular_utilidade(self, jogador):
    if self.venceu(jogador) and self.HUMANO == jogador:
      return -1
    elif self.venceu(jogador) and self.HUMANO != jogador:
      return 1
    else:
      return 0


  
  def imprimir(self):
    colunas = "   " + " ".join(chr(y + ord('a')) for y in range(self.tamanho))
    divisao_cima = "  " + "-" * (self.tamanho * 2 + 2)

    linhas = []
    for y in range(self.tamanho):
      row = " " * (y - len(str(y)) + 1) + str(y) + " \\ "
      for x in range(self.tamanho):
        jogador = self.tabuleiro[x][y]
        if jogador == self.HUMANO:
          row += "0 "
        elif jogador == self.AGENTE:
          row += "X "
        else:
          row += ". "
      row += "\\ "
      linhas.append(row)

    divisao_baixo = " " * (self.tamanho + 2) + ("-" * (self.tamanho * 2 + 2)) + "\n"

    linhas = "\n".join(linhas)
    tabuleiro_final = f"{colunas}\n{divisao_cima}\n{linhas}\n{divisao_baixo}"
    print(tabuleiro_final)
