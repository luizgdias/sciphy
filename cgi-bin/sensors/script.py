import os

x = os.listdir('.')
with open('lista.txt', 'w') as f:
    for item in x:
        f.write("%s_\n" % item)

txt = "isso#e#um"
x = txt.split("#")
print(x)