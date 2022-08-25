def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))


print("longitud: ")
l = int(input())

print("Secuencia:")
for i in range(l):
    print(fibonacci(i))
