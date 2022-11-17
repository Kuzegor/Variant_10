from random import randint

def randomPassword():
     randomLength = randint(7, 10)
     result = ""
     for i in range(randomLength):
        randomChar = chr(randint(33, 126))
        result = result + randomChar
     return result

print("random password:", randomPassword())

