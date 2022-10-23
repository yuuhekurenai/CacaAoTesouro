import Puzzle
import win

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

#Mensagem inicial
print("Bem vindo a Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro perdido 🎁 .")


#Mensagem se caso o player perder (padrão)
gameover = "Fim de Jogo!"

#Questionários
escolha_1 = input('Você está em um cruzamento 🎆 , para onde você quer ir? Digite "Esquerda" ou "Direita".').lower()
if escolha_1 == "esquerda":
    escolha_2 = input("Agora você está de frente com um lago e no meio do lago há uma ilha. \n"
                      "Digite esperar para aguardar um barco 🚢 ou nado 🏊🏼‍ para nadar até a ilha.").lower()

    if escolha_2 == "nado":
        ultima_escolha = input("Nadou mais rápido que os tubarões e chegou ileso! 🐟\n"
                               "Agora você está de frente com 3 casas; 🚪 amarela , 🚪 azul e 🚪 verde.\n"
                               "Qual a sua escolhar?").lower()
    if ultima_escolha == "amarela":
        print(f"Sua morte poderia ser honrosa mas você escolheu a cor do medo! 🌌 \n"
              f"{gameover}")

    elif ultima_escolha == "azul":
        print("Os nobres sonham alto e você alcançou o tesouro!\n"
              "Agora encontre a chave!")
        Puzzle.puzzle()
    elif ultima_escolha == "verde":
        print("Aqui você não encontrará a paz!\n"
              "Você foi atacado por um urso! 🐻‍/\n"
              f"{gameover}")

    else:
        print(f"Só os fortes conseguirão encontrar o meu Tesouro!\n"
              f"{gameover}")

else:
    print(f"A sua busca pelo tesouro não começa com o pé direito! {gameover}")

