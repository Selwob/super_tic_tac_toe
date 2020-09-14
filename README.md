# super_tic_tac_toe
Python version of Tic-Tac-Toe where every square contains a smaller Tic-Tac-Toe game.

Super Tic-Tac-Toe(TTT) rules - There is one large 9 square grid with each grid square containing a smaller TTT
board. The aim of the game is to win the larger grid by getting three in a row. You can win an individual square of the
large grid by winning the smaller TTT game inside it. Therefore you need to win at least three smaller games of TTT to
win the large game. Player 1 starts by choosing any of the smaller games and making a move (X or O). Player 2 then
makes their move but must play on the smaller game positioned in the larger game grid which corresponds to that of the
position Player 1 played in the first small game grid.

e.g. P1 plays X in the top-middle position of the game in the top left of the large game grid. P2 must then play on the
top-middle game of the large game grid, although they can play any space within that game. If a small game is won and
no more moves are possible in that small game, a player who has to play there for their move can choose to play in any
small game of their choosing.
