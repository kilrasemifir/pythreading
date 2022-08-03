liste1 = [1, 2, 3, 4, 5]
liste2 = ['a', 'b', 'c', 'd', 'e']
liste3 = [1, 2, 3, 4, 5]
for i in range(len(liste1)):
    print(liste1[i], liste2[i])

for chiffre, lettre, chiffre2 in zip(liste1, liste2, liste3):
    print(chiffre, lettre, chiffre2)

for t in zip(liste1, liste2, liste3):
    print(t)

for i, val in enumerate(liste1):
    print(i, val)
print(zip(liste1, liste2))

var = (-1)
vart = (1,)
print(var, vart)
