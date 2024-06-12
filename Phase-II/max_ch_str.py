dk = 'dsisineh'
d = {}
for i in dk:
    if i in d:
        d[i] += 1
    else :
        d[i] = 1
print(d)
print(min(d,key = lambda x:(-d[x],x)))