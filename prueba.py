while True:
    nombreTrabajador = input("Ingrese el nombre del trabajador: ")
    sueldoBase = int(input("Ingrese su sueldo base: "))
    horasExtras = int(input("Ingrese la cantidad de horas extras trabajadas: "))
    #Se piden los datos al usuario
    if len(nombreTrabajador) >= 30 or nombreTrabajador == "":
        print("No se ha ingresado el nombre.")
        break
    elif sueldoBase < 0 or horasExtras < 0:
        print("Solo se pueden ingresar valores positivos.")
        break
    #Se valida la informaciòn y si no funciona se cierra el programa
    else:
        pagoHora = sueldoBase/180
        pagoHoraExtra = (pagoHora * 1.5) * horasExtras
        totalIngresos = sueldoBase + pagoHoraExtra
        descuentoFonasa = totalIngresos*0.07
        descuentoAFP = totalIngresos * 0.1
        seguridadSocial = descuentoAFP + descuentoFonasa
        sueldoNeto = totalIngresos - seguridadSocial
    #Càlculo de la liquidaciòn
    def creararchivo():
        archivo = open(f"liquidacion_{nombreTrabajador}.txt","w")
        archivo.write(f"Nombre trabajador: {nombreTrabajador} \nSueldo base: {sueldoBase}\nPago horas extras: {pagoHoraExtra}\nTotal de ingresos: {totalIngresos}\n")
        archivo.write(f"Descuentos por fonasa y AFP: {seguridadSocial}\nSueldo neto a pagar: {sueldoNeto}")
        archivo.close()
    creararchivo()
    #Creaciòn de un archivo de texto con todos los datos
    print("1. Realizar otra liquidaciòn")
    print("2. Salir del programa")
    opcion = input("Elige una opciòn: ")
    if opcion == "1":
        print("")
    elif opcion == "2":
        print("Saliendo del programa...")
        break
    else: 
        print("Opciòn no valida.")
    #Pregunta al usuario si desea continuar o salir

