import random

class Aventureiro:
    def __init__(self, nome):
        self.nome = nome
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.vida_maxima = random.randint(100, 120)
        self.vida = self.vida_maxima
        self.mochila = []
        self.posicao = [0, 0]

    def atacar(self):
        return self.forca + random.randint(1,6)

    def defender(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        return dano_final

    def mover(self, dir):
        if dir.lower() == "w":
            if self.posicao[1] > 0:
                self.posicao[1] -= 1
            else:
                return False
        elif dir.lower() == "s":
            if self.posicao[1] < 9:
                self.posicao[1] += 1
            else:
                return False
        elif dir.lower() == "d":
            if self.posicao[0] < 9:
                self.posicao[0] += 1
            else:
                return False
        else:
            if self.posicao[0] > 0:
                self.posicao[0] -= 1
            else:
                return False
        return True

    def coletar(self, item):
        self.mochila.append(item)

    def perder_item(self):
        if self.mochila != []:
            return self.mochila.pop(0)
        return None

    def esta_vivo(self):
        return self.vida > 0

    def ver_atributos(self):
        print(f"Força: {self.forca}\nDefesa: {self.defesa}\nVida: {self.vida}")

    def usar_item(self, item_index):
        item = self.mochila.pop(item_index)
        if item.tipo == "força":
            self.forca += item.intensidade
            print(f"Item {item.nome} aplicado! Aumentou permanentemente a força"
                  f" em {item.intensidade}.\n")
        elif item.tipo == "vida":
            self.vida = min(self.vida_maxima, self.vida + 20 * item.intensidade)
            print(f"Item {item.nome} aplicado! Recuperou {20 * item.intensidade}"
                  f" de vida.\n")
        else:
            self.defesa += item.intensidade
            print(f"Item {item.nome} aplicado! Aumentou permanentemente a "
                  f"defesa em {item.intensidade}.\n")

    def ver_mochila(self):
        index = 0
        print("\nMOCHILA:\n")
        for item in self.mochila:
            index += 1
            # Não usamos 'ç' no nome da variável como boa prática. Porém aqui
            # fazemos um tratamento para representar o tipo na tela.
            print(f"Item n°{index}:\n{item.nome}, Tipo: {'Força' if item.tipo == 'forca' else item.tipo.capitalize()}, "
                  f"Intensidade: {item.intensidade}\n")

