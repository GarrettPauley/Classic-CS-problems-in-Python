from csp import Constraint, CSP
from typing import Dict, List, Optional

if __name__ == "__main__": 
    columns: List[int] = [1,2,3,4,5,6,7,8] 
    rows: Dict[int, List[int]] = {}
    for column in columns: 
        rows[column] = [1,2,3,4,5,6,7,8] 
    csp: CSP[int, int] = CSP(columns, rows) 

class QueensConstraint(Constraint[int, int]): 
    def __init__(self, columns: List[int]) -> None: 
        super().__init__(columns)
        self.columns: List[int] = columns

    def satisfied(self, assignment: Dict[int, int]) -> bool: 
        #q1c = queen 1 column, q1r = queen 1 row (Q to a1)
        for q1c, q1r in assignment.items():
        #q2c = queen 2 column 
            for q2c in range(q1c + 1, len(self.columns) + 1): 
                if q2c in assignment: 
                    q2r: int = assignment[q2c] #q2r = queen 2nd row 
                    if q1r == q2r: #same row? 
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c): #same diagonal
                        return False
        return True

csp.add_constraint(QueensConstraint(columns))
solution: Optional[Dict[int, int]] = csp.backtracking_search()
if solution is None: 
    print("No Solution found") 
else: 
    print(solution)