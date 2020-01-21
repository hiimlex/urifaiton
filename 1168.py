n = int(input())

for i in range(n):
    testes = input()
    count = 0

    leds = {
        "1": 2,
        "2": 5,
        "3": 5,
        "5": 5,
        "4": 4,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6,
        "0": 6
    }

    for l in testes:
        for j in leds:
            if l == j:
                count += leds.get(j)
    print("%d leds" % count)
