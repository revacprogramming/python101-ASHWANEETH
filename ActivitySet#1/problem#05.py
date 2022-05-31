# functions
h = float(input("Enter The hours of work:"))
r = float(input("Enter the rate:"))
def computepay(h, r):
    x = h*r
    return x
if(h<=40):
   print(pay=computepay(h,r))
else:
  z= pay=computepay(40,r)+((h-40)*r*1.5)  
  print('Pay',z)