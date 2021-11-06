from typing import List, Dict, Optional, Any, Sequence, Tuple, Callable, Generic, TypeVar
#Exploring the typing module in python 

#x: int = 2
#x: List[List[int]]

def add_numbers (a:int, b:int, c:int) -> int: 
    return a + b + c

#generic version of list 
#list of lists containing integers: 
x: List[List[int]] = [[1,2],[3,4]] 
#This would return 'incompatible type error' y: List[List[int]] = [[1,2],[3,'not an int, type error']] 

#Dictionaries 

#Dict[<keyDatatype>, <valueDatatype> ]
d: Dict[str, str] = {"a": "b"}
#Line below will not work
#d['NewKey'] = 2 #Will Throw: error: Incompatible types in assignment (expression has type "int", target has type "str")

d['NewKey'] = 'The number two as a string' #Both key and value types match the type annotations

#Creating your own type variables. 
#Vector is a variable that I have defined as a list of floating pinot numbers
#The IDE will recognize this as a type alias --- Vector: Type[List[float]]
Vector = List[float]

def foo(v: Vector) -> Vector: 
    pass

#Here we define Vectors as a list containing Vectors.. 
Vectors = List[Vector]  #This is easier to read than Vectors = List[List[float]]

#Optional type 

def bar(output: Optional[bool] = False):
    pass

#The function takes in any input and will return Any
def func_that_returns_anything(output = Any) -> Any: 
    return output

#Sequence: maybe a list, maybe a tuple, any sequence! -- Anything that can be indexed? 

def function_that_takes_sequence(seq: Sequence[str]) -> Sequence: 
    pass 

function_that_takes_sequence(['string1','string2','string3']) #No problems
# function_that_takes_sequence(['string1','string2', 1 ]) 
'''Problem! Tried to put an integer in a Sequence that only accepts Strings'''
#List item 2 has incompatible type "int"; expected "str"

#Tuple -- Must specify the type for each position in the tuple 
#   This should work, right?  t: Tuple[int] =  (1,2,3) 
""" 
python_typing.py:54: error: Incompatible types in assignment (expression has type "Tuple[int, int, int]", variable has type "Tuple[int]")
Found 2 errors in 1 file (checked 1 source file)
"""
# Surprise :) 

#This is what is expected by linter
t: Tuple[int,int,int] =  (1,2,3)

def add_with_two_ints(x:int, y:int)-> int: 
    return x + y

def add_with_two_string(x:str, y:str) -> str: 
    return  x + y
#Callable type: accepting functions as parameters 
#Example below: Function takes another function as input, the function used as input takes in two parameters, both are integers, and it return an integer
def callable_as_param(func_as_param: Callable[[int, int], int]) -> None: # func: Callable[<param1 type>, <param2 type>], <return type> ] 
    func_as_param(1,2)

callable_as_param(add_with_two_ints) #No Errors 
#callable_as_param(add_with_two_string) #Expecting error. 

'''
python_typing.py:76: error: 
Argument 1 to "callable_as_param" has incompatible type "Callable[[str, str], str]"; expected "Callable[[int, int], int]" 


'''

#We can also use Callable as a return type... 
#This example will be a nested function. 

def nested() -> Callable[[int, int], int]: 
    #Notice that the function signature (param types and return type) match that of the outer function, which is returning the inner function
    def subtract(x:int, y:int) -> int: 
        return x - y 

    return subtract

#Generics 
T = Typevar('T')

# 'T' is the name of the type..
# Generic types are placeholders, 'i DOn't ow what it will be, but I will call it T 

def get_item(some_list: List[T], index: int) -> T: 
    return lst[index]

#Everything inside the list, some_list, must be of type 'T'
