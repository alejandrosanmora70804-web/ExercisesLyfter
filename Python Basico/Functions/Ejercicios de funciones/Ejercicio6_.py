def alphabetically_ordered(string):
    words = string.split("-")
    words.sort()
    result = "-".join(words)
    return result


print(alphabetically_ordered("python-variable-funcion-computadora-monitor"))

# split("-") --> separa el texto en una lista
# sort() --> ordena la lista alfabéticamnete
# joint("-") --> une la lista en un striing con guiones