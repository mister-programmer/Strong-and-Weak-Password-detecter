s = open(passlist.txt")
password = input("Enter the password : ")
if password in s:
	print("Weak password")

elif password not in s:
	print("Strong password")

else:
	while (True):
		password = input("please enter a password")
		continue
s.close()
