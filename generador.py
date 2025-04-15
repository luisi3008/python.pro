import random

caracters = "-!$%&/=qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM"

pregunta = int(input("¿De cuántos caracteres quieres tu contraseña?"))

contra = ""

for i in range(pregunta):
    contra = contra + random.choice(caracters)
    
print(f'Tu contraseña es {contra}')