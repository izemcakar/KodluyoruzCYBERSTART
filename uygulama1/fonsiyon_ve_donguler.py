
import math

points = [(2,5),(-3,7),(8,-1)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazılması
def euclideanDistance( point1 , point2 ):

    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)


# Points Listesindeki Noktalar Arasındaki Mesafenin Hesaplanması
distances = []

for i in range(len(points)):
    for j in range(i+1 , len(points)):
          distance = euclideanDistance( points[i] , points[j] )
          distances.append(distance)


# Min Mesafe Değerinin Bulunması
min_mesafe = min(distances)

# Min Mesafe Değerinin Yazdırılması
print(min_mesafe)


        