line = input("input 8 bit of info: ")
while line != "":
 if line.count("0") + line.count("1") != 8 or len(line) != 8:
    print("this is not 8 bit")
 else:
    ones = line.count("1")
 if ones % 2 == 0:
    print("Parity bit must be equal to 0.")
 else:
    print("Parity bit must be equal to 1.")
 line = input("input 8 bit of info: ")
