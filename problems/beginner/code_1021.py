"""
Problem 1021 with python
"""
N = float(input())

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
    #Caculate note1
    N1 = N//1
    N = N - N1*1
    N1 = float(f'{N1:.2f}')
    N = float(f'{N:.2f}')
    #N050
    N050 = N//0.5
    N = N - N050*0.5
    N050 = float(f'{N050:.2f}')
    N = float(f'{N:.2f}')
    #N025
    N025 = N//0.25
    N = N - N025*0.25
    N025 = float(f'{N025:.2f}')
    N = float(f'{N:.2f}')
    N010 = N//0.10
    N = N - N010*0.10
    N010 = float(f'{N10:.2f}')
    N = float(f'{N:.2f}')
    N005 = N//0.05
    N = N - N005*0.05
    N005 = float(f'{N005:.2f}')
    N = float(F'{N:.2f}')
    N001 = N*100
    N001 = float(f'{N001:.2f}')
    N = float(f'{N:.2f}')
    #Caculate NOTAS
    print("NOTAS:")
    print(f'{int(N100)} nota(s) de R$ 100.00')
    print(f'{int(N50)} nota(s) de R$ 50.00')
    print(f'{int(N20)} nota(s) de R$ 20.00')
    print(f'{int(N10)} nota(s) de R$ 10.00')
    print(f'{int(N5)} nota(s) de R$ 5.00')
    print(f'{int(N2)} nota(s) de R$ 2.00')
    print("MOEDAS:")
    print(f'{int(N1)} moeda(s) de R$ 1.00')
    print(f'{int(N050)} moeda(s) de R$ 0.50')
    print(f'{int(N025)} moeda(s) de R$ 0.25')
    print(f'{int(N010)} moeda(s) de R$ 0.10')
    print(f'{int(N005)} moeda(s) de R$ 0.05')
    print(f'{int(N001)} moeda(s) de R$ 0.01')
