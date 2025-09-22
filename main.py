from math import sqrt

#### Fonction secondaire


def isprime(p):
    if p<2:
        return False    
    for k in range (2, int(sqrt(p)+1)):
        if p%k==0:
            return False
    return True


#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ") ###Problème ?

    print()


if __name__ =="__main__":
    main()
