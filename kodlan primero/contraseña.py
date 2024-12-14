import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
usuario = int(input("cuantos caracteres quiere en su contraseña : "))
password = ""

for i in range (usuario):
    password+=(random.choice(characters))
print(password)





    

