N = 25
A = []

for i in range(N):
    A.append(int(input(("Введите элемент массива: "))))

cnt = 0
sm = 0
for i in A:
    if abs(i) > 0:
        cnt = cnt + 1
        sm = sm + i

avg = sm / cnt
print(avg)

for i in range(len(A)):
    if A[i] == 0:
        A[i] = 1
print(A)
p = 1
for i in A:
    p *= i
print(p)
