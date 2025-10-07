a, b = map(int,input().split())
Z = int(a % b == 0 or b % a == 0)
print(Z)