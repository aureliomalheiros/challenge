"""
Problem 1018 with python
"""
N = int(input())

#Use seven variables N100, N50, N20, N10, N5, N2, N1

print(N)

if 1000000 < N > 0:

    #Calculate Quotient 100
    N100    = N//100
    N       = N - N100*100
    #Calculate Quotient 50
    N50     = N//50
    N       = N - N50*50
    #Calculate Quotient 20
    N20     = N//20
    N       = N - N20*20
    #Calculate Quotient 10
    N10     = N//10
    N       = N - N10*10
    #Calculate Quotient 5
    N5     = N//5
    N       = N - N5*5
    #Calculate Quotient 2
    N2     = N//2
    N       = N - N2*2
    N1     = N//1
    N       = N - N1*1
    print(f'{N100} nota(s) de R$ 100,00')
    print(f'{N50} nota(s) de R$ 50,00')
    print(f'{N20} nota(s) de R$ 20,00')
    print(f'{N10} nota(s) de R$ 10,00')
    print(f'{N5} nota(s) de R$ 5,00')
    print(f'{N2} nota(s) de R$ 2,00')
    print(f'{N1} nota(s) de R$ 1,00')
