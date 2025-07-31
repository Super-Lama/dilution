nb = float(input("Combien de solutions? "))

solutions = []
volumes = []
k = 0
x = 0

c_i = float(input("Quelle est la concentration de la solution mère? "))

while k < (nb):
    concentration = float(input("Quelle est la concentration de la solution " + str(k + 1) + " ? "))
    solutions.append(concentration)
    k += 1

q = input("Les solutions auront-elles tous le même volume final ? (Oui/Non) ")

if q.lower() == 'oui':
    v_f = float(input("Quel est le volume final commun de toutes les solutions (L) ? "))
    
    for i in solutions:
        if i > c_i:
            print("La concentration de la solution désirée est supérieure à celle de la solution mère.")
        else:
            v_i = ((i * v_f) / c_i) * 1000
            print(f"Pour obtenir {v_f} mL de solution à {i}, il faut {v_i:.3f} mL de la solution mère à {c_i}.")
else:
    while x < nb:
        v_f = float(input("Quel est le volume final de la solution " + str(x + 1) + " (mL) ? "))
        volumes.append(v_f)
        x += 1

    for i, v in zip(solutions, volumes):
        if i > c_i:
            print("La concentration de la solution désirée est supérieure à celle de la solution mère.")
        else:
            v_i = ((i * v)/c_i) * 1000
            print(f"Pour obtenir {v} L de solution à {i}, il faut {v_i:.3f} mL de la solution mère à {c_i}.")