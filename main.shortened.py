print(f"Licencing: GNU Public Licence V. 3.0")
def p(c):
  i=[c]
  while c!=1:
    i.append(c:=int(c/2 if not c%2 else c*3+1))
  return max(i),i,len(i)-1
s=int(input("Seed: "))
print(f"Max: {p(s)[0]}\nIntegers: {p(s)[1]}\nSteps: {p(s)[2]}")
