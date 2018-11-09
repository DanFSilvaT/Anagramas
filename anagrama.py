import random
import math

print("Bem Vind(o/a)! Queres um anagrama? Então..")
#print("São de borla, por isso faz os que quiseres!")

def palavra_input():
    palavra = input("Escreve uma palavra: ").lower()
    
    return palavra
    
def anagrama_rng(palavra):
    palavra = [letra for letra in palavra]
    anagrama = ""
    for letra in range(len(palavra)):
        anagrama = anagrama + palavra.pop(random.randrange(len(palavra)))

    return anagrama
    
palavra = palavra_input()
print('\n--> ', anagrama_rng(palavra))
anagrama = anagrama_rng(palavra)
memoria = []
memoria.append(anagrama)


while True:

    if len(memoria) == math.factorial(len(palavra)):
        print("Todos os anagramas:", sorted(memoria))
        break
        
    decisao = input("\nQueres outro com esta palavra? (sim/nao): ").casefold()

    if decisao == "não" or decisao == "nao" or decisao == "n":
        decisao = input("\nQueres um com outra palavra? (sim/nao): ").casefold()

        if decisao == "não" or decisao == "nao" or decisao == "n":
            print("\nAdeus")
            print(sorted(memoria))
            break

        else:
            palavra = palavra_input()
            memoria = []
            print('\n--> ', anagrama_rng(palavra))
            continue

    else:
        anagrama_rng(palavra)
        anagrama = anagrama_rng(palavra)
        if anagrama not in memoria:
            memoria.append(anagrama)
            print('\n--> ', anagrama)
            continue
        else:
            print("Repeti um anagrama, desculpa, foi este:\n--> ", anagrama)
            continue
