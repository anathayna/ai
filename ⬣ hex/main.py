from jogo_hex import JogoHex

if __name__ == "__main__":
  jogo = JogoHex()
  print(jogo.imprimir())

  while True:
    jogada = input("faça sua jogada: ")
    movimento = jogo.converter_jogada(jogada)
    
    while not jogo.colocar_peca(movimento, jogo.HUMANO):
      print("jogada inválida! tente novamente")
      jogada = input("faça sua jogada: ")
      movimento = jogo.converter_jogada(jogada)
    
    if jogo.venceu(jogo.HUMANO):
      print("\n")
      print(jogo.imprimir())
      print("\nhumano venceu!")
      break

    jogo.capturar_jogada_agente()
    print("\n")
    print(jogo.imprimir())

    if jogo.venceu(jogo.AGENTE):
      print("\ncomputador venceu!")
      break
