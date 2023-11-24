import time

def ataque(atacante, defensor):
    time.sleep(1.5)
    dano = atacante.atacar()
    dano_final = defensor.defender(dano)
    if defensor.esta_vivo():
        print(f"{defensor.nome} sofre um ataque, leva {dano_final} de dano e "
              f"está com {defensor.vida} de vida.")
        return False
    # Retorna True se o ataque matou o defensor
    return True


def combate(jogador, oponente):
    while True:
        if ataque(jogador, oponente):
            return True
        if ataque(oponente, jogador):
            return False