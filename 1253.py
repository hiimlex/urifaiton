n = int(input())

for i in range(n):
    text = input()
    move = int(input())
    t = ""
    for l in text:
        v = ord(l) - move

        if (v < 65):
            t += chr(91 - (65 - v))
        else:
            t += chr(ord(l) - move)
    print(t)
