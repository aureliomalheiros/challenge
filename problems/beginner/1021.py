N = float(input())

if (N > 0 and N < 1000000):
    ###CALCULATE NOTAS###
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

    ###CALCULATE COINS###
    N1 = N//1
    N = N - N1*1
    N1 = float("%.2f" %N1)
    N = float("%.2f" %N)
    
    N050 = N//0.5
    N = N - N050*0.5
    N050 = float("%.2f" %N050)
    N = float("%.2f" %N)
    
    N025 = N//0.25
    N = N - N025*0.25
    N025 = float("%.2f" %N025)
    N = float("%.2f" %N)
    
    N010 = N//0.10
    N = N - N010*0.10
    N010 = float("%.2f" %N010)
    N = float("%.2f" %N)
    
    N005 = N//0.05
    N = N - N005*0.05
    N005 = float("%.2f" %N005)
    N = float("%.2f" %N)
    
    N001 = N*100
    N001 = float("%.2f" %N001)
    N = float("%.2f" %N)
    
    print("NOTAS:")
    print("{} nota(s) de R$ 100.00" .format(int(N100)))
    print("{} nota(s) de R$ 50.00" .format(int(N50)))
    print("{} nota(s) de R$ 20.00" .format(int(N20)))
    print("{} nota(s) de R$ 10.00" .format(int(N10)))
    print("{} nota(s) de R$ 5.00" .format(int(N5)))
    print("{} nota(s) de R$ 2.00" .format(int(N2)))
    print("MOEDAS:")
    print("{} moeda(s) de R$ 1.00" .format(int(N1)))
    print("{} moeda(s) de R$ 0.50" .format(int(N050)))
    print("{} moeda(s) de R$ 0.25" .format(int(N025)))
    print("{} moeda(s) de R$ 0.10" .format(int(N010)))
    print("{} moeda(s) de R$ 0.05" .format(int(N005)))
    print("{} moeda(s) de R$ 0.01" .format(int(N001)))
    
