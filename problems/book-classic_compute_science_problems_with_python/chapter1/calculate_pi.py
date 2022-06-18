"""Calculate PI"""

def calculate_pin(n_terms: int) -> int:
    "Calculate PI"
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi_calc: float = 0.0


    for _ in range(n_terms):
        pi_calc += operation * (numerator/denominator)
        denominator += 2
        operation *= -1
    return pi_calc

if __name__ == "__main__":
    print(calculate_pin(1000000))
    
