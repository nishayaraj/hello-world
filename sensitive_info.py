# def my_secret(str):
#  return '*'*(len(str)-4) + str[-4:]

# secret = input("What is your biggest secret ?: ->")
# print("My biggest secret is: ",my_secret(secret))

#MODIFYING THE EXERCISE USING REGEX
import re

def format_str(param_str, replace_count):
  return re.sub(r"[a-z0-9]", "*", param_str[0: replace_count],flags=re.IGNORECASE)

secret_mask_alpha_num = input("What is your biggest secret ?: ->")

#replace_count
first_sec_count = len(secret_mask_alpha_num)-4

print("My biggest secret is: ",format_str(secret_mask_alpha_num, first_sec_count)+secret_mask_alpha_num[-4:])
