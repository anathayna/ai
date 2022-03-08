from player import Player
from game import Game
import os

def clear_stdout() -> None:
  os.system('cls' if os.name == 'nt' else 'clear')

# começando o jogo
def set_player(color) -> Player:
  clear_stdout()
  output_color = "brancas" if color == Player.WHITE_COLOR else "pretas"
  player_kind = input("escolha o jogador das peças " + output_color + ":\n1. bot\n2. você\n")

  is_bot = True if player_kind == "1" else False
  strategy = None

  if is_bot:
    strategy = Player.MINIMAX_STRATEGY

  return Player(color, is_bot, strategy)

# desenhando o tabuleiro
def main():
  match = Game()
  match.white_player = set_player(Player.WHITE_COLOR)
  match.black_player = set_player(Player.BLACK_COLOR)

  while True:
    clear_stdout()
    print(match)

    if match.board.is_game_over():
      break

    player = match.current_player()
    position = player.move(match.board)
    match.push(position)

if __name__ == "__main__":
    main()
