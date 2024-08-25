# fonksiyonları obje olarak kullanmak

l = [1,2,3,4]

def apply(l , f):

    n = len(l)

    for i in range(n):
        l[i]=f(l[i])

def kare(x):
    return x**2

apply(l , kare)
print(l)   # liste fonksiyonla güncellendi.

def kup(x):
    return x**3







def apply_funcs(f_list , x):    # f_list listesininin her bir elemanı fonksiyonlardır(kare, kup)
    l = []
    for f in f_list:           # f, f_list içindeki her bir fonksiyonu temsil eder.
        l.append(f(x))

    return l

print(apply_funcs([kare , kup],5))

