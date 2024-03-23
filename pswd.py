import string 
import random

def gen():
    s1 = string.ascii_uppercase # Todas as letras maiúsculas 
    s2 = string.ascii_lowercase # Todas as letras minúsculas
    s3 = string.digits # Todos os números de 0 a 9
    s4 = string.punctuation # Todos os caracteres especiais 

    passlen = int(input("Enter the password lenght:\n "))

    s = []
    # Adiconando todos os tipos de elementos à lista s
    s.extend(list(s1)) 
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s) # Embaralhando os elementos da lista 
    passw = (''.join(s[0:passlen])) # Adicionando elementos à senha final

gen()

