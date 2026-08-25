import counter as c
s = " the cat sat on the mat that the cat sat on"
res = c.count(s)

for w, count in res.items():
    print(w,'->',count)
