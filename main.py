import re


def validate_formula(molecule):
    element = re.split("[2-9|A-Z]", molecule)
    cuantity = re.split("\D", molecule)
    cuantity = cuantity[1:]
    print(element)
    print(cuantity)
    print(molecule)


# some tests:
test = ["H2O", "NaCl", "H2SO4", "HCl", "CHPO3"]
for i in test:
    print(f"\033[93m{validate_formula(i)}\033[0m")
