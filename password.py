import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '{}()[]/@#;_*.'
number = '0123456789'

all = lower + upper + symbol + number
length = int(input("Enter desired length of the password:"))
password = "".join(random.sample(all,length))
print("The password generated for you is: ",password)
