#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Lastdigit = int(str(number)[-1])
if Lastdigit > 5 and number>0:
    result = "{} {} is {} and {}".format("Last digit of",number,Lastdigit, "is greater than 5"  )
    print(result)
elif Lastdigit == 0:
    result = "{} {} is {} and {}".format("Last digit of",number,Lastdigit, "is 0"  )
    print(result)


if  number<0 and Lastdigit!= 0:
    Lastdigit *= -1
    result = "{} {} is {} and {}".format("Last digit of",number,Lastdigit, "is less than 6 and not 0"  )
    print(result)

