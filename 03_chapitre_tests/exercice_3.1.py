###### Solution 1 ###### 
a = int(input('Saisir a:'))
b = int(input('Saisir b:'))
c = int(input('Saisir c:'))
maximum = a
minimum = b
if b > a:
    maximum = b
    minimum = a

if maximum < c:
    maximum = c
elif minimum > c:
    minimum = c

print(minimum, maximum)


###### Solution 2 ###### 
a = int(input('Saisir a:'))
b = int(input('Saisir b:'))
c = int(input('Saisir c:'))
maximum, minimum = a, b

if b > a:
    maximum, minimum = b, a

if maximum < c:
    maximum = c
elif minimum > c:
    minimum = c

print(minimum, maximum)
