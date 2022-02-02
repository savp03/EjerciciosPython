def run():
    print("Este programa es el juego de piedra, papel o tijera")       
    i=1
    n=1

    
    while i<3 or n<3:  
        player1=int(input("""Por favor jugador 1:
        Si tu eleccion es piedra escribe 1
        Si tu eleccion es papel escribe 2
        Si tu eleccion es tijera escribe 3 
        """))
        player2=int(input(""""Por favor jugador 2:
        Si tu eleccion es piedra escribe 1
        Si tu eleccion es papel escribe 2
        Si tu eleccion es tijera escribe 3 
        """))     
        if player1<1 or player1>3 or player2<1 or player2>3:
            print("Elige una opcion valida:")
            continue
        elif player1==1 and player2==3:
            print("Gana el jugador 1")
            if i == 2:
                break
            i += 1
        elif player1==2 and player2==1:
            print("Gana el jugador 1")
            if i == 2:
                break
            i += 1
        elif player1==3 and player2==2:
            print("Gana el jugador 1")
            if i == 2:
                break
            i += 1
        elif player1==player2:
            print("Empate")
            continue
        else:
            print("Gana el jugador 2")
            if n == 2:
                break
            n += 1


if __name__=="__main__":
    run()