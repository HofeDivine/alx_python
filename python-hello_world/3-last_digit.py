#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Lastdigit = int(str(number)[-1])
if Lastdigit > 5:
    result = "{} {} is {} and {}".format("Last digit of",number,Lastdigit, "is greater than 5"  )
    print(result)
elif Lastdigit == 0:
    result = "{}  {} is {} and {}".format("last digit of",number,Lastdigit, " is 0"  )
    print(result)
elif Lastdigit < 5:
     result = "{}  {} is {} and {}".format("last digit of",number,Lastdigit, "is less than 5"  )
     print(result)
elif Lastdigit < 6 and not 0:
    result = "{}  {} is {} and {}".format("last digit of",number,Lastdigit, "and is less than 6 and not 0"  )
    print(result)