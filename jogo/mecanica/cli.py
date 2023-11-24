import random, time

from jogo.ativos import item, mapa, tesouro
from jogo.mecanica import combate
from jogo.personagens import aventureiro, monstro
from jogo.ativos.introducao import arte_tesouro, texto_tutorial

def interagir_item(p1):
    """
    - lista os itens da mochila
    - pede para o jogador escolher o item
    - usa o item caso exista, ou diz que não achou aquele item na mochila
    """
    p1.ver_mochila()

    escolha_item = input("Digite o número do item escolhido ou 0 caso deseje "
                         "fechar a mochila: ")
    while not escolha_item.isnumeric():
        escolha_item = input("Por favor, digite o número do item escolhido ou "
                             "0 para fechar a mochila: ")
    index_item = int(escolha_item)-1
    if index_item in range(0, len(p1.mochila)):
        p1.usar_item(index_item)
    elif index_item == -1:
        print("")
    else:
        print("Desculpe, esse item não está na sua mochila.\n")

# Essa função é chamada quando um novo item aparece, seja aleatoriamente ou
# por ter derrotado um monstro.
def drop_item(jogador):
    novo_item = item.Item()
    jogador.coletar(novo_item)
    print(f"{novo_item.nome}, Tipo: "
          f"{'Força' if novo_item.tipo == 'forca' else novo_item.tipo.capitalize()}"
          f", Intensidade: {novo_item.intensidade}\n")

"""
A nova mecânica que decidimos adicionar é a de fuga. Quando um jogador encontra
um monstro, ele tem a opção de tentar fugir. Se essa for a escolha do jogador,
um dado de 6 lados é rolado. Se o jogador tira 6, ele consegue fugir.
Para que o jogador não fique sempre tentando fugir:

1. O monstro agora "dropa" um item sempre que é derrotado.
2. Se o jogador não consegue fugir, ele perde o primeiro item da mochila. Se o 
jogador não tinha itens na mochila, ele toma um dano aleatório que pode variar 
de 1 até 20. (O jogador também pode escolher não usar um item para que isso o
proteja desse dano.)

Como isso tornou o encontro aleatório de monstro mais complexo, o separamos numa
função encontro_monstro que apenas recebe o aventureiro e lida com todos os 
desdobramentos desse encontro, retornando True se o aventureiro sobreviveu e 
False se não.
"""
def encontro_monstro(jogador):
    novo_monstro = monstro.Monstro()
    print(f"\nOh não! Você encontrou o monstro {novo_monstro.nome}!")
    novo_monstro.ver_atributos()
    fuga = input("Deseja tentar fugir? (s/n) ").lower()[0]
    if fuga == 's':
        print("\nRolando o dado... Você precisa tirar 6 para conseguir "
              "fugir.\n")
        time.sleep(2)
        # O jogador consegue fugir do combate se tirar 6 no dado.
        dado_sorte = random.randint(1, 6)
        print(f"Você rolou {dado_sorte} no dado do destino.\n")
        if dado_sorte == 6:
            print("Você conseguiu despistar o monstro!")
            time.sleep(2)
            return True
        else:
            print("Oops! Você não conseguiu fugir.")
            item_perdido = jogador.perder_item()
            if item_perdido:
                print(f"Em sua tentativa de fuga, você perdeu o seguinte item:"
                      f"\n{item_perdido.nome}\n")
            else:
                dano_azar = random.randint(1,20)
                jogador.vida -= dano_azar
                print(f"Em sua tentativa de fuga, você tropeçou e tomou "
                      f"{dano_azar} de dano.\n")
                if not jogador.esta_vivo():
                    print("Wow! Você conseguiu mesmo morrer fugindo...")
                    return False
            time.sleep(2)
    elif fuga != 'n':
        print("Não conheço esse comando.", end=' ')
    print("Prepare-se para o combate!")
    time.sleep(1)
    if combate.combate(jogador, novo_monstro):
        print(
            "\nSeu ataque matou o monstro! Parabéns! Veja o que ele deixou "
            "cair:")
        drop_item(jogador)
        return True
    else:
        return False

def movimentar(p1, dir, tes):
    """
    - movimenta o aventureiro
    - se ele andou, seleciona uma das opções: nada, item ou monstro
    - se sorteou monstro, inicializa um monstro e começa um combate
    - se sorteou item, inicializa um item
    - retorna False se o aventureiro morrer, e True nos outros casos
    """
    if p1.mover(dir):
        encontro = random.randint(1,100)
        if encontro <= 40:
            return encontro_monstro(p1)
        elif encontro <= 60 and p1.posicao != tes.posicao:
            print(f"\nVocê encontrou um novo item! Veja:")
            drop_item(p1)
    return True

def jogo():
    print(arte_tesouro)
    print("=" * 50)
    print("Olá! Bem-vindo à ilha do tesouro!")
    nome = input("Deseja ir atrás de riquezas incalculáveis? Primeiro, informe "
                 "seu nome: ")
    p1 = aventureiro.Aventureiro(nome)
    tutorial = input(f"Saudações, {nome}! Devo-lhe informar que este é um mundo"
                     f" perigoso, deseja um tutorial? (s/n) ").lower()[0]
    if tutorial == 's':
        print(texto_tutorial, end=' ')
    print("Boa sorte!\n")
    tes = tesouro.Tesouro()
    # mapa.desenhar(p1, tes)

    while True:
        mapa.desenhar(p1, tes)
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Já correndo?")
            break

        if op == "T":
            p1.ver_atributos()
        elif op == "I":
            interagir_item(p1)
        elif op in ["W", "A", "S", "D"]:
            if not movimentar(p1, op, tes):
                print("Você sofreu um ataque mortal! Game Over...")
                break
        else:
            print(f"{p1.nome}, não conheço essa! Tente novamente!")

        if p1.posicao == tes.posicao:
            print(f"Parabéns, {p1.nome}! Você encontrou o tesouro!")
            break
