out_f ="counted.txt"
of = open(out_f, 'w')

# f = open('ssorted.txt') 
f = open('sorted.txt') 

counter = 0 

for line in f:
   line = line.strip()
   if len(line) == 0:
      continue
   if counter == 0:
      prevLine = line
   if line == prevLine: 
      counter = counter + 1
   else:
      out_line = prevLine+"\t"+str(counter)+"\n"
#      print(out_line.strip())
      of.writelines(out_line)
      counter = 1
   prevLine = line
f.close()
of.close()