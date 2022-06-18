"""
Problem 1021 with python
"""

X = float(input())

if 1000000 < X > 0:

    #Calculate Quotient 100
    X100    = X//100
    X       = X - X100*100
    #Calculate Quotient 50
    X50     = X//50
    X       = X - X50*50

    #Calculate Quotient 20
    X20     = X//20
    X       = X - X20*20

    #Calculate Quotient 10
    X10     = X//10
    X       = X - X10*10

    #Calculate Quotient 5
    X5     = X//5
    X       = X - X5*5

    #Calculate Quotient 2
    X2     = X//2
    X       = X - X2*2
    #Caculate note1
    X1 = X//1
    X = X - X1*1
    X1 = float(f'{X1:.2f}')
    X = float(f'{X:.2f}')
    #X050
    X050 = X//0.5
    X = X - X050*0.5
    X050 = float(f'{X050:.2f}')
    X = float(f'{X:.2f}')
    #X025
    X025 = X//0.25
    X = X - X025*0.25
    X025 = float(f'{X025:.2f}')
    X = float(f'{X:.2f}')
    X010 = X//0.10
    X = X - X010*0.10
    X010 = float(f'{X10:.2f}')
    X = float(f'{X:.2f}')
    X005 = X//0.05
    X = X - X005*0.05
    X005 = float(f'{X005:.2f}')
    X = float(F'{X:.2f}')
    X001 = X*100
    X001 = float(f'{X001:.2f}')
    X = float(f'{X:.2f}')
    #Caculate NOTAS
    print("NOTAS:")
    print(f'{int(X100)} nota(s) de R$ 100.00')
    print(f'{int(X50)} nota(s) de R$ 50.00')
    print(f'{int(X20)} nota(s) de R$ 20.00')
    print(f'{int(X10)} nota(s) de R$ 10.00')
    print(f'{int(X5)} nota(s) de R$ 5.00')
    print(f'{int(X2)} nota(s) de R$ 2.00')
    print("MOEDAS:")
    print(f'{int(X1)} moeda(s) de R$ 1.00')
    print(f'{int(X050)} moeda(s) de R$ 0.50')
    print(f'{int(X025)} moeda(s) de R$ 0.25')
    print(f'{int(X010)} moeda(s) de R$ 0.10')
    print(f'{int(X005)} moeda(s) de R$ 0.05')
    print(f'{int(X001)} moeda(s) de R$ 0.01')
    
