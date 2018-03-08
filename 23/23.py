import this

code = 'va gur snpr bs jung?'
res = ''

for i in code:
    p = this.d.get(i)
    if p:
        res += p
    else:
        res += i

print res