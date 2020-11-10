#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
from timeit import timeit
# from sympy import *
from scipy.integrate import quad

s = "import numpy as np"

# TODO: Définissez vos fonctions ici (il en manque quelques unes)

# 1.Créer un array présentant 64 valeurs uniformément réparties entre -1.3 et
# 2.5
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, 64)

print(timeit("np.linspace(-1.3, 2.5, 64)", setup=s, number=10000))

# On peut aussi faire avec la fonction arange()
print(-1.3 + (2.5 + 1.3) * np.arange(0, 64) / 63)

print(timeit("-1.3 + (2.5 + 1.3) * np.arange(0, 64) / 63", setup=s, number=10000))

# On peut aussi faire avec des boucles

print(timeit("[-1.3 + (2.5 + 1.3) * i / 63 for i in range(64)]", number=10000))

a = [-1.3 + (2.5 + 1.3) * i / 63 for i in range(64)]
print(a)


# 2.Créer une fonction qui convertit une liste de coordonnées cartésiennes (x, y)
# en coordonnées polaires (rayon, angle)
def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    for i in range(len(cartesian_coordinates)-1):
        module = np.sqrt(cartesian_coordinates[i] ** 2 + cartesian_coordinates[i+1] ** 2)
        angle = np.arctan2(cartesian_coordinates[i+1], cartesian_coordinates[i])
    return module,angle


# 3.Créer un programme qui trouve l’index de la valeur la plus proche d’un nombre fournit
# dans un array.
# def find_closest_index(values: np.ndarray, number: float) -> int:
#     return np.argmin(abs(values - number)

# b = np.linspace(-1.3, 2.5, 10)

# print(find_closest_index(b, 1.1))

# 5.Évaluer l’intégrale ∫_(−∞)^∞ 𝑒^(−𝑥^2) 𝑑𝑥. Afficher dans un graphique ∫𝑒^(−𝑥^2) 𝑑𝑥 pour x = [-4, 4].
func = lambda x : exp(-x**2)
print(quad(func, -np.inf, np.inf))

x = Symbol("x")
y = integrate(exp(-x**2), (x< -00, 00))
print(y)
print(np.sqrt(np.pi))

z = integrate(exp(-x**2), x)
pprint(z)
plot(z, (x, -4, 4))

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    pass
