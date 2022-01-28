def run():
    numero=int(input("Escribe un numero: "))
    par_o_impar=numero%2
    divisible_cuatro=numero%4
    if divisible_cuatro==0:
        print("Tu numero es divisible 4")
    elif par_o_impar==0:
        print("Tu numero es par")
    else:
        print("Tu numero es impar")


if __name__=="__main__":
    run()

