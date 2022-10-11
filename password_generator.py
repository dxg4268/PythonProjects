"""
Password Generator
"""
import random


alpha = "abcdefghijknlmopqrstuvwxyz"
num = "1234567890"
symbol = "!@#_$%^-&*="
length = random.randrange(7,16)


#Password is to be of 3 parts - alpha part, number part and symbol part
# ex - Password = alpha + num + sym

part_len = int(length * (1/3))                       # Length of 2 part is to be one third of total length
rem_len = int(length - (2 * part_len))               # Length of third part is remaining of the length           
alpha_part = ''; num_part = ''; sym_part = ''


for k in range(part_len):
    rand_index = random.randrange(0,len(alpha))
    rand_char = alpha[rand_index]
    
    num_index = random.randrange(0,len(num))
    rand_num = num[num_index]
    
    alpha_part = alpha_part + rand_char
    num_part = num_part + rand_num


for i in range(rem_len):
    sym_index = random.randrange(0,len(symbol))
    sym = symbol[sym_index]
    sym_part = sym_part + sym


password = alpha_part + symbol[random.randrange(0,len(symbol))] + num_part
password = password + sym_part
print("[+] Generated Password : ", password)
# print(len(password))
# print(length)