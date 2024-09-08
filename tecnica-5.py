# Técnica 5)
# Linguagem: Python

def inverter_string(string):
    string_invertida = ""
    for i in range(len(string)-1, -1, -1):
        string_invertida += string[i]
    return string_invertida


original = input("Digite uma string: ")
invertida = inverter_string(original)

print(f"String invertida: {invertida}")
