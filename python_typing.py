from typing import Any, List, Sequence, Tuple, TypeVar, Generic
from enum import IntEnum, Enum
#Exploring Generics 
T = TypeVar('T')

#create a stack with a Generic Type, this Stack could hold anything! When we instatiate the Stack, we can specify the type
class Stack(Generic[T]):
    def __init__(self) -> None: 
        self.items: list[T] = [] 

    def push(self, item: T) -> None: 
        self.items.append(item)
    def pop(self) -> T: 
        return self.items.pop()
    def empty(self) -> bool: 
        return not self.items


GenericStack = Stack[Any]()
GenericStack.push("Heres a string")
GenericStack.push(10)
GenericStack.push(23.0003)
print(GenericStack.empty())
print(GenericStack.items)

IntStack = Stack[int]()
# IntStack.push("Not an int")  # This fails when called by mypy.. But Since type hinting is optional in Python... The program runs fine. 
IntStack.push(1)
print(IntStack.items)

#The order of type variables in Generics matters. The order is always determined by their order in Generic[...]

U = TypeVar('U')
S = TypeVar('S')
A = TypeVar('A')

class One(Generic[U]): 
    pass
class Another(Generic[U]): 
    pass

class First(One[U], Another[S]): 
    pass
class Second(One[T], Another[S], Generic[U,S,A,T]): #mypy will complain: If generic is presnet, it should list all type variables
    pass

#Generic Functions

def first_gen_func(seq: Sequence[T]) -> T: #Note that this type variable, T, can be used in multiple generic classes and functions
    return seq[0]

s = first_gen_func('foo')
n = first_gen_func([1,2,3])
print(s)
print(n)


#Type checking inherited classes and chained getters and setters. 
class Shape: 
    def set_scale(self: T, scale: float) -> T:  # Note that Shape is Type T 
        self.scale = scale
        return self

class Circle(Shape): 
    def set_radius(self, radius: float)-> 'Circle': 
        self.radius = radius
        return self

class Square(Shape): 
    def set_width(self, width: float) -> 'Square': 
        self.width = width
        return self

shape = Shape().set_scale(0.5)
circle = Circle().set_scale(0.5).set_radius(2.7) # type: Circle
square = Square().set_scale(0.5).set_width(4.2) # type: Square 
print(type(shape))
print(type(circle))
print(type(square))


Letters: IntEnum = IntEnum('Letters', ('B', 'A', 'C', 'T')) #define a new Enum  -> __new__('Letters')

print(Letters.B >Letters.A)

valid_tuple= (Letters['A'], Letters['B'], Letters['C'])
possibly_invalid_tuple = (Letters['B'], Letters['B'], Letters['C'])

Codon = Tuple[Letters, Letters, Letters]

valid_Codon = ('B', 'A', 'C')
invalid_Codon = ('B', 'A', 'K') # Why does this line work? 'K' is clearly not a member of the Int Enum Defined on 82

