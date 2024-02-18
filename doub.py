"""n = 2
m = 3
A = []
for i in range(n*m+2):
    row=input().split()
    A.append(row)
print(A)

for i in range(n*m+2):
    for j in range(n*m+2):
        print(end='')"""
import copy

"""n = int(input())
m = int(input())
A = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    A.append(row)

for row in A:
    print(*row)""" # Матрица
"""n =int(input())
m = int(input())
A = []
lol=[]
k=[]
f=[]
for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    A.append(row)
    lol+=row
for row in A:
    print(*row)
    k.append(row)
#print(k)
print()
for i in range(m):
    b=[]
    for j in range(n):
        b.append(k[j][i])
    f.append(b)
#print(f)
for row in f:
    print(*row)""" # Транспортированная матрица
"""n=int(input())
matrix=[input().split() for i in range(n)]
niz,v,right,left=0,0,0,0
for i in range(n):
   for j in range(n):
    if i>j and i<n-1-j:
     left+=int(matrix[i][j])
    if i < j and i > n - 1 - j:
         right += int(matrix[i][j])
    if i < j and i < n - 1 - j:
        v += int(matrix[i][j])
    if i > j and i > n - 1 - j:
        niz += int(matrix[i][j])
print('Верхняя четверть: {}\nПравая четверть: {}\nНижняя четверть: {}\nЛевая четверть: {}'.format(v, right, niz, left))"""
"""for i in range(n):
   for j in range(n):
    if i<j and i>n-1-j:
     right+=int(matrix[i][j])
print('right',right)"""
"""n = int(input())
m = int(input())
mult = [[i*j for j in range(m)]for i in range(n)]

for row in mult:
    print(*[str(x).ljust(3) for x in row])""" #  Таблица умножения *
"""n = 3
m = 4
matrix = []
for i in range(n):
    row=input().split()
    matrix.append(row)
print(matrix)"""
"""n,m = int(input()),int(input())
f,p=0,0
n = [[int(x) for x in input().split()] for i in range(n)]  # Создаем матрицу с числами размером nxm с клавиатуры через пробел
maximum = n[0][0]
for i,row in enumerate(n):
        if int(max(row))>int(maximum):
            maximum=max(row)
            f,p=i,row.index(maximum)
print(f,p)""" # Индекс самого большого элемента матрицы
"""n,m = int(input()),int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]  # Создаем матрицу с числами размером nxm с клавиатуры через пробел
s = input().split()
for row in matrix:
    row[int(s[0])],row[int(s[1])] = row[int(s[1])],row[int(s[0])]
for row in matrix:
    print(*row)""" # Обмен столбцов
"""n= int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]
flag=True
for i in range(n):
    for j in range(n):
        if matrix[i][j]!=matrix[j][i]:
            flag=False
            break
if flag:
    print('YES')
else:
    print('NO')
""" # Симметричная матрица
"""n= int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]
for i in range(n):
       temp = matrix[i][i]
       matrix[i][i]  = matrix[n - i - 1][i]
       matrix[n - i - 1][i] = temp
for row in matrix:
    print(*row)""" # Обмен диагоналей
"""n = int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]
for row in matrix[::-1]:
    print(*row)""" # Зеркальное отображение
"""n = int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]
matrix.reverse()
for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=" ")
    print()""" # Поворот матрицы *
"""v = str(input())
matrix = [['.' for i in range (8)] for i in range(8)]
alf = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
row = 8-int(v[1])
col = alf[v[0]]
print(row,col)
for i in range(8):
    for j in range(8):
        if i == row and j == col:
            matrix[i][j] = 'N'
        if (i - row) ** 2 + (j - col) ** 2 == 5:
                matrix[i][j] = '*'
for row in matrix:
    print(*row)""" # Ход коня
"""pob,temp,col,row =0,0,0,0
n= int(input())
flag=bool
myset=set()
matrix = [[int(x) for x in input().split()] for i in range(n)]
dubl=[i for i in range(1,(n*n)+1)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] in dubl:
            dubl.remove(matrix[i][j])
        else:
            flag=False
if flag:
    for i in range(n):
        myset.add(sum(matrix[i]))
        temp +=  matrix[i][i]
        for j in range(n):
            col+=matrix[j][i]
            pob+=matrix[n - i - 1][i]
        myset.add(col)
        col=0
    myset.add(int(pob / n))
    myset.add(temp)
    if len(myset)>1:
        print('NO')
    else:
        print('YES')
else:
    print('NO')""" # Магический квадрат
"""s=input().split()
n=int(s[0])
m=int(s[1])
matrix=[]
for i in range(n):
    row=[]
    if i%2==0:
     row = ['.' if j % 2 == 0 else '*' for j in range(m)]
    else:
     row=['*' if j % 2 == 0 else '.' for j in range(m)]
    matrix.append(row)
for i in matrix:
    print(*i)""" # Шахматная доска
