name =input("Enter your name: ")
sig=input("Enter the signals: ")
g=0
h=0
r=0
s=0

for i in range(len(sig)):
   if sig[i]=='G' or sig[i]=='g':
       g+=1
   if sig[i]=='H' or sig[i]=='h':
           h+=1
   if sig[i]=='R' or sig[i]=='r':
           r+=1
   if sig[i]=='S' or sig[i]=='s':
           s+=1



if g>h and g>r and g>s:
   print(name, "you brlong in ..... Gryffindor! (",g,") signals")
elif h>g and h>r and h>s:
   print(name, "you brlong in ..... Hufflepuff! (",h,") signals")
elif r>g and r>h and r>s:
    print(name, "you brlong in ..... Ravenclaw! (",r,") signals")
elif s>h and s>r and s>g:
   print(name, "you brlong in ..... Slytherin! (",s,") signals")