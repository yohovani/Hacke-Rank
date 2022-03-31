def birthday(s, d, m):
    # Write your code here
    contador = 0
    if len(s) == 1 and m == 1:
        if s[0] == d:
            return 1
    for i in range(len(s)-m+1):
        aux = s[i]
        for j in range(1,m):
            aux += s[i+j]
        if aux == d:
            contador += 1
    print(contador)
s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
d = 18
m = 7
birthday(s,d,m)