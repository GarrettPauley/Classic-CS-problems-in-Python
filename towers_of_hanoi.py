""" A classic problem in which three towers (A, B, C) stand. Three disks (1,2,3) are resting on tower a. The widest 
disk (1) is at the bottom of tower A, with disks 2, and three stacked on top. The goal is to move all of the disks 
from tower A to tower C. 

The following constraints must be considered: 
 * Only one disk can be moved at a time
 * a larger disk cannot be placed on top of a smaller disk
 * The topmost disk on a tower is the only one that we can move. 

 Sound Good? Great, lets start. 
 """ 

 #model the towers. 
 # push and pop can simulate how the disks are moved between the towers. LIFO (Last in First Out). 
from typing import TypeVar, Generic, List
T = TypeVar("T")

class Stack(Generic[T]): 

    def __init__(self): 
        self.container =  [] 
    
    def push(self, item): 
        self.container.append(item)
    
    def pop(self): 
        return self.container.pop()
    def __repr__(self): 
        return repr(self.container)
    
num_of_disks = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

#place three disks on Tower a to source. 
for i in range(1,num_of_disks + 1): 
    tower_a.push(i)
#begin is our starting point, end is our destination, and temp is the tower used to hold disks as we solve the problem. 
def hanoi(source, dest, temp, n): 
    if n == 1: 
        dest.push(source.pop())
        print("tower a",tower_a)
        print("tower b",tower_b)
        print('tower c',tower_c)   
        
    else: 
        #recurion
        #move disks n-1(all disks except the bottom) from the source to the temp, using the destination as a spare
        hanoi(source, temp, dest, n-1)
        #move disks n-1(all disks except the bottom) from the source to the desk, using the temp as a spare
        #this is just one disk (the widest disk)
        hanoi(source, dest, temp, 1)
        #move disks n-1(all disks except the bottom) from the temp to the dest, using the source as a spare
        hanoi(temp, dest, source, n-1)
       

if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_of_disks)
    print(tower_a)
    print(tower_b)
    print(tower_c)      
