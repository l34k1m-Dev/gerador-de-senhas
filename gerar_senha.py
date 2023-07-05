from random import choice
from colorama import init, Fore, Back, Style
import string
init(autoreset=True)

print(Fore.GREEN + 47*"=")
print(Back.GREEN + "** Bem-vindo ao Sistema de Geração de Senhas **")
print(Fore.GREEN + 47*"=")

tamanho_senha = int(input("Quantos dígitos você quer na sua senha? "))
caracteres = string.ascii_letters + string.digits + string.punctuation
gerar_senha = ''
for i in range (tamanho_senha):
    gerar_senha += choice(caracteres)

print("\nA senha gerada é: ", Fore.GREEN + (gerar_senha))