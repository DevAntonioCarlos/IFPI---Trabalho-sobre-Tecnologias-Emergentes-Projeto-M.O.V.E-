import numpy as np

def calcular_distancia(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def detectar_gesto(marcadores):
    dedo_polegar = marcadores[4]
    dedo_indicador = marcadores[8]

    dist = calcular_distancia(dedo_polegar, dedo_indicador)
    
    if dist < 0.05:
        return "Pinça (Comando 1)"
    else:
        return "Aberto (Comando 2)"

