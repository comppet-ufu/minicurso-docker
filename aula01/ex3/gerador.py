from termcolor import colored
import random
import string

tamanho = 16
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choice(caracteres) for i in range(tamanho))

print(colored(f"\nSua nova senha segura é: {senha}\n", 'green', attrs=['bold']))
