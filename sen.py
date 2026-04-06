d={'Morning':'Evening','Welcome':'Thank You','Hii':'Bye'}
s=input("enter a sentence:").split(" ")
for i in s:
   if i in d:
      i=d[i]
      print(i,end=' ')
   else:
      print(i,end=' ')
