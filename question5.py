# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(input_string):
    string_invertida = ""
    for char in input_string:
        string_invertida = char + string_invertida
    return string_invertida

entrada_do_usuario = input("Digite uma string: ")
resultado_invertido = inverter_string(entrada_do_usuario)
print(f"String invertida: {resultado_invertido}")
