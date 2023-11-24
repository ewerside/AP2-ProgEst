import random
from random import randint

nomes_de_monstros = [
    "Grifo Celestial",
    "Basilisco Venenoso",
    "Ciclope Gigante",
    "Gárgula de Pedra",
    "Hidra de Sete Cabeças",
    "Manticora Alada",
    "Quimera Flamejante",
    "Sátiro Ensandecido",
    "Troll das Montanhas",
    "Fênix Negra"
]

class Monstro:
    def __init__(self):
        # Sorteamos diferentes nomes de monstros para dar mais variedade
        # ao jogo.
        self.nome = random.choice(nomes_de_monstros)
        self.forca = randint(5, 25)
        self.defesa = randint(5, 10)
        self.vida = randint(10, 100)

    def atacar(self):
        return self.forca

    def defender(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        return dano_final

    def esta_vivo(self):
        return self.vida > 0

    def ver_atributos(self):
        print(f"Força: {self.forca}\nDefesa: {self.defesa}\nVida: {self.vida}")