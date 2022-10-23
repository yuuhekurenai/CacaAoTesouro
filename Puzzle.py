# Este Puzzle aparecerá se o player encontrar o tesouro
import random
import win


def puzzle():
    # print inicial
    linha1 = ["🎁","🎁","🎁"]
    linha2 = ["🎁","🎁","🎁"]
    linha3 = ["🎁","🎁","🎁"]
    local = [linha1, linha2, linha3]

    print(f"{linha1}\n{linha2}\n{linha3}")

    # Código para alterar a posição da chave
    horizontal = random.randint(1, 3)
    vertical = random.randint(1, 3)
    linha_select = local[vertical - 1]
    linha_select[horizontal - 1] = "🔑"

    #Concatenar as posições para serem comparadas com a reposta do player
    concatenar = f"{horizontal}+{vertical}"

    h_pergunta = input("Digite de 1 a 3, Qual linha está a chave?")
    v_pergunta = input("Digite de 1 a 3, Qual coluna está a chave?")
    print(h_pergunta)
    print(v_pergunta)
    concat_resposta = f"{h_pergunta}+{v_pergunta}"

    if concat_resposta == concatenar:
        print(f"{linha1}\n{linha2}\n{linha3}")
        print(f"Parabéns vocês abriu o Báu de Tesouros!\n {win.bebidas}")
    else:
        print(f"Você não encontrou a chave! Mais sorte na próxima\n"
              f"Fim de Jogo!")




