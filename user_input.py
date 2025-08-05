import calc as cl

nb = int(input("Combien de solutions voulez-vous préparer ? "))

c_i = float(input("Quelle est la concentration de la solution mère ? "))

volumes = []
concentrations = []

print("Note : mettre les solutions en ordre decroissant de concentration")

q = input("Les solutions auront-elles toutes le même volume ? (Oui/Non) ")

while q.lower() not in ['oui', 'non']:
        q = input("Veuillez répondre par 'Oui' ou 'Non ")

if q.lower() == 'oui':
        volumes = [float(input("Quel sera le volume des solutions? "))] * nb
elif q.lower() == 'non':
        while len(volumes) < nb:
            v = float(input("Quel est le volume final de la solution " + str(len(volumes) + 1) + " (mL) ? "))
            volumes.append(v)


while len(concentrations) < nb:
    c = float(input("Quelle est la concentration de la solution " + str(len(concentrations) + 1) + " ? "))
    concentrations.append(c)

f = input("Voulez-vous faire des solutions directs ou en series ? ")

while f.lower() not in ['series', 'directs']:
    f = input("Veuillez répondre par 'Oui' ou 'Non' ")

if f.lower() == 'directs':
    cl.calc_dilutions_directs(c_i, concentrations, volumes)
elif f.lower() == 'series':
    cl.calc_dilutions_series(c_i, concentrations, volumes)