from cryptography.fernet import Fernet

#Aquí puedo generar una nueva llave Fernet para encriptar.
key = Fernet.generate_key()

#La llave se imprime en formto base64
print(key.decode('utf-8'))
