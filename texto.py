import math as mt


r=float(input("ingrese r"))
theta=float(input("ingrese theta"))

x=r*mt.cos(theta)
y=r*mt.sin(theta)

print (x)
print (y)

print ("PROBLEMA 2")

A=float(input("ingrese el valor de x años luz"))
v=float(input("ingrese el valor de v en fraccion de c"))

x=A*9.46e15 #m

c=3e8 #m/s
t=x/v #s

print ("parte A")

print ("t",t,"s")
print ("parte B")

R=(t-(v*x)/(c))/mt.sqrt (1-(v*v)/(c)) #s
"t=",
print ("t=",R,"s") 

print ("problema 3")

f1=1
f2=1

print (f1)
print (f2) 
f3=f1+f2
print (f3)
while f3<1000:
      f1=f2
      f2=f3
      f3=f1+f2
      if f3>1000:
             break
      print(f3)

print ("natalia m")





