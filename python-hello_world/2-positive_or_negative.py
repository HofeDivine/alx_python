import random

number = random.randint(-10, 10)

msg = "{} is {}".format(number, "positive" if number > 0 else "zero" if number == 0 else "negative")
print(msg)
