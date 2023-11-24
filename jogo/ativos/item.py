import random

nomes_de_itens = {
    "forca": ['Poção de Força Poderosa',
               'Elixir de Fortalecimento',
               'Tônico de Força',
               'Poção de Vigor',
               'Essência de Potência'
    ],
    "vida": ['Poção de Cura Rápida',
              'Elixir Revigorante',
              'Tônico Vital',
              'Poção de Energia',
              'Essência de Vitalidade'
    ],
    "defesa": ['Poção de Proteção',
                'Elixir de Resiliência',
                'Tônico de Defesa',
                'Poção de Resistência',
                'Essência de Guarda'
    ]
}

class Item:
    def __init__(self):
        sorteio_item = random.randint(1, 100)
        if sorteio_item <= 15:
            self.tipo = "forca"
            if sorteio_item <= 10:
                self.intensidade = 1
            else:
                self.intensidade = 2
        elif sorteio_item <= 95:
            self.tipo = "vida"
            if sorteio_item <= 65:
                self.intensidade = 1
            else:
                self.intensidade = 2
        else:
            self.tipo = "defesa"
            self.intensidade = 1
        # Sorteamos diferentes nomes de itens para dar mais variedade ao jogo.
        self.nome = random.choice(nomes_de_itens[self.tipo])
