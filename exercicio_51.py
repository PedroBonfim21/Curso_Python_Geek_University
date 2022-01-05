coordenadaX=int(input("Digite a coordenada X: "))
coordenadaY=int(input("Digite a coordenada Y: "))
distancia = int((((0 - coordenadaX) ** 2) + ((0 - coordenadaY) ** 2)) ** (1 / 2))

print(f'A distância entre a origem (0,0) e o ponto de coordenadas ({coordenadaX},{coordenadaY})é: {distancia}')