"""Calculating pi with the Leibniz formula of 
pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11... """

def calcpi(n): 
    numerator = 4.0 
    denominator = 1.0 
    operation = 1.0 
    pi = 0.0

    for _ in range(n): 
        pi += operation * (numerator/denominator)
        denominator += 2.0 
        operation *= -1 
    return pi

if __name__ == "__main__":
    print(calcpi(100000))
