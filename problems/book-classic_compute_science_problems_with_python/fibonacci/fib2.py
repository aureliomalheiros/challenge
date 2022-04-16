#Fibonacci with dictionary
from typing import Dict

memo: Dict[int, int] = {0: 0, 1:1}

def fib2(n: int) -> int: 
    if n not in memo: 
        memo[n] = fib2(n - 1) + fib2(n - 2)
    return memo[n]
if __name__ == "__main__":
    print(fib2(5))
    print(fib2(30))