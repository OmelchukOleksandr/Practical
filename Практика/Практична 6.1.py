a = []

for _ in range(3):
    a.append([0]*3)

for i in range(3):
    for j in range(3):
        a[i][j] = int(input('Введіть координату: '))

print(a)
f = (a[0][0]*a[1][1]*a[2][2])+(a[0][2]*a[1][0]*a[2][1])+(a[0][1]*a[1][2]*a[2][0])-(a[0][2]*a[1][1]*a[2][0])-(a[0][1]*a[1][0]*a[2][2])-(a[0][0]*a[1][2]*a[2][1])
print(f)
                                                                            
