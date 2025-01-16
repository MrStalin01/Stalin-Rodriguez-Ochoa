def main ():
    vector = []

    print ("Introduce 10 numeros para llenar el vector: \n")

    for i in range (10):
        continuar = True
        while(continuar):
            numeros = float(input(f"Dime los numeros {i+1}:\n"))
            vector.append(numeros)
            continuar = False

    maximovalor = max(vector)
    cantidadmaxima = vector.count(maximovalor)

    print("\nResultados:")
    print(f"El valor máximo es: {maximovalor}")
    print(f"El valor máximo aparece {cantidadmaxima} veces.")

    return main()