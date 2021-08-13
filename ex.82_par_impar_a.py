l = []
p = []
i = []


while True:
    n = int(input("Insira um número: "))
    l.append(n)

    print("Deseja continuar? [S/N]", end="")
    r = input()

    if r in "Nn":
        break
    while r not in "NnSs":
        print("Insira uma opção válida: ")
        print("Deseja continuar? [S/N]", end="")
        r = input()

for n in l:
    if n%2 == 0:
        p.append(n)
    else:
        i.append(n)

print(f"Lista completa: {l}")
print(f"Lista formada apenas com os números pares: {p}")
print(f"Lista formada apenas com os números ímpares: {i}")