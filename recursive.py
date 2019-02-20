def fun(n):
   if n<=1:
       return 1
   else:
       return n*fun(n-1)
n=int(input("factorial number:"))
fun(n)
