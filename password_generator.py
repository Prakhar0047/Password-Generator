import string
import random

alpha_lower = list(string.ascii_lowercase)
alpha_upper = list(string.ascii_uppercase)
symbols = list(string.punctuation)
numbers = list(string.digits)

print("Welcome")
print("Enter Combination you want")
sy = input("Number of Symbol:")
cap = input("Number of Uppercase Alphabets:")
low = input("Number of Lowercase Alphabets:")
num = input("Number of Number:")
pre_password = []
final_password = ''

if int(sy)+int(cap)+int(low)+int(num) < 8:
    print("\nNot a valid combination.")
    print("Total must be >= 8")

else:
    for a in range(int(sy)):
        pre_password.append(random.choice(symbols))
        
    for a in range(int(cap)):
        pre_password.append(random.choice(alpha_upper))
        
    for a in range(int(low)):
        pre_password.append(random.choice(alpha_lower))
    
    for a in range(int(num)):
        pre_password.append(random.choice(numbers))

random.shuffle(pre_password)

for ele in pre_password:  
        final_password += ele 

print("Your Password is:",final_password)