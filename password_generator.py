from random import sample
import time

length = int(input("Enter the length of password  :"))
password_set = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

print("Generating password...")

for i in range(3):
    time.sleep(1)
    print(".")




password = "".join(sample(password_set,length))
print("Generated password : ",password)
    
