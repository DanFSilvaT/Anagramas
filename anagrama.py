import random

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

while True:
    decisao = input("\nQueres outro com esta palavra? (sim/nao): ").casefold()

    if decisao == "não" or decisao == "nao" or decisao == "n":
        decisao = input("\nQueres um com outra palavra? (sim/nao): ").casefold()

        if decisao == "não" or decisao == "nao" or decisao == "n":
            print("\nAdeus")
            break

        else:
            palavra = palavra_input()
            print('\n--> ', anagrama_rng(palavra))
            continue

    else:
        print('\n--> ', anagrama_rng(palavra))
        continue
