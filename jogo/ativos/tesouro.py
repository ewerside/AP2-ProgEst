import random

class Tesouro:
    def __init__(self):
        while True:
            self.posicao = [random.randint(0, 9), random.randint(0, 9)]
            if self.posicao != [0, 0]:
                break
