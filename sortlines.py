out_f ="sorted.txt"
of = open(out_f, 'w')

with open("cleandata.txt", "r") as f:
    lines = f.readlines()
    lines.sort()        
    f.seek(0)
    of.writelines(lines)

f.close()
of.close()