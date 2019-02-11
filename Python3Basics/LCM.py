def gcd(a,b):                       #function to find Greatest Common Divisor(GCD) of two numbers
    if a<b:
        (a,b)=(b,a)
    while a%b != 0:
        (a,b)=(b,a%b)
    return b

def lcm(a,b):                       #function to find Least Common Multiple(LCM) of two numbers
    return int((a*b)/gcd(a,b))
lcm(30,40)
