##
# CONVERTE UN DECIMALE IN UN BINARIO
# OTTIMIZZATO PER CIFRE SINO A 255
#

def dec_bin(n):
    b = ''
    while n > 0:
        if n % 2 == 0:
            b = '0' + b
        else:
            b = '1' + b
        n = int(n / 2)  # casting in intero
    # formatto il numero binario in 8 cifre;
    # se sono di meno le inserisco davanti
    if len(b) < 8:
        # inserisco tanti zeri quanti
        # ne mancano per arrivare a 8
        for i in range(8 - len(b)):
            b = "0" + b
    # inserisco uno spazio tra i due gruppi di 4 cifre
    if len(b) == 8:
        val_form = b[:4] + ' ' + b[4:]
    else:
        val_form = b
    print(val_form)


c = int(input("Inserisci un numero decimale: "))
dec_bin(c)
