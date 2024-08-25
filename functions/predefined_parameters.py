# kullanıcı değer belirtmedikçe önceden belirlenen değeri alır.

def hello(end, start = "Hello"):  # kullanıcı start'a değer atamadığı sürece Hello ata. #Predefined, ilk değişken olamaz.
    print(start , " " , end)

def f(x , y = 1 , z = 3):
    return x + y + z

print(f(2,5)) # z değeri predifened olarak 3 atılır.