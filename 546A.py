dayso = input().split(" ")
k = int(dayso[0])
n = int(dayso[1])
w = int(dayso[2])
a= k * (w / 2) * (w + 1)
if n < a:
    c= a - n
    print(int(c))
if n>= a:
    print("0")
    