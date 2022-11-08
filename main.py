import re


def validate_formula(molecule):
    splited = re.split("", molecule)
    splited = splited[1:-1]
    for i in range(len(splited)-1):
        print(splited[i])
        if splited[i].isupper():
            if not (splited[i + 1].isupper()):
                if not (splited[i + 1].islower() or splited[i + 1].isdigit()):
                    print(splited[i])
                    return False
        else:
            if splited[i].isdigit():
                if not splited[i+1].isupper():
                    return False
    return True


# some tests:
test = ["H2O", "NaCl", "H2SO4", "HCl", "CHPO3"]
for i in test:
    print(f"\033[93m{validate_formula(i)}\033[0m")
