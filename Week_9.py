import re



def chars_frecs(text):
    result = {}

    for i in range(len(text)):
        if text[i] in result:
            result[text[i]] += 1
        else:
            result[text[i]] = 1

    return result


def words_frecs(text):
    result = {}
    treated_text = text.split()

    for i in treated_text:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result


def change_dict(persons):
    new_DNI = 0

    for key in persons:
        new_DNI = add_letter(key)
        persons[key] = (new_DNI, persons[key])

def add_letter(DNI):
    letter_str = "TRWAGMYFPDXBNJZSQVHLCKE"
    DNI += letter_str[int(DNI) % 23]
    return DNI


def isvowel(text):
    vowels = "aeiouüáéíóúAEIOUÜÁÉÍÓÚ"
    vowels_in_list = []
    vowels_in_list[:0] = vowels

    for i in range(len(text)):
        if text[i] not in vowels_in_list:
            return False
    return True


def swap(text):
    text = text.title()
    words = text.split()
    result = ""
    for i in range(len(words)-1, -1, -1):
        result += words[i] + " "
    result = result.rstrip()
    return result


def sub2upper(text, mayus):
    return text.replace(mayus, mayus.upper())
  
  
def longest_word(text):
    text = text.split()
    result = text[0]

    for word in text:
        if len(word) >= len(result):
            result = word

    return result


def celsius2fahrenheit(celsius):
    return f"{celsius:5.1f} grados Celsius equivalen a " \
           f"{celsius * 9 / 5 + 32:5.1f} grados Fahrenheit"


def format_pows(num):
    return f"{num:>02}{num**2:>3}{num**3:$>4}"


def format_frecs(frecs):
    result = []
    for i in frecs[0]:
        result.append(f"{i:<10}:{((frecs[0][i]/frecs[1])*100):6.2f}%")
    return result


def verbs(text):
    result = []
    new_text = re.split(",|\s", text)
    for word in new_text:
        if re.search(".+(o|as|a|amos|áis|an)$", word) != None:
            result.append(word)
    return result


def replace_verbs(text):
    result = ""
    result = re.sub("(o|as|a|amos|áis|an),", "ar,", text)
    result = re.sub("(o|as|a|amos|áis|an)\s", "ar ", result)
    result = re.sub("(o|as|a|amos|áis|an)$", "ar", result)
    return result


def normalize(text):
    result = ""
    result = re.sub(" +", " ", text)
    result = re.sub("^\s", "", result)
    result = re.sub("\s$", "", result)
    return result
