"""
Problem fibonacci with python
"""
def fib1(n_recursive: int) -> int:
    """Recursive"""
    if n_recursive < 2:
        return n_recursive
    return fib1(n_recursive - 1) + fib1(n_recursive - 2)

if __name__ == "__main__":
    print(fib1(5))
    print(fib1(10))
