"""Three missionaries and three cannibals are on the west bank of a river. 
They have a canoe that can hold two people, and they all must cross the east bank of the river. 
There may never be more cannibals than missionaries on either side of the river, 
or the cannibals will...well, you can probably guess what will happen. 
Also, the canoe must have at least one person on board to cross the river. 
What sequence of crossings will successfully take the entire part across the river?  
M = Missionaries 
C = Cannibals""" 

from __future__ import annotations
from typing import List, Optional 
from generic_search import bfs, Node, node_to_path

MAX_NUM: int = 3 

class MCState: 
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None: 
        self.wm:  int = missionaries #west bank M's
        self.wc: int = cannibals # west bank C's 
        self.em: int = MAX_NUM - self.wm # east bank M's 
        self.ec: int = MAX_NUM - self.em# east bank C's 
        self.boat: bool = boat
    def __str__(self) -> str: 
        return ("On the west bank there are {} missionaries and {} cannibals. \n" "On the east bank there are {} missionaries and {} cannibals. \n" "The boat is on the {}").format(self.wm, self.wc, self.em, self.ec, ("west" if self.boat else "east"))
    def goal_test(self) -> bool: 
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM #the test did not violate the restrictions, and the all M's and C's crossed to the east side
    
    @property
    def is_legal(self) -> bool: 
        if self.wm < self.wc and self.wm > 0: 
            return False 
        if self.em < self.ec and self.em > 0: 
            return False 
        return True

    def successors(self) -> List[MCState]: 
        """All combinations of adding and subtracting M's and C's """
        sucs: List[MCState] = [] 
        if self.boat: #boat is on the west bank 
            if self.wm > 1: 
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0: 
                sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1: 
                sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
            if self.wc > 1: 
                sucs.append(MCState(self.wm, self.wc - 1, not self.boat))

            if(self.wc > 0) and (self.wm > 0): 
                sucs.append(MCState(self.wm - 1, self.wc - 1, not self.boat))
        else: #boat is on the east bank 
            if self.boat: #boat is on the west bank 
                if self.em > 1: 
                    sucs.append(MCState(self.em + 2, self.ec, not self.boat))
                if self.em > 0: 
                    sucs.append(MCState(self.em + 1, self.ec, not self.boat))
                if self.ec > 1: 
                    sucs.append(MCState(self.em, self.ec + 2, not self.boat))
                if self.ec > 1: 
                    sucs.append(MCState(self.em, self.ec + 1, not self.boat))

                if(self.ec > 0) and (self.em > 0): 
                    sucs.append(MCState(self.em + 1, self.ec + 1, not self.boat))
        return [x for x in sucs if x.is_legal]

def display_solution(path: List[MCState]): 
    if len(path) == 0: #sanity check 
        return 
    old_state : MCState = path[0]
    print(old_state)
    for current_state in path[1:]: 
        if current_state.boat: 
            print("{} missionaries and {} cannibals moved from the east to the west bank.\n".format(old_state.em - current_state.em, old_state.ec - current_state.ec))
        else: 
            if current_state.boat: 
                print("{} missionaries and {} cannibals moved from the west to the east bank.\n".format(old_state.wm - current_state.wm, old_state.wc - current_state.wc))
        print(current_state)
        old_state = current_state

if __name__ == "__main__": 
    start: MCState = MCState(MAX_NUM, MAX_NUM, True)
    solution: Optional[Node[MCState]] = bfs(start, MCState.goal_test, MCState.successors)
    if solution is None: 
        print("No solution found") 
    else: 
        path: List[MCState] = node_to_path(solution) 
        display_solution(path)