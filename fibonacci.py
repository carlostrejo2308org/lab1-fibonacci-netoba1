num = int(input("Longitud de la sucesión  "))

n1 = 0
n2 = 1
l = 0

if num == 1:
   print(n1)

else:
   print("Secuencia:")
   while l < num:
       print(n1)
       nsum = n1 + n2
       
       n1 = n2
       n2 = nsum
       l += 1