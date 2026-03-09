#simulador de cuenta bancaria# #como bancolombia pero mejor :v#
print("Bienvenido a tu banco")
print("debes crear un usuario nuevo")
usuario = input("ingresa tu nombre de usuario : ")
clave = int(input("ingresa tu clave:  "))
saldo = 0
retiro = 0
print("Bienvenido ahora debes hacer un deposito de $100 minimo:   ")
def depositar(saldo_actual):
    deposito = int(input("Monto a depositar"))
    
    if deposito >= 100:
        print("deposito exito")
        return saldo_actual + deposito
    else:
        print("monto insuficiente ( Minimo 100)")
        return saldo_actual
    

while True:
    print("----- Menu-----")
    print("1. Depositar")
    print("2. ver saldo")
    print("3 retirar")
    print("4 salir")
    
    opcion = input("elige una opcion: ")
    
    if opcion == "1":
        saldo = depositar(saldo)
        
    elif opcion == "2":
        print("tu saldo es de: ", saldo)
        
    elif opcion == "3":
        print("Cantidad que deseas retirar:  ")
        retiro = int(input())
        if retiro < saldo:
            print("tu mondo a retirar es de:" , (saldo - retiro))
        elif retiro == saldo:
             print("tu monto a retirar es de:  " ,  retiro)   
        elif  retiro > saldo:
            print("monto insuficiente para retirar")
    elif opcion == "4":
        print("gracias por usar el mejor banco")
        break
    else:
        print("opcion invalida")    
        
        
    print("Vuelva Pronto ;)")       
