# Exercise 7 
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

def run():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b=[]
    

    for numero in a:
        if numero%2==0:
            b.append(numero)
        
    print(b)


    


if __name__=="__main__":
    run()