hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))
if hrs<= 40:
  pay = hrs*rate
elif hrs>40:
    h = hrs-40
pay = (40*rate)+h*rate*1.5
print(pay)