"""n=int(input())
matrix = [[1 if i+j==n-1 else 2 if i+j>=n else 0 for j in range(n)]for i in range(n)]
for row in matrix:
    print(*row)""" # Побочная диагональ
"""s=input().split()
n=int(s[0])
m=int(s[1])
matrix = [i for i in range(1,m*n+1)]
for row in range(0, m*n, m):
    row_values = matrix[row:row+m]
    formatted_row = ' '.join('{:<3}'.format(value) for value in row_values)
    print(formatted_row)""" # Заполнение 1
"""n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
l=1
for i in range(n):
    l=i+1
    for j in range(m):
        matrix[i][j] =l
        l+=n
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()"""# Заполнение 2
"""n = int(input())
matrix=[[1 if i==j else 1 if n == i + j + 1 else 0 for j in range(n) ]for i in range(n)]
for row in matrix:
    print(*row)""" # Заполнение 3
"""n = int(input())
matrix=[[1 if i<=j and i<=n-1-j else 1 if i>=j and i>= n-1-j  else 0 for j in range(n) ]for i in range(n)]
for row in matrix:
    print(*row)""" # Заполнение 4
"""n, m = [int(i) for i in input().split()]
lol=[]
matrix = [[0] * m for _ in range(n)]
base= [i for i in range(1,m+1)]
for row in matrix:
    lol.append(list(base))
    base.append(base[0])
    base.remove(base[0])
for i in lol:
    print(*i)""" #Заполнение 5 *
"""n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1
f = True
for row in matrix:
    if f:
        print(' '.join(str(num).ljust(3) for num in row))
        f = False
    else:
        row.reverse()
        print(' '.join(str(num).ljust(3) for num in row))
        f = True""" #Заполнение змейкой
"""n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
x=1
for k in range(n*m):
 for i in range(n):
        for j in range(m):
            if i+j==k:
                matrix[i][j]=x
                x+=1
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()""" # Заполнение диагоналями *
"""n, m = [int(i) for i in input().split()]
num = 1
right=m
top=0
down=n-1
left=0
matrix = [[0 for j in range(m)] for i in range(n)]
num=1
if n>1 and m>1:
    while num<=n*m:
        for i in range(left,right):
                matrix[top][i]=num
                num+=1
        top+=1
        for i in range(top,down+1):
                matrix[i][right-1]=num
                num+=1
        right-=1
        for i in range(right-1,left-1,-1):
                matrix[down][i] = num
                num += 1
        down-=1
        for i in range(down, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(2), end=' ')
        print()
elif n==1:
    matrix=[i for i in range(1,m+1)]
    print(*matrix)
elif m==1:
    matrix = [[i] for i in range(1, n+1)]
    for i in matrix:
        print(*i)""" # Заполнение по спирали
"""n, m = [int(i) for i in input().split()]
a=[input().split() for i in range(n)]
s=input()
b=[input().split() for i in range(n)]
c=[[0 for j in range(m)]for i in range(n)]
for i in range(n):
    for j in range(m):
        c[i][j]=int(a[i][j])+int(b[i][j])
for i in c:
        print(*i)
""" # Сложение матриц
"""rowa, cola = [int(i) for i in input().split()]
a = [input().split() for i in range(rowa)]
s=input()
rowb, colb = [int(i) for i in input().split()]
b = [input().split() for i in range(rowb)]
c = [[0 for j in range(colb)] for i in range(rowa)]
for i in range(rowa):
    for j in range(colb):
        sum = 0
        for k in range(cola):
            sum += int(a[i][k]) * int(b[k][j])
        c[i][j] = sum
for i in c:
    print(*i)""" # Умножение матриц
"""n=int(input())
matrix = [input().split() for i in range(n)]
k=int(input())
c = [[0 for j in range(n)] for i in range(n)]
test = [[0 for j in range(n)] for i in range(n)]
copymatrix= copy.deepcopy(matrix)
for r in range(k-1):
    if r<1:
        for i in range(n):
                for j in range(n):
                    sum = 0
                    for y in range(n):
                     sum += int(matrix[i][y]) * int(copymatrix[y][j])
                    c[i][j] = sum
    else:
        test = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                sum = 0
                for y in range(n):
                    sum += int(copymatrix[i][y]) * int(c[y][j])
                test[i][j] = sum
        c=copy.deepcopy(test)
for i in c:
    print(*i)""" # Возведение в стпень
