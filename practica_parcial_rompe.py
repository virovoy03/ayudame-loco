

op = -1
while op != 0:
        try:
            op = int(input("1- comprar 0-salir"))
            if op != 0 and op <2:
                while op != 0:
                    try:
                        numero = int(input("1-producto de limpieza 2-ropa 0-salir"))  
                        if numero == 2:
                            monto_ropa = int(input("ingrese monto de ropa: "))
            
                            if monto_ropa < 3000 and monto_ropa >0:
                                print("su monto es: ", monto_ropa)
           
                            if monto_ropa > 3000 and monto_ropa >0:
                                print("su monto es: " , monto_ropa - monto_ropa * 0.1)


                        if numero == 1:               
                            monto_limpieza = int(input("ingrese monto de producto de limpieza: "))

                            if monto_limpieza < 5000 and monto_limpieza >0:
                                 print("su monto es: ", monto_limpieza)

                            if monto_limpieza > 5000 and monto_limpieza >0:
                                print("su monto es: " , monto_limpieza - monto_limpieza * 0.3)
                        if numero != 0 and numero>2:
                            print("ingrese numero valido")
                    except ValueError:
                        print("ingrese numero valido")        
            print("ingrese numero positivo valido")
        except ValueError:
                    print("ingrese numero valido")
            
        