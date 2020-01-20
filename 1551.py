n = int(input())

for i in range(n):
    texto = input().upper()
    count = 0
    alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    for l in alfabeto:
        if l in texto:
            count += 1

    if count == 26:
        print("frase completa")
    elif count >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")
