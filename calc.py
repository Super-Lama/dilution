def calc_dilutions_series(c_i, solutions, volumes):

    for i, v in zip(solutions, volumes):
        if i > float(c_i):
            print("La concentration de la solution désirée est supérieure à celle de la solution mère.")
        else:
            v_i = ((i * v) / float(c_i))
            print(f"Pour obtenir {v} mL de solution à {i}, il faut {v_i:.3f} mL de la solution à {c_i}.")
            c_i = i

def calc_dilutions_directs(c_i, concentrations, volumes):
        
        for i, v in zip(concentrations, volumes):
            if i > c_i:
                print("La concentration de la solution désirée est supérieure à celle de la solution mère.")
            else:
                v_i = ((i * v)/c_i)
                print(f"Pour obtenir {v} mL de solution à {i}, il faut {v_i:.3f} mL de la solution mère à {c_i}.")