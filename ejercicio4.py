# Exercise 4 
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


def run():
    numero=int(input("""Este programa calcula los divisores de un numero.    
    Escribe un numero:"""
    ))
    contador=1


    for contador in range(1,numero+1):
        if numero%contador==0:
            print(contador)
            
        

if __name__=="__main__":
    run()