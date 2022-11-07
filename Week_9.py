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
