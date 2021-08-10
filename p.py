
import random

lent=1
  
  


for i in range(1000):
   st=str(i)
   tx=".txt"
   a="bcdfghjklmnpqrstvwxz"
   b="aeiouy"
   rm1=random.sample(a,lent)
   rm2=random.sample(b,lent)
   rm3=random.sample(a,lent)
   rm4=random.sample(b,lent)
   rm5=random.sample(a,lent)
   rm6=random.sample(b,lent)
   rm7=random.sample(a,lent)
   rm8=random.sample(b,lent)

   word="".join(rm1+rm2+rm3+rm4+rm5+rm6+rm7+rm8)

   c=word+st+tx
   
   f= open(c,"w")
   f.write(word+" hack your vsd")
   
   print(c)
   

else :
  m= input()
