def melhor_jogada_agente(jogo, profundidade_maxima = 3):
  melhor_valor = float("-inf")
  melhor_jogada = -1
  for proximo_jogo in jogo.espaco_disponivel():
    utilidade = minimax_alfabeta(jogo, False, jogo.AGENTE)
    if utilidade > melhor_valor:
      melhor_valor = utilidade
      melhor_jogada = proximo_jogo
  return melhor_jogada



def minimax_alfabeta(jogo,
                     turno_max,
                     jogador,
                     profundidade_maxima=3,
                     alfa=float("-inf"),
                     beta=float("inf")):

  if profundidade_maxima == 0 or jogo.venceu(jogo.turno(jogador)):
    return jogo.calcular_utilidade(jogo.turno(jogador))

  if turno_max:
    for proximo_jogo in jogo.espaco_disponivel():
      utilidade = minimax_alfabeta(jogo, False, jogo.turno(jogador), profundidade_maxima - 1, alfa, beta)
      alfa = max(utilidade, alfa)
      if alfa >= beta:
        break
      return alfa

  else:
    for proximo_jogo in jogo.espaco_disponivel():
      utilidade = minimax_alfabeta(jogo, True, jogo.turno(jogador), profundidade_maxima - 1, alfa, beta)
      beta = min(utilidade, beta)
      if beta <= alfa:
        break
      return beta
