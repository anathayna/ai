import chess
from player import Player

class Game():
  # escolhendo como vão aparecer as peças no tabuleiro
  UNICODE_WHITE = {
    chess.PAWN: "\u2659",
    chess.ROOK: "\u2656",
    chess.KNIGHT: "\u2658",
    chess.BISHOP: "\u2657",
    chess.QUEEN: "\u2655",
    chess.KING: "\u2654"
  }

  UNICODE_BLACK = {
    chess.PAWN: "\u265F",
    chess.ROOK: "\u265C",
    chess.KNIGHT: "\u265E",
    chess.BISHOP: "\u265D",
    chess.QUEEN: "\u265B",
    chess.KING: "\u265A"
  }

  def __init__(self) -> None:
    self.board = chess.Board()
    self.last_move = None
    self.white_player = None
    self.black_player = None

  # definindo os headers
  def __str__(self) -> str:
    headers = self.formatted_previous_turn() + self.formatted_player_turn()
    return headers + self.unicode_formatted_board() + self.formatted_endgame_message()

  # atualizando o tabuleiro c/ os movimentos posíveis/válidos
  def push(self, movement) -> None:
    self.last_move = movement.uci()
    self.board.push(movement) if movement in self.board.legal_moves else None

  def current_player(self) -> Player:
    return self.white_player if self.is_white_turn() else self.black_player

  def formatted_player_turn(self) -> str:
    player = "brancas" if self.is_white_turn() else "pretas"
    return "rodada das " + player + "\n\n"

  def formatted_previous_turn(self) -> str:
    if self.last_move == None:
      return ""
    player = "pretas" if self.is_white_turn() else "brancas"
    return player + " jogou " + self.last_move + "\n\n"

  def formatted_endgame_message(self) -> str:
    outcome = self.board.outcome()
    if outcome == None:
      return ""
    if outcome.winner == chess.WHITE:
      winner = "brancas"
    elif outcome.winner == chess.BLACK:
      winner = "pretas"
    else:
      winner = "empate"
    return "\nxeque-mete. " + winner + " ganhou das " + str(outcome.termination)

  def is_white_turn(self) -> bool:
    return self.board.turn == chess.WHITE

  # editando as posições do tabuleiro
  def unicode_formatted_board(self) -> str:
    pieces = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for square in chess.SQUARES:
      piece = self.board.piece_at(square)
      if not piece:
        pieces.append(".")
      elif piece.color == chess.BLACK:
        pieces.append(Game.UNICODE_WHITE[piece.piece_type])
      else:
        pieces.append(Game.UNICODE_BLACK[piece.piece_type])
    rows = [" ".join([str(i//8)] + pieces[i:i+8]) for i in range(0, len(pieces), 8)]
    board = "\n".join(rows)
    return board
