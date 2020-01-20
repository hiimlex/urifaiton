linha1 = input().split(" ")
linha2 = input().split(" ")

p1, q1, v1 = linha1
p2, q2, v2 = linha2

p1 = int(p1)
q1 = int(q1)
v1 = float(v1)
p2 = int(p2)
q2 = int(q2)
v2 = float(v2)

total = (q1 * v1) + (q2 * v2)

print("VALOR A PAGAR: R$ %.2f" % total)
