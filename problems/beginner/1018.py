N = int(input())

#Use seven variables N100, N50, N20, N10, N5, N2, N1

print(N)

if (N > 0 and N < 1000000):

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

    #Calculate Quotient 1
    N1     = N//1
    N       = N - N1*1

    print("{} nota(s) de R$ 100,00" .format(N100))
    print("{} nota(s) de R$ 50,00" .format(N50))
    print("{} nota(s) de R$ 20,00" .format(N20))
    print("{} nota(s) de R$ 10,00" .format(N10))
    print("{} nota(s) de R$ 5,00" .format(N5))
    print("{} nota(s) de R$ 2,00" .format(N2))
    print("{} nota(s) de R$ 1,00" .format(N1))
