print("Triangle validity experience")

a=int(input("What is the length of one of the sides?"))
b=int(input("What is the length of another side of supposed triangle?"))
c=int(input("What is the length of the last side of the supposed triangle"))

if (a+b <= c or a+c <=b or b+c <=a):
  x=False
else:
  x=True

if x==True:
  print("The sides make a Triangle")
else:
  print("The sides do not make a Triangle")
  
  
  # Another way
def triangle_check(l1,l2,l3):
    if (l1>l2+l3) or (l2>l1+l3) or (l3>l1+l2):
        print('No, the lengths wont form a triangle')
    elif (l1==l2+l3) or (l2==l1+l3) or (l3==l1+l2):
        print('yes, it can form a degenerated triangle')
    else:
        print('Yes, a triangle can be formed out of it')
length1 = int(input('enter side 1\n'))
length2 = int(input('enter side 2\n'))
length3 = int(input('enter side 3\n'))
triangle_check(length1,length2,length3)
  
