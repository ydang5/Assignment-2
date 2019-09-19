def c_to_f (c):
    #Formular = (c * 9/5) +32
    f = (c * 9/5) + 32
    return f
f = c_to_f (c)

def c_to_k (c):
    #function convert is: c+ 273.15
    k = c + 273.15
    return k
k = c_to_k (c)

def f_to_c (fahr):
    # Function of Fahrenheit to Celsius is: (F - 32) x .5556 = C
    c = (f - 32) * 0.5566
    return c
c = f_to_c (f)

def f_to_k(fahr):

    k = (f - 32) * 5/9 + 273.15
    return k
k = f_to_k(f)

# Kelvin to Celsius
def k_to_c (celsius):
    #formular for Kelvin to Celsius is C = K - 273.15
    c = k - 273.15
    return c
c = k_to_c (k)

# Kelvin to Fahrenheit
def k_to_f (k):

    f = - (k - 273.15) * 9/5 +32
    return f
f = k_to_f (k)
