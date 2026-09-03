name = []
nam = int(input("How many names to be listed?: "))

x = 1
ar = 1

while x <= nam:
  name1 = str(input("name= "))
  name.insert(ar, name1)
  x+=1
  ar+=1

print(name)
for ha in name:
  print(ha)
