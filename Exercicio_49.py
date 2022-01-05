hora=int(input("Digite a hora: "))
mi = int(input("Digite os minutos: "))
seg = int(input("digite os segundos: "))
dur = int(input("Informe a duração em segundos: "))
hora = hora * 3600
mi = mi * 60
tSec = hora + mi + seg + dur
hFinal = tSec // 3600
rest = tSec % 3600
miFinal = rest // 60
rest = rest % 60
print(f"A experiência irá terminar as: {hFinal}:{miFinal}:{rest}")


