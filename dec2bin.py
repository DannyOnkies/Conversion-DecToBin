##
# converts a decimal number to binary
#

def bin2dec(binario):
    lung = len(binario)
    dec = 0
    for i in range(lung):
        indice = lung - i - 1
        cifra = int(binario[indice]) * pow(2, i)
        dec = dec + cifra
    return dec


bin2conv = input("Enter the binary number to convert to decimal ...")

print(bin2dec(bin2conv))
