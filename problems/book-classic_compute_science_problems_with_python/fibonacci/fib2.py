"""Fibonacci with dictionary"""
from typing import Dict

memo: Dict[int, int] = {0: 0, 1:1}

def fib2(n_recursive: int) -> int:
    """Recursive"""
    if n_recursive not in memo:
        memo[n_recursive] = fib2(n_recursive - 1) + fib2(n_recursive - 2)
    return memo[n_recursive]
if __name__ == "__main__":
    print(fib2(5))
    print(fib2(30))