"""s = input().split()
shag=int(input())
res=[]
for i in range(shag):
    row = []
    for j in range(i,len(s),shag):
            row.append(s[j])
    res.append(row)
print(res)""" # Каждый n-ый элемент
"""n = int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]  
maximum = matrix[0][0]
for i in range(n):
        for j in range(n):
            if  i>=n-1-j:
                if matrix[i][j]>maximum:
                 maximum=matrix[i][j]
print(maximum)""" # Максимальный в области 2
"""n = int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[j][i],end=' ')
    print()""" # Транспортированя  матрица
"""n = int(input())
matrix=[['*' if i==j or i==n//2 or j==n//2 else '*' if n == i + j + 1 else '.' for j in range(n) ]for i in range(n)]
for row in matrix:
    print(*row)""" # Вывод снежинкой
"""n= int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]
flag=True
for i in range(n):
    for j in range(n):
        if matrix[i][j]!=matrix[n-1-j][n-i-1]:
            flag=False
            break
if flag:
    print('YES')
else:
    print('NO')""" # Семетрия относитльно побочной диагонали
"""n= int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]
myline=[i for i in range(1,n+1)]
f=True
test = [[0 for x in range(n)] for i in range(n)]
for i in range(n):
        if sorted(matrix[i])!=myline:
            f=False
            break
for i in range(n):
     for j in range(n):
            test[i][j]=matrix[j][i]
for i in range(n):
        if sorted(test[i])!=myline:
            f=False
            break
if f:
    print('YES')
else:
    print('NO')
""" #  Латинский квадрат *
"""v = str(input())
matrix = [['.' for i in range (8)] for i in range(8)]
alf = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
row = 8-int(v[1])
col = alf[v[0]]
for i in range(8):
    for j in range(8):
        if i==row or j==col or abs(row - i) == abs(col - j) and matrix[i][j]!= 'Q':
            matrix[i][j] = '*'
        if i == row and j == col:
            matrix[i][j] = 'Q'
for row in matrix:
    print(*row)""" # Ход ферзя
"""n=int(input())
matrix= [[abs(i-j) if i==j else abs(i-j) if i>=j-2 else abs(i-j) for j in range(n)]for i in range(n)]
for row in matrix:
    print(*row)"""
"""tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if i !=tuples[0] ]
print(non_empty_tuples)""" # Кортежи
"""tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples =[]
for i in tuples:
    a=list(i)
    a[len(a)-1]=100
    new_tuples.append(tuple(a))
print(new_tuples)""" # Кортежи
"""numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
temp=list(numbers)
c=temp[0]
for i in temp[1:]:
    c*=(i)
print(c)""" # Кортежи
"""poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
temp=list(poet_data)
temp[2]='Москва'
poet_data=tuple(temp)
print(poet_data)""" # Кортежи
"""numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
temp = []
res=0
for i in numbers:
    for j in i:
        l=len(i)
        res+=j/l
    temp.append(res)
    res=0
print(temp)""" # Кортежи
"""a,b,c=int(input()),int(input()),int(input())
elone=(-(b/(2*(a))))
eltwo=(4*(a*c)-(b**2))/(4*a)
temp=[elone,eltwo]
print(tuple(temp))""" # Кортежи
"""n=int(input())
mat=[]
for i in range(n):
    row = input().split()
    mat.append(row)
for i in mat:
    print(*i)
print()
for i in range(n):
    if int(mat[i][1])>3:
        print(*mat[i])""" # Кортежи
"""n = int(input())
f1, f2,f3 = 1, 1,1
for i in range(n):
    print(f1,end=' ')
    f1, f2, f3 = f2, f3, f1 + f2 + f3""" # Трибоначи
"""n = int(input())
m= int(input())
k=int(input())
x=int(input())
y=int(input())
z=int(input())
print((n+m+k)-x-y+z)""" # Множесства
"""n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
b=n+m-t-x
c=k+m-t-y
d=n+k-t-z
res=(n-(b+t+d))+(m-(b+t+c))+(k-(c+d+t))
res2=b+c+d
print(res)
print(res2)
print(a-(res+res2+t))""" # Множесства
"""s=input()
myset= len(s)-len(set(s))
if myset>0:
    print('NO')
else:
    print('YES')""" # Множесства
#print('YES' if len(set(input() + input()))==10 else 'NO') Все 10 цифр
#print('YES' if sorted(set(input())) == sorted(set(input())) else 'NO') Одинаковые наборы
"""s=input().split()
print('YES' if sorted(set(s[0])) == sorted(set(s[1]))==sorted(set(s[2])) else 'NO')
"""# Уникальные символы
"""n=int(input())
s=[input().lower() for i in range(n)]
for i in s:
    print(len(set(i)))""" # Уникальные символы
