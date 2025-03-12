import numpy as np


jogo = 0
while jogo <= 2:
    numeros =  np.random.choice(range(1, 60), size=6, replace=False)
    jogo += 1
    print(f'Jogo {jogo} = {numeros}\n')



