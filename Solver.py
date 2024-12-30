import janus_swi as kb
import var
import random
import os
class MineSweeperSolver:
    def __init__(self):
        kb.consult(os.path.join(var.BASE_DIR,var.KB_FILE_NAME))
        self.assertions = []
        self.discovered_mines = []
        self.clicked = []
    def assert_in_kb(self,knowledge:str):
        if knowledge in self.assertions:return
        self.assertions.append(knowledge)
        query = f"asserta({knowledge})"
        kb.query_once(query)
        
    def update_knowledge(self,data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                state = data[i][j]
                if state == '-':continue
                if state == 'X':continue
                state = int(state)
                self.assert_in_kb(f"safe({j},{i})")
                self.assert_in_kb(f"clue({j},{i},{state})") 
    def ask(self,query:str):
        result = []
        q = kb.query(query)
        while True:
            answer = q.next()
            if not answer:break
            if 'truth' in answer:
                if not answer['truth']:break
                del answer['truth']
            result.append(answer)
        return result
    def generate_next_moves(self):
        kb.query_once('find_mines.')
        found_mines = False
        found_safe = False
        actions = []
        new_mines = self.ask('mine(X,Y).')
        for mine in new_mines:
            x,y = mine['X'],mine['Y']
            if (x,y) in self.discovered_mines:continue
            self.discovered_mines.append((x,y))
            actions.append(('M',x,y))
            found_mines = True
        next_actions = self.ask('action(X,Y).')
        for action in next_actions:
            x,y = action['X'],action['Y']
            if (x,y) in self.clicked:continue
            self.clicked.append((x,y))
            actions.append(('S',x,y))
            found_safe = True
        if not (found_safe or found_mines):
            while True:
                x,y = random.randint(0,8),random.randint(0,8)
                unxp = kb.query_once(f"unexplored(({x},{y}))")
                if unxp['truth']==False:continue
                actions.append(('R',x,y))
                break
        return actions
    