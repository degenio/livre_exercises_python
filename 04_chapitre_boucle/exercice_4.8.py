repetition = int(input("Entrez un entier : "))

figure = ""
for i in range(1, repetition + 1):
    print("repetition="+str(i))
    figure += "*" + "*" * (i - 1) + "#"
    print(figure)
