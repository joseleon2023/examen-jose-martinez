#ET programacion de algoritmo
pisos = []
for _ in range(10):
    pisos.append(['A', 'B', 'C', 'D'])

vendidos = []
compradores = []

def obtener_departamento():
    departamento_valido = False
    while not departamento_valido:
        piso = int(input("Ingrese el número de piso (1-10): "))
        tipo = input("Ingrese el tipo de departamento (A, B, C o D): ")
        if piso < 1 or piso > 10 or tipo not in ['A', 'B', 'C', 'D']:
            print("Departamento inválido. Intente nuevamente.")
        elif pisos[piso-1][ord(tipo)-ord('A')] == 'X':
            print("El departamento seleccionado no está disponible. Intente nuevamente.")
        else:
            departamento_valido = True
            pisos[piso-1][ord(tipo)-ord('A')] = 'X'
    return piso, tipo

def obtener_run():
    run_valido = False
    while not run_valido:
        run = input("Ingrese el RUN del comprador (sin guion ni puntos): ")
        if not run.isdigit() or len(run) != 8:
            print("RUN inválido. Intente nuevamente.")
        else:
            run_valido = True
    return run

def comprar_departamento():
    print("Departamentos disponibles:")
    for i, piso in enumerate(pisos, 1):
        for j, departamento in enumerate(piso, 1):
            if departamento == 'X':
                print(f"Departamento {chr(j+ord('A')-1)} en el piso {i} - No está disponible")
            else:
                print(f"Departamento {chr(j+ord('A')-1)} en el piso {i} - Disponible")
    piso, tipo = obtener_departamento()
    run = obtener_run()
    compradores.append((run, f"{tipo}{piso}"))
    print("La operación se ha realizado correctamente.")

def mostrar_departamentos_disponibles():
    print("Departamentos disponibles:")
    for i, piso in enumerate(pisos, 1):
        for j, departamento in enumerate(piso, 1):
            if departamento == 'X':
                print(f"Departamento {chr(j+ord('A')-1)} en el piso {i} - No está disponible")
            else:
                print(f"Departamento {chr(j+ord('A')-1)} en el piso {i} - Disponible")

def mostrar_listado_compradores():
    print("Listado de compradores:")
    compradores_ordenados = sorted(compradores, key=lambda x: x[0])
    for run, departamento in compradores_ordenados:
        print(f"RUN: {run} - Departamento: {departamento}")

def mostrar_ventas_totales():
    precios = {'A': 3800, 'B': 3000, 'C': 2800, 'D': 3500}
    ventas_totales = {tipo: 0 for tipo in precios}
    for _, departamento in compradores:
        tipo = departamento[0]
        ventas_totales[tipo] += precios[tipo]
    print("Ventas totales:")
    print("Tipo de Departamento Cantidad Total")
    for tipo, total in ventas_totales.items():
        cantidad = pisos[0].count(tipo) + pisos[1].count(tipo) + pisos[2].count(tipo) + pisos[3].count(tipo)
        print(f"Tipo {tipo} {precios[tipo]} UF {cantidad} {total} UF")
    print(f"TOTAL {sum(ventas_totales.values())} UF")

def mostrar_menu():
    print("------ MENÚ ------")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            comprar_departamento()
        elif opcion == '2':
            mostrar_departamentos_disponibles()
        elif opcion == '3':
            mostrar_listado_compradores()
        elif opcion == '4':
            mostrar_ventas_totales()
        elif opcion == '5':
            print("gracias por usar el sistema")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
if __name__ == "__main__":
    main()