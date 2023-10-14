import random
import string

def generar_contrasena():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(16))
    return contrasena

if __name__ == "__main__":
    contrasena_generada = generar_contrasena()
    print("Contraseña generada:", contrasena_generada)
