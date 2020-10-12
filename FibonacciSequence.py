from typing import Generator 
"""Start with the base cases of the fibonacci sequence "0 and 1" store these 
in a dictionary. if the number based to fib2 is not in the dict, create a new slol for it, store it,
and return it. """
memory = {0:1, 1:1}
def fib2(n):
    if n not in memory: 
        memory[n] = fib2(n-1) + fib2(n-2)
    return memory[n]
    
        

if __name__ == "__main__":
    print(fib2(50))