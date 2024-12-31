from solver import MineSweeperSolver
from interface import MineSweeperInterface
import time
interface = MineSweeperInterface()
solver = MineSweeperSolver()
while interface.get_game_state()=='Playing':
    solver.update_knowledge(interface.parse_elements())
    moves = solver.generate_next_moves()
    for move in moves:
        action,x,y =move[0],move[1],move[2]
        if action in ('S','R'):
            interface.click_on_cell(x,y)
input()