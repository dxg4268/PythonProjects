#Program to check email validity
from curses.ascii import isalnum
import sys

#Input from user
email = input("[+] Enter Email Address = ")

"""
Spliting the email into 2 parts enables us to check each part separately
"""

split_email = email.split("@")


# Very first check, if email contains @ symbol
if email.find("@") == -1:
    print("[-] Invalid Email => '@' not found.")
    sys.exit("[!] Terminating further checks, Exiting...")

# storing 2 parts of email into 2 variable
prefix = split_email[0]
suffix = split_email[1]


if suffix.find('.') == -1:
    print("[-] Invalid Email => '.' expected before domain.")
    sys.exit("[!] Terminating further checks, Exiting...")


# adding a space to avoid error
prefix = prefix + ' '


def SymbolCheck(e1):
    e = e1 + 1
    if not prefix[e].isalnum():
        
        print("[-] Err => '{}' placement error. Symbol should succeed with alphanumeric charachter".format(prefix[e1], e1))
        return 1
        # print(prefix[e1])
    else:
        pass


#Different tests to validate the Email Address 
def Check(prefix,suffix):
    f = 0; f2 = 0; f3 = 0

    #prefix checks
    for i in range(len(prefix)):
        char = prefix[i]

        if char.isalnum() : f = 0 
        elif char in '-_.':

            f = SymbolCheck(i)
            if f == 1: f3 = 1

        elif char == ' ': pass
        else:
            print("[-] Err => '{}' not allowed at position {}.".format(char, i))
            f = 1


    #suffix checks
    for ch in suffix:
        if ch.isalnum(): pass 
        elif ch in '-.':
            # SymbolCheck(suffix.index(ch))
            domain = suffix.split(".")[1]
        else:
            print("[-] Err => '{}' not allowed at position {}.".format(ch, suffix.index(char)))


    #domain check
    if domain in ["com", "cc", "org"]:
        pass
    else:
        print("=> Domain Error")
        f2 = 1


    # returning a flag if there are any errors or not
    if f or f2 or f3:
        return 1
    else:
        return 0


prefix = prefix.strip()  # removing added space to check spaces enter by the user
space_flag = 0
for i in prefix:
    if i == ' ':
        space_flag = 1

#calling methods and displaying final message
check_result = Check(prefix,suffix)
if check_result and space_flag:
    print("[-] Invalid Email => These Errors were reported in the address!")
else:
    print("[+] No Errors reported")

# "aditya".isalnum()

# SymbolCheck(e)


# print(split_email)


# print("test string")
print("\n[+] Check completed !")