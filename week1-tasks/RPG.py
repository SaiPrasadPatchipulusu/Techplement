import random
#Letters used in the password
upper_Case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_Case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Numbers=['0','2','3','4','5','6','7','8','9']
spl_char=['!','@','#','$','%','^','&','*']
No_UC=int(input("Enter number of Upper case letters ="))
No_LC=int(input("Enter number of Lower case letters ="))
No_NUM=int(input("Enter number of NUMBERS ="))
No_SC=int(input("Enter number of Spl Charecters="))
Password_list=[]
for i in range(1, No_UC+1):
    a=random.choice(upper_Case)
    Password_list += a
for i in range(1, No_LC+1):
    a=random.choice(lower_Case)
    Password_list += a
for i in range(1, No_NUM+1):
    a=random.choice(Numbers)
    Password_list+= a
for i in range(1, No_SC+1):
    a=random.choice(spl_char)
    Password_list += a
#shuffling the letters for more security
random.shuffle(Password_list)
Password=''
#changeing the list into string
for i in Password_list:
    Password+=i
print(Password)
