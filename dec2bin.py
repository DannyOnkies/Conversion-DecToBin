##
# CONVERTS A DECIMAL TO A BINARY 

def dec_bin(n):
    b = ''
    while n > 0:
        if n % 2 == 0:
            b = '0' + b
        else:
            b = '1' + b
        n = int(n / 2)  # casting
    print(b)

c = int(input("Enter a decimal number: "))
dec_bin(c)
