def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    cents = int((vuelto - pesos)*100)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print(f"\n{"Vuelto"}")
    print(f"\n{"Pesos:"}")
    print(pesos)
    print("Centavos:")
    print(cents)