"""n=int(input())
s=[input().lower() for i in range(n)]
с=''
for i in s:
    с+=i
print(len(set(с)))""" # Уникальные символы 2
"""s=input().lower().split()
ss=[[j for j in i if j.isalpha()] for i in s]
myset=set()
c=''
for i in ss:
    for j in i:
        c+=str(j)
    myset.add(c)
    c=''
print(len(myset))
""" # Количество слов в тексте
"""s=input().split()
myset=set()
for i in range(0,len(s)):
        if int(s[i]) not in myset:
            print('NO')
            myset.add(int(s[i]))
        else:
            print("YES")
""" #Встречалось ли число раньше?
"""s1,s2 = input().split(),input().split()
s1=[i for i in s1]
s2=[i for i in s2]
myset1,myset2 = set(s1),set(s2)
myset3= myset1&myset2
print(len(myset3))""" #Количество совпадающих
"""s1 = set([int(i) for i in input().split()])
s2 = set([int(i) for i in input().split()])
s3= s1 - s2
print(*sorted(set(s3)))""" # Числа первой строки
"""n=int(input())
s=[set(input()) for i in range(n)]
ms=s[0]
for i in s:
    ms=ms & i
print(*sorted(ms))
""" #Общие цифры
"""s1=set(input())
s2=set(input())
print('NO' if s1.isdisjoint(s2) else 'YES')""" # Одинаковые цифры


"""s1=set(input().split())
s2=set(input().split())
s3=set(input().split())
my=s1 & s2
print(*sorted(my-s3, reverse=True, key=int))""" #Урок информатики
"""s1=set(input().split())
s2=set(input().split())
s3=set(input().split())
last= s1 & s2 &s3
my=s1 | s2 | s3
print(*sorted(my-last, key=int))""" #Урок математике
"""s1=set(input().split())
s2=set(input().split())
s3=set(input().split())
onion= s1 | s2
print(*sorted(s3-onion,reverse=True, key=int))""" #Урок физики
"""s1=set(input().split())
s2=set(input().split())
s3=set(input().split())
onion= s1 | s2 | s3
myset = set(str(i) for i in range(11))
print(*sorted(myset-onion, key=int))""" #Урок биологии

"""words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
s={  i[0].lower() for i in words }
print(*sorted(s))""" # Генератор множеств
"""sentence = '''My very photogenic mother died in a freak accident 
(picnic, lightning) when I was three, and, save for a pocket of warmth 
in the darkest past, nothing of her subsists within the hollows and dells of memory, 
over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those 
redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the 
bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
words = {word.lower().strip('.,;:-?!()') for word in sentence.split() if len(word.strip('.,;:-?!()'))<4}
print(*sorted(words))""" # Генератор множеств

"""files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
words = {word.lower() for word in files if word.lower().endswith('png') == True}
print(*sorted(words))""" # Генератор множеств

"""n,m,k,p=int(input()),int(input()),int(input()),int(input())
print(n-((m-p)+(k-p)+p))""" # Экзамен множества
"""s= input().split()
#l=len(s)
res = {int(i) for i  in s}
print(len(s)-len(res))"""  # Экзамен множества
"""n=int(input())
citis=[input() for i in range(n+1)]
s={ i for i in citis}
print('OK' if len(s)==n+1 else 'REPEAT')"""# Экзамен множества
"""n=int(input())
m=int(input())
home = [input() for _ in range(n)]
dz= [input() for _ in range(m)]
for book in dz:
    if book in home:
        print('YES')
    else:
        print('NO')""" # Экзамен множества
"""f=input().split()
s=input().split()
first={int(i) for i in f}
sec={int(i) for i in s}
s3=first & sec
if len(s3)==0:
    print('BAD DAY')
else:
    print(*sorted(s3, reverse=True))""" # Экзамен множества
"""first={int(i) for i in input().split()}
sec={int(i) for i in input().split()}
print('YES' if sorted(first)==sorted(sec) else 'NO')""" # Экзамен множества
"""m, n = int(input()), int(input())
matem = {input() for i in range(m)}
infa= {input() for i in range(n)}
print(len( matem - infa))
""" # Экзамен множества
"""m, n = int(input()), int(input())
matem = {input() for i in range(m)}
infa= {input() for i in range(n)}
print('NO' if (matem ^ infa)==set() else len(matem ^ infa))""" # Экзамен множества
"""matem = {i for i in input().split()}
infa= {i for i in input().split()}
print(*sorted(matem | infa))""" # Экзамен множества
"""m, n = int(input()), int(input())
s=[input() for i in range(m+n)]
myset=set(s)
c = (len(s)-len(myset))*2
res = m+n -c
print('NO' if res ==0 else res)""" # Экзамен множества *
"""m = int(input())
lessons_data = []
for i in range(m):
    n = int(input())
    lesson_attendance = {input() for j in range(n)}
    lessons_data.append(lesson_attendance)
xui=lessons_data[0]
for i in lessons_data[1:]:
    xui=xui & i
for i in sorted(xui):
    print(i)""" # Экзамен множества *




