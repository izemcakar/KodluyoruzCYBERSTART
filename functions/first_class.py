# python dilinde fonksiyonlar first class function olarak yaratılmıştır

# bir fonksiyon bir değişkene atanabilir

def kare(x):
    return x**2

a = kare
print(a(5))


#bir fonksiyonu başka bir fonksiyona argüman olarak verebilirsiniz.

def f2(x , f):
    return f(x) + 4

print(f2(3 , kare))
