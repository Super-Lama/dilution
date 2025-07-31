nb = input("Combien de solutions? ")
c_i = input("Quelle est la concentration de la solution mère? ")

solutions = []
k = 0

print("Entrez les solutions en ordre décroissant de concentration.")

while k < int(nb):
    concentration = input(f"Quelle est la concentration de la solution {k + 1} ? ")
    solutions.append(float(concentration))
    k += 1

volumes = []
x = 0

while x < int(nb):
    v_f = input(f"Quel est le volume final de la solution {x + 1} (L) ? ")
    volumes.append(float(v_f))
    x += 1

for i, v in zip(solutions, volumes):
    if i > float(c_i):
        print("La concentration de la solution désirée est supérieure à celle de la solution mère.")
    else:
        v_i = ((i * v) / float(c_i)) * 1000  # Convertir en mL
        c_i = i
        print(f"Pour obtenir {v} L de solution à {i}, il faut {v_i:.3f} mL de la solution mère à {c_i}.")