def run():
    lista1 = [1,2,3,4,5,6,7,8,9]
    lista2=[3,6,9]


    for numero in lista1:
        if numero in lista2:
            print(numero)


if __name__=="__main__":
    run()