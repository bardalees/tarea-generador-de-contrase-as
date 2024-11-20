import random
digits= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
user= int(input("Cantidad de digitos de la contraseña"))
if user <=0:
    print('debe seleccionar al menos un digito')
else:
    password= ''.join(random.choice(digits)for i in range (user))
    print('tu contraseña es' , password